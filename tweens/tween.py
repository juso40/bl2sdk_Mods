from __future__ import annotations

from typing import Any, Callable, List, Optional, TypeVar, Union, cast

import unrealsdk  # type: ignore

from Mods.coroutines import (
    TickCoroutine,
    Time,
    WaitUntil,
    WaitWhile,
    start_coroutine_tick,
)

from .easing import linear

T = TypeVar("T")
PauseWhile = Union[WaitWhile, WaitUntil]

__all__ = ["Tween"]


GameIsPaused: WaitWhile = WaitWhile(
    lambda: unrealsdk.GetEngine().GamePlayers[0].Actor.IsPaused()
)


def step_tuple(tup_start: tuple, tup_end: tuple, t: float) -> tuple:
    """Step a tuple from start to end by the given t value"""
    return tuple(start + (end - start) * t for start, end in zip(tup_start, tup_end))


def step_float(start: float, end: float, t: float) -> float:
    """Step a float from start to end by the given t value"""
    return start + (end - start) * t


def step_int(start: int, end: int, t: float) -> int:
    """Step an int from start to end by the given t value"""
    return int(start + (end - start) * t)


CUSTOM_STEPS = {
    tuple: step_tuple,
    float: step_float,
    int: step_int,
}


class Tweener:
    """Base class for all Tweener objects."""

    def __init__(self, final_value: Any, duration: float) -> None:
        self._start_value: Any = 0
        self._end_value: Any = final_value
        self._duration: float = duration
        self._ease_function: Callable[[float], float] = linear
        self._elapsed: float = 0.0
        self._step_function: Callable[[Any, Any, float], Any] = CUSTOM_STEPS.get(
            type(final_value), step_float
        )

    def transition(self, ease_function: Callable[[float], float]) -> Tweener:
        """Set the easing function for this Tweener object, by default linear is used."""
        self._ease_function = ease_function
        return self

    def _reset(self) -> None:
        self._elapsed = 0.0

    def _tween_val(self, value: Any) -> None:
        raise NotImplementedError

    def step(self, delta: float) -> bool:
        """Step the tweener by the given delta time, returns True if the tweener is finished."""
        if self._elapsed >= self._duration:  # Dont tween if we are already done
            return True
        self._elapsed += delta
        t: float = self._elapsed / self._duration
        a: float = self._ease_function(t)
        value: Any = self._step_function(self._start_value, self._end_value, a)
        self._tween_val(value)
        return self._elapsed >= self._duration


class PropertyTweener(Tweener):
    """PropertyTweener tweens a value between a start and end value,
    and sets the given property to the tweened value.
    """

    def __init__(
        self,
        obj: Any,
        property_name: str,
        final_value: Any,
        duration: float,
    ) -> None:
        super().__init__(final_value=final_value, duration=duration)
        self._obj = obj
        self._property_name = property_name

    def from_val(self, value: Any) -> "PropertyTweener":
        """Set the start value for this Tweener object"""
        self._start_value = value
        return self

    def from_current(self) -> "PropertyTweener":
        """Set the start value to the current value of the property"""
        self._start_value = getattr(self._obj, self._property_name)
        return self

    def as_relative(self) -> "PropertyTweener":
        """Set the end value to be relative to the start value"""
        self._end_value += self._start_value
        return self

    def transition(self, ease_function: Callable[[float], float]) -> "PropertyTweener":
        return cast("PropertyTweener", super().transition(ease_function))

    def _tween_val(self, value: Any) -> None:
        setattr(self._obj, self._property_name, value)


class CallableTweener(Tweener):
    """CallableTweener tweens a value between a start and end value,
    and calls the given function with the tweened value.
    """

    def __init__(
        self,
        func: Callable[[Any], Any],
        start_value: Any,
        final_value: Any,
        duration: float,
    ) -> None:
        super().__init__(final_value=final_value, duration=duration)
        self._func = func
        self._start_value = start_value

    def transition(self, ease_function: Callable[[float], float]) -> "CallableTweener":
        return cast("CallableTweener", super().transition(ease_function))

    def _tween_val(self, value: Any) -> None:
        self._func(value)


class TimerTweener(Tweener):
    """TimerTweener is a special tweener that does not tween a value, but instead
    just calls the transition function every frame for the given duration.
    This can be used to add a delay to a tween sequence.
    """

    def __init__(self, duration: float) -> None:
        super().__init__(final_value=0, duration=duration)

    def transition(self, ease_function: Callable[[float], float]) -> "TimerTweener":
        return cast("TimerTweener", super().transition(ease_function))

    def _tween_val(self, value: Any) -> None:
        pass


class Tween:
    def __init__(self) -> None:
        self._completed: bool = False
        self._started: bool = False
        self._is_parallel: bool = False
        self._loops: int = 1
        self._paused: bool = False
        self._pause_while: Optional[PauseWhile] = GameIsPaused
        self._tweeners: List[Tweener] = []
        self._last_tweener: Optional[Tweener] = None

    def tween_property(
        self, object: Any, property_name: str, final_value: Any, duration: float
    ) -> PropertyTweener:
        """Create a new PropertyTweener object"""
        tweener = PropertyTweener(
            obj=object,
            property_name=property_name,
            final_value=final_value,
            duration=duration,
        ).from_current()
        self._tweeners.append(tweener)
        return tweener

    def tween_callable(
        self,
        func: Callable[[Any], Any],
        start_value: Any,
        final_value: Any,
        duration: float,
    ) -> CallableTweener:
        """Create a new CallableTweener object"""
        tweener = CallableTweener(
            func=func,
            start_value=start_value,
            final_value=final_value,
            duration=duration,
        )
        self._tweeners.append(tweener)
        return tweener

    def tween_timer(self, duration: float) -> TimerTweener:
        """Create a new TimerTweener object"""
        tweener = TimerTweener(duration=duration)
        self._tweeners.append(tweener)
        return tweener

    def kill(self) -> None:
        """Kill this Tween object and stop all tweens"""
        if self._completed:
            raise RuntimeError("Cannot kill a completed Tween object")
        if not self._started:
            raise RuntimeError("Cannot kill a Tween object that has not been started")
        self._completed = True

    def set_parallel(self, is_parallel: bool = True) -> Tween:
        """Set whether this Tween object should be executed in parallel or not.
        By default Tween objects are executed one after another.
        """
        if self._started:
            raise RuntimeError("Cannot change parallel mode on a started Tween object")
        self._is_parallel = is_parallel
        return self

    def is_running(self) -> bool:
        """Check if this Tween object is still running"""
        return self._started and not self._completed and not self._paused

    def is_paused(self) -> bool:
        """Check if this Tween object is paused"""
        return self._paused

    def is_completed(self) -> bool:
        """Check if this Tween object is completed"""
        return self._completed

    def pause(self) -> None:
        """Pause this Tween object"""
        self._paused = True

    def play(self) -> None:
        """Play this Tween object"""
        self._paused = False

    def set_loops(self, loops: int = 0) -> "Tween":
        """Set the number of times this Tween object should loop.
        If loops is smaller or equal to 0 it will loop forever, until manually killed.
        By default Tween objects only run once.
        """
        if self._started:
            raise RuntimeError("Cannot change loops on a started Tween object")
        self._loops = loops
        return self

    def pause_while(self, condition: Optional[PauseWhile]) -> "Tween":
        """Pause this Tween object while the condition is True.
        By default Tween objects are paused only while PlayerController.IsPaused() returns True.

        Args
        ----
        condition: PauseWhile
            The condition to pause this Tween object while it is True.
            If the condition is None, the Tween object will not be paused.
        """
        if self._started:
            raise
        self._pause_while = condition
        return self

    def start(self) -> None:
        """Start this Tween object"""
        if self._completed:
            raise RuntimeError("Cannot start a completed Tween object")
        if self._started:
            raise RuntimeError("Cannot start a started Tween object")
        if not self._tweeners:
            raise RuntimeError("Cannot start a Tween object without any Tweeners")
        self._started = True
        self._last_tweener = self._tweeners[-1]
        start_coroutine_tick(self._tween())

    def _tween(self) -> TickCoroutine:
        while self._loops != 0 and not self._completed:
            # While Paused we dont want to do anything, so continue
            if self._paused:
                yield
                continue

            yield self._pause_while

            delta: float = Time.delta_time
            if self._is_parallel:
                finished_tweeners: List[Tweener] = []
                for tweener in self._tweeners:
                    if tweener.step(delta):
                        finished_tweeners.append(tweener)
                # Decrement our loop, based on all finished tweeners
                if len(finished_tweeners) == len(self._tweeners):
                    for _tweener in finished_tweeners:
                        _tweener._reset()
                    if self._loops == 0:
                        break
                    self._loops -= 1

            else:  # Sequential
                _tweener: Tweener = self._tweeners[0]
                if _tweener.step(delta):
                    # Decrement our loop counter, based on the first tweener
                    if _tweener == self._last_tweener:
                        self._loops -= 1
                    # move completed tweener to the back of the list
                    self._tweeners.remove(_tweener)
                    self._tweeners.append(_tweener)
                    _tweener._reset()

        self._completed = True
