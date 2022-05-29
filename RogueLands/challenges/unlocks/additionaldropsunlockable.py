from . import BaseUnlockable

import unrealsdk


class AdditionalDropsUnlockable(BaseUnlockable):

    def __init__(self) -> None:
        super(AdditionalDropsUnlockable, self).__init__("+1 Loot Roll on Kill")

    def unlock(self) -> None:
        def drop_loot(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            caller.DropLootOnDeath(params.Killer, params.DamageType, params.DamageTypeDefinition)
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPawn.DropLootOnDeath", str(id(self)), drop_loot)

    def lock(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPawn.DropLootOnDeath", str(id(self)))
