from unrealsdk import *


class CinematicKills(BL2MOD):
    Name = "Cinematic Kills"
    Version = "1.0"
    Author = "Juso"
    Description = "Slows time down for a short duration after last kill in current Combat." \
                  f"\n\nVersion: {Version}"

    def __init__(self):
        self.slowdown = 0.5

    def Enable(self):
        def combat_update(caller: UObject, function: UFunction, params: FStruct) -> bool:
            Log(f"Time since Last update: {caller.TimeSinceLastUpdate}")
            Log(f"bChangingState: {caller.bChangingState}")

        RegisterHook("WillowGame.CombatMusicManager.Update", "CMM_tick", combat_update)

    def Disable(self):
        RemoveHook("WillowGame.CombatMusicManager.Update", "CMM_tick")


RegisterMod(CinematicKills())
