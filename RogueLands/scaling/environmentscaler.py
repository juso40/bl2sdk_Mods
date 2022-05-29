from . import BaseScaler

import unrealsdk


class EnvironmentScaler(BaseScaler):

    def __init__(self):
        super().__init__()

    def register_hooks(self):
        def interactives_scaler(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            lvl = BaseScaler._get_player_level()
            unrealsdk.DoInjectedCallNext()
            caller.SetGameStage(lvl)
            return False

        def damage_scaler(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            lvl = BaseScaler._get_player_level()
            unrealsdk.DoInjectedCallNext()
            caller.SetGameStage(lvl)
            return True

        unrealsdk.RegisterHook("WillowGame.WillowInteractiveObject.SetGameStage", str(id(self)), interactives_scaler)
        unrealsdk.RegisterHook(
            "WillowGame.BehaviorVolume.InitializeAttributeStartingValues",
            str(id(self)),
            damage_scaler
        )

    def remove_hooks(self):
        unrealsdk.RemoveHook("WillowGame.WillowInteractiveObject.SetGameStage", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.BehaviorVolume.InitializeAttributeStartingValues", str(id(self)))
