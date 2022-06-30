from abc import ABC, abstractmethod

from ..rewards import Reward


class Challenge(ABC):
    _name: str
    key: str  # Used in ChallengeManager and for saving progress
    reward: Reward
    claimed: bool = False
    level: int = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    @abstractmethod
    def progress(self) -> str:
        pass

    @abstractmethod
    def activate(self) -> None:
        pass

    @abstractmethod
    def deactivate(self) -> None:
        pass

    @property
    @abstractmethod
    def completed(self) -> bool:
        pass

    @abstractmethod
    def load_progress(self, save_dict: dict) -> None:
        pass

    @abstractmethod
    def save_progress(self, save_dict: dict) -> None:
        pass

    @abstractmethod
    def set_playthrough(self, playthrough: int) -> None:
        pass

    @abstractmethod
    def set_level(self, level: int) -> None:
        pass

    @abstractmethod
    def reset_progress(self) -> None:
        pass
