from .base import KillChallenge
from ..unlocks import VendorUnlockable


class PyroPeteKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyro Pete Slain"
        self.unlockable = VendorUnlockable()
        self.required_enemy = "GD_Iris_Raid_PyroPete.Character.CharClass_Iris_Raid_PyroPete"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
