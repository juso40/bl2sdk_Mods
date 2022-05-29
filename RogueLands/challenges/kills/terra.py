from .base import KillChallenge
from ..unlocks import RespawnLegendaryUnlockable


class TerraKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Terramorphous Slain"
        self.unlockable = RespawnLegendaryUnlockable()
        self.required_enemy = "GD_Thresher_Raid.Character.CharClass_Thresher_Raid"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
