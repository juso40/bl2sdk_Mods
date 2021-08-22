import unrealsdk
from ..ModMenu import EnabledSaveType, Hook, SDKMod, OptionManager, RegisterMod


class DropChanceMultiplier(SDKMod):
    Name = "Drop Chance Multiplier"
    Description = "Runs multiple times the function that decides whether or not the Enemy should drop loot."
    Author = "Juso"
    Version = "2.0"
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu

    def __init__(self):
        self.multiplier_option = OptionManager.Options.Slider(
            "Drop Multiplier", "How often should loot be dropped from the same Lootpool.", 1, 0, 100, 1
        )
        self.Options = [self.multiplier_option]

    @Hook("WillowGame.WillowPawn.DropLootOnDeath")
    def Loot(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        for _ in range(self.multiplier_option.CurrentValue):
            caller.DropLootOnDeath(params.Killer, params.DamageType, params.DamageTypeDefinition)
        return True


RegisterMod(DropChanceMultiplier())
