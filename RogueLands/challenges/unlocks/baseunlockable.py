from abc import ABC, abstractmethod


class BaseUnlockable(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        self.name: str = name

    @abstractmethod
    def unlock(self) -> None:
        pass

    @abstractmethod
    def lock(self) -> None:
        pass
