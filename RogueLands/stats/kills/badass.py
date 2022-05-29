from .base import KillStat

import unrealsdk


class BadassKillStat(KillStat):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Badass Kills"

    def enemy_killed(self, target_pawn: unrealsdk.UObject) -> None:
        if target_pawn.IsChampion():
            self.value += 1
            self.total_value += 1

    def load_stat(self, save_dict: dict) -> None:
        super().load_stat(save_dict)

    def save_stat(self, save_dict: dict) -> None:
        super().save_stat(save_dict)
        save_dict[self.outer_dict_key][self.name] = {"Value": self.value, "TotalValue": self.total_value}
