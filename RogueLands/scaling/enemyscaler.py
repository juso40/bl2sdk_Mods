from . import BaseScaler

import unrealsdk


class EnemyScaler(BaseScaler):

    def __init__(self):
        super().__init__()

    def register_hooks(self):
        def stage(
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

        def exp(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            if "WillowPlayerPawn" in str(caller.Class):
                return True
            lvl = BaseScaler._get_player_level()
            unrealsdk.DoInjectedCallNext()
            caller.SetExpLevel(lvl)
            return False

        unrealsdk.RegisterHook(
            "WillowGame.WillowPawn.SetGameStage",
            str(id(self)),
            lambda c, f, p: stage(c, f, p)
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowVehicle.SetGameStage",
            str(id(self)),
            lambda c, f, p: stage(c, f, p)
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPawn.SetExpLevel",
            str(id(self)),
            lambda c, f, p: exp(c, f, p)
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowVehicle.SetExpLevel",
            str(id(self)),
            lambda c, f, p: exp(c, f, p)
        )

    def remove_hooks(self):
        unrealsdk.RemoveHook("WillowGame.WillowPawn.SetGameStage", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.WillowVehicle.SetGameStage", str(id(self)))
