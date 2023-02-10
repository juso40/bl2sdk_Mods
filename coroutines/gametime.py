import unrealsdk

__all__ = ["Time"]


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
