from abc import abstractmethod
from dataclasses import asdict

import unrealsdk

from ..challenge import Challenge
from ...events import KilledEnemyEventManager
from ...rewards import Reward


class KillsChallenge(Challenge):
    def __init__(self):
        self.has: int = 0
        self.needs: int = 0
        self.track: str = "Stuff"
        self.playthrough_index: int = 0
        self.level: int = 0

    @abstractmethod
    def on_killed_enemy(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> None:
        pass

    @property
    def progress(self) -> str:
        if self.completed:
            return f"[{self.needs}/{self.needs}]"  # Dont over-add
        return f"[{self.has}/{self.needs}]"

    def activate(self) -> None:
        KilledEnemyEventManager.add(self.on_killed_enemy)

    def deactivate(self) -> None:
        KilledEnemyEventManager.remove(self.on_killed_enemy)

    def load_progress(self, save_dict: dict):
        own_dict = save_dict.get(self.key, {})
        self.claimed = own_dict.get("claimed", False)
        self.has = own_dict.get("has", 0)
        self.needs = own_dict.get("needs", 0)

        self.track = own_dict.get("tracks", "Stuff")
        self._name = own_dict.get("name", "Kills")

        reward_data = own_dict.get("reward", None)
        if reward_data:
            self.reward = Reward(**reward_data)
        else:
            self.reward = None
        self.playthrough_index = own_dict.get("playthrough", 0)
        self.level = own_dict.get("level", 0)

    def save_progress(self, save_dict: dict):
        save_dict[self.key] = {
            "claimed": self.claimed,
            "has": self.has,
            "needs": self.needs,
            "tracks": self.track,
            "name": self._name,
            "playthrough": self.playthrough_index,
            "level": self.level,
            "reward": asdict(self.reward),
        }

    def set_playthrough(self, playthrough: int) -> None:
        self.playthrough_index = playthrough

    def set_level(self, level: int) -> None:
        self.level = level

    def reset_progress(self):
        self.has = 0
