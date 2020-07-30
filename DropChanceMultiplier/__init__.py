import unrealsdk
from unrealsdk import *
from ..OptionManager import Options


class DropChanceMultiplier(unrealsdk.BL2MOD):
    Name = "Drop Chance Multiplier"
    Description = "Runs multiple times the function that decides whether or not the Enemy should drop loot."
    Author = "Juso"

    Options = [
        Options.Slider("Drop Multiplier", "How often should loot be dropped from the same Lootpool.", 1, 0, 100, 1),
    ]

    def __init__(self):
        self.multiplier = 0

    def Enable(self):
        def Loot(caller: UObject, function: UFunction, params: FStruct) -> bool:
            for _ in range(self.multiplier):
                unrealsdk.DoInjectedCallNext()
                caller.DropLootOnDeath(params.Killer, params.DamageType, params.DamageTypeDefinition)
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPawn.DropLootOnDeath", "LootHook", Loot)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowPawn.DropLootOnDeath", "LootHook")

    def ModOptionChanged(self, option, newValue):
        if option in self.Options:
            if option.Caption == "Drop Multiplier":
                self.multiplier = newValue


unrealsdk.RegisterMod(DropChanceMultiplier())
