from .base import KillChallenge
from ..unlocks import AdditionalDropsUnlockable


class VermivorousKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Vermivorous Slain"
        self.unlockable = AdditionalDropsUnlockable()
        self.required_enemy = "GD_BugMorphRaid.Character.CharClass_BugMoprhRaid"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
