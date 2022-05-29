from abc import ABC, abstractmethod

from .unlocks import BaseUnlockable
from ..ui_util import Colors, color_text_conditional, color_text


class Challenge(ABC):
    challenges = []

    name: str = ""
    completed: bool = False
    total_completions: int = 0
    unlockable: BaseUnlockable = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Challenge.challenges.append(cls())

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def register_hooks(self) -> None:
        pass

    @abstractmethod
    def remove_hooks(self) -> None:
        pass

    @abstractmethod
    def load_challenge(self, save_dict: dict) -> None:
        """Load this challenge from a save dict"""
        pass

    @abstractmethod
    def save_challenge(self, save_dict: dict) -> None:
        """Save this challenge to the save dictionary"""
        pass

    def check_unlockable(self) -> None:
        if self.total_completions > 0:
            self.unlockable.unlock()
        else:
            self.unlockable.lock()

    def on_death(self) -> None:
        """Reset the challenge when the player dies"""
        self.completed = False

    @property
    def challenge_unlockable(self) -> str:
        return f"[funstat]{self.unlockable.name}: " \
               f"{color_text_conditional(self.name, Colors.GREEN, Colors.RED, self.total_completions > 0)}"

    @property
    def readable_challenge_progress(self) -> str:
        """Returns a string with the current challenge progress"""
        return Challenge.format_challenge(self.name, self.completed)

    @property
    def readable_challenge_completions(self) -> str:
        """Returns a string with all the challenges that were completed"""
        return Challenge.format_challenge_total(self.name, self.total_completions)

    @staticmethod
    def format_challenge(name: str, cond: bool) -> str:
        """Returns a string with the challenge name pretty formatted"""
        return f"[funstat]{'[x]' if cond else '[   ]'}: {color_text_conditional(name, Colors.GREEN, Colors.RED, cond)}"

    @staticmethod
    def format_challenge_total(name: str, val: int) -> str:
        return f"[funstat]{name}: {color_text(str(val), Colors.YELLOW)}"  # yellow
