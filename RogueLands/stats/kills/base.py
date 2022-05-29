from ..stat import Stat

import unrealsdk


class KillStat(Stat):
    def __init__(self) -> None:
        self.name = ""
        self.value = 0
        self.total_value = 0

        self.outer_dict_key = "KillStats"

    def enemy_killed(self, target_pawn: unrealsdk.UObject) -> None:
        return

    def register_hooks(self) -> None:
        def on_kill(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if caller.Controller.IsLocalPlayerController():
                self.enemy_killed(params.aTargetPawn)
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerPawn.KilledEnemy", str(id(self)), on_kill)

    def remove_hooks(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerPawn.KilledEnemy", str(id(self)))

    def load_stat(self, save_dict: dict) -> None:
        stats = save_dict.get(self.outer_dict_key, {}).get(self.name, {})
        self.value = stats.get("Value", 0)
        self.total_value = stats.get("TotalValue", 0)

    def save_stat(self, save_dict: dict) -> None:
        save_dict[self.outer_dict_key] = save_dict.get(self.outer_dict_key, {})
