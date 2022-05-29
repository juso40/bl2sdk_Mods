from . import BaseScaler

import unrealsdk


class LootScaler(BaseScaler):
    
    def __init__(self):
        super().__init__()

    def register_hooks(self):
        def loot_scaler(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            if caller.AdditionalQueryInterfaceSource and "Player" in str(caller.AdditionalQueryInterfaceSource.Class):
                return True
            lvl = BaseScaler._get_player_level()
            caller.SetExpLevel(lvl)
            caller.SetGameStage(lvl)
            caller.DefinitionData.ManufacturerGradeIndex = lvl
            caller.DefinitionData.GameStage = lvl
            return True

        unrealsdk.RegisterHook(
            "Engine.WillowInventory.ClientInitializeInventoryFromDefinition",
            str(id(self)),
            loot_scaler
        )

    def remove_hooks(self):
        unrealsdk.RemoveHook("Engine.WillowInventory.ClientInitializeInventoryFromDefinition", str(id(self)))
