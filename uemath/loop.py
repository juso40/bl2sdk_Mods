from dataclasses import dataclass
from time import time
from typing import Callable, List, Optional, Union

import unrealsdk

__all__ = [
    "Time",
    "WaitCondition", "WaitWhile", "WaitForSeconds",
    "TickFunction", "PostRenderFunction",
    "post_render", "tick", "register_tick", "remove_tick",
    "register_post_render", "remove_post_render",
]


class _Time:

    def __init__(self):
        self._delta_time: float = 0
        self._time: float = 0
        self._time_scale: float = 1
        self._unscaled_delta_time: float = 0

    @property
    def delta_time(self) -> float:
        """The time in seconds from the last frame to the current frame. Affected by timescale."""
        return self._delta_time

    @property
    def time(self) -> float:
        """The time in seconds at the beginning of the current frame."""
        return self._time

    @property
    def time_scale(self) -> float:
        """The scale at which the time is passing."""
        try:
            self._time_scale = unrealsdk.GetEngine().GetCurrentWorldInfo().TimeDilation
        except (AttributeError, TypeError):
            pass
        return self._time_scale

    @time_scale.setter
    def time_scale(self, value: float):
        self._time_scale = value
        unrealsdk.GetEngine().GetCurrentWorldInfo().TimeDilation = value

    @property
    def unscaled_delta_time(self) -> float:
        """The time in seconds from the last frame to the current frame, ignoring timescale."""
        return self._unscaled_delta_time


Time = _Time()


class WaitForSeconds:
    """Wait for the specified amount of time."""

    def __init__(self, seconds: float, unscaled: bool = False):
        self._seconds: float = seconds
        self._start_time: float = Time.time
        self._unscaled: bool = unscaled

    def __call__(self) -> bool:
        """Return True if the time has not passed, False if it has."""
        if self._unscaled:
            return Time.time - self._start_time < self._seconds
        return Time.time - self._start_time < self._seconds / Time.time_scale


class WaitWhile:
    """Wait until the condition is false."""

    def __init__(self, condition: Callable[[], bool]):
        self._condition: Callable[[], bool] = condition

    def __call__(self) -> bool:
        """Return True if the condition is still true, False if it is false."""
        return self._condition()


WaitCondition = Optional[Union[WaitForSeconds, WaitWhile]]
TickFunction = Callable[[], WaitCondition]
PostRenderFunction = Callable[[unrealsdk.UObject], WaitCondition]


@dataclass
class _TickFunction:
    __slots__ = ("function", "wait")
    function: Union[TickFunction, PostRenderFunction]
    wait: Optional[WaitCondition]


_TICK: List[_TickFunction] = []
_POST_RENDER: List[_TickFunction] = []


def tick(wait: Optional[WaitCondition] = None) -> Callable[[TickFunction], TickFunction]:
    """Decorate a function to add it to the tick loop. Optionally add a wait condition.

    Example:
        >>> @tick()
        >>> def tick_once_per_second():
        >>>    print("Hello World!")
        >>>    return WaitForSeconds(1)
    """

    def decorator(function: TickFunction) -> TickFunction:
        if f"{function.__module__}.{function.__qualname__}" in (
                f"{t.function.__module__}.{t.function.__qualname__}" for t in _TICK
        ):
            return function
        _TICK.append(_TickFunction(function, wait))
        return function

    return decorator


def post_render(wait: Optional[WaitCondition] = None) -> Callable[[PostRenderFunction], PostRenderFunction]:
    """Decorate a function to add it to the post render loop. Optionally add a wait condition.

    Example:
        >>> @post_render()
        >>> def my_post_render_function(canvas: unrealsdk.UObject):
        >>>    canvas.DrawText("Down Under!", False, 1, 1, ())
        >>>    return WaitWhile(lambda : unrealsdk.GetEngine().GamePlayers[0].Actor.Location.Z > 0)
    """

    def decorator(function: PostRenderFunction) -> PostRenderFunction:
        # Since inner functions can be decorated with this, we need to check if the function is already in the list
        if f"{function.__module__}.{function.__qualname__}" in (
                f"{t.function.__module__}.{t.function.__qualname__}" for t in _POST_RENDER
        ):
            return function
        _POST_RENDER.append((function, wait))
        return function

    return decorator


def register_tick(function: TickFunction, wait: Optional[WaitCondition] = None) -> None:
    """Register a function to be called every tick. Optionally add a wait condition."""
    if f"{function.__module__}.{function.__qualname__}" in (
            f"{t.function.__module__}.{t.function.__qualname__}" for t in _TICK
    ):
        return
    _TICK.append(_TickFunction(function, wait))


def remove_tick(function: TickFunction) -> None:
    """Remove a function from the tick loop."""
    for t in _TICK:
        if f"{t.function.__module__}.{t.function.__qualname__}" == f"{function.__module__}.{function.__qualname__}":
            _TICK.remove(t)
            return


def register_post_render(function: PostRenderFunction, wait: Optional[WaitCondition] = None) -> None:
    """Register a function to be called every post render. Optionally add a wait condition."""
    if f"{function.__module__}.{function.__qualname__}" in (
            f"{t.function.__module__}.{t.function.__qualname__}" for t in _POST_RENDER
    ):
        return
    _POST_RENDER.append(_TickFunction(function, wait))


def remove_post_render(function: PostRenderFunction) -> None:
    """Remove a function from the post render loop."""
    for t in _POST_RENDER:
        if f"{t.function.__module__}.{t.function.__qualname__}" == f"{function.__module__}.{function.__qualname__}":
            _POST_RENDER.remove(t)
            return


def _tick(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    Time._unscaled_delta_time = params.DeltaTime
    Time._delta_time = Time.unscaled_delta_time * Time.time_scale
    Time._time = time()

    for t in _TICK:
        if t.wait is None:  # No wait condition, just call the function
            t.wait = t.function()
            continue
        if t.wait():  # Our function has a specific wait condition, keep waiting while True
            continue
        t.wait = t.function()  # Our wait condition returned False, we can now call our function again
    return True


def _post_render(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    canvas: unrealsdk.UObject = params.Canvas
    for t in _POST_RENDER:
        if t.wait is None:
            t.wait = t.function(canvas)
            continue
        if t.wait():
            continue
        # Our wait condition returned False, we can now call our function again
        t.wait = t.function(canvas)
    return True


unrealsdk.RunHook("WillowGame.WillowGameViewportClient.PostRender", "post_render", _post_render)
unrealsdk.RunHook("WillowGame.WillowGameViewportClient.Tick", "tick_frame", _tick)
