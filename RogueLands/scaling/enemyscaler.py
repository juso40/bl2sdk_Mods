from . import BaseScaler

import unrealsdk


class EnemyScaler(BaseScaler):

    def __init__(self):
        super().__init__()

    def register_hooks(self):
        def enemy_scaler(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            if "WillowPlayerPawn" in str(caller.Class):
                return True
            lvl = BaseScaler._get_player_level()
            unrealsdk.DoInjectedCallNext()
            caller.SetGameStage(lvl)
            return False

        unrealsdk.RegisterHook(
            "WillowGame.WillowPawn.SetGameStage",
            str(id(self)),
            enemy_scaler
        )

    def remove_hooks(self):
        unrealsdk.RemoveHook("WillowGame.WillowPawn.SetGameStage", str(id(self)))
