from .. import ui_util

from abc import ABC, abstractmethod


class Stat(ABC):
    stats = []

    name: str
    value: int
    total_value: int

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Stat.stats.append(cls())

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def register_hooks(self) -> None:
        pass

    @abstractmethod
    def remove_hooks(self) -> None:
        pass

    def on_death(self) -> None:
        self.value = 0

    @abstractmethod
    def load_stat(self, save_dict: dict) -> None:
        pass

    @abstractmethod
    def save_stat(self, save_dict: dict) -> None:
        pass

    @property
    def readable_stat_run(self) -> str:
        return Stat.format_stat(self.name, self.value)

    @property
    def readable_stat_total(self) -> str:
        return Stat.format_stat(self.name, self.total_value)

    @staticmethod
    def format_stat(name: str, val: int) -> str:
        return f"[funstat]{name}: {ui_util.color_text(str(val), ui_util.Colors.YELLOW)}"
