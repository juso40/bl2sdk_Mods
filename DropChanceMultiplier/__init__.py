import unrealsdk
from unrealsdk import *


class DropChanceMultiplier(unrealsdk.BL2MOD):
    Name = "Drop Chance Multiplier"
    Description = "Runs multiple times the function that decides whether or not the Enemy should drop loot."
    Author = "Juso"

    def Enable(self):
        unrealsdk.RegisterHook("WillowGame.WillowPawn.DropLootOnDeath", "LootHook", Loot)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowPawn.DropLootOnDeath", "LootHook")


LootInstance = DropChanceMultiplier()


def Loot(caller: UObject, function: UFunction, params: FStruct) -> bool:
    for _ in range(5):
        unrealsdk.DoInjectedCallNext()
        caller.DropLootOnDeath(params.Killer, params.DamageType, params.DamageTypeDefinition)
    return True


unrealsdk.Mods.append(LootInstance)
