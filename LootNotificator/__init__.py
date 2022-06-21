import unrealsdk
from ..ModMenu import EnabledSaveType, ModTypes, OptionManager, SDKMod, Hook, RegisterMod

import os
import json


class Lootbeams(SDKMod):
    Name: str = "Loot Notificator"
    Version: str = "2.1"
    Description: str = "Adds Special Particles to all Red Text gear dropped. Also plays a sound. " \
                       "Configure which modpack you are running in the Mod Options."
    Author: str = "Juso and SilverBeam"
    Types: ModTypes = ModTypes.Utility
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    def __init__(self):
        super(Lootbeams, self).__init__()

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "rarities.json"), "r") as f:
            self.Rarities = json.load(f)

        self.Particles = [
            "FX_ENV_Misc.Particles.Part_Confetti",  # Lowest
            "FX_Aster_Knight.Particles.Paladin.Part_DivineShard_HitImpact",
            "FX_Aster_Knight.Particles.Paladin.Part_PillarOfSmite",  # Middle Rarity
            "FX_Aster_Knight.Particles.Paladin.Part_DivineFavor",  # High Rarity
            "FX_Aster_Knight.Particles.Paladin.Part_ConcecrateGround",  # Highest Rarity
            "FX_Aster_ButtStallion.Particles.Part_ButtStallionSavesTheWorld"  # Rainbow Rarity
        ]

        self.EventSounds = [
            "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward",
            "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"
        ]

        self.ModPackSpinner = OptionManager.Options.Spinner(
            Caption="Mod Pack",
            Description="Select which modpack you are running.",
            StartingValue="Exodus",
            Choices=list(self.Rarities.keys())
        )
        self.Options = [
            self.ModPackSpinner
        ]

    # This is how we know that we're in the main menu.
    # We run the hook on the first tick of the main menu, then we unhook.
    # This is needed due to the fact that not all packages are available to load until the MainMenu has loaded.
    @Hook("WillowGame.FrontendGFxMovie.OnTick", "ForceLoadParticles")
    def ForceLoad(self, caller, function, params):
        unrealsdk.LoadPackage("SanctuaryAir_Dynamic")
        unrealsdk.LoadPackage("CastleKeep_FX")
        unrealsdk.LoadPackage("CastleKeep_Combat")
        unrealsdk.LoadPackage("CastleKeep_Mission")
        for Particle in self.Particles:
            temp = unrealsdk.FindObject("ParticleSystem", Particle)
            unrealsdk.KeepAlive(temp)
        unrealsdk.RemoveHook("WillowGame.FrontendGFxMovie.OnTick", "ForceLoadParticles")

    def GetParticle(self, index):
        return unrealsdk.FindObject("ParticleSystem", self.Particles[index])

    def GetSound(self, index):
        return unrealsdk.FindObject("AkEvent", self.EventSounds[index])

    @Hook("WillowGame.WillowPickup.ConvertRigidBodyToFixed")
    def HandleLootBeams(self, caller, function, params):
        # We search for the EmitterPool to spawn our particles from, also we need a location.
        EmitterSpawner = unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool
        Location = (caller.Location.X, caller.Location.Y, caller.Location.Z)
        Rotation = (caller.Rotation.Pitch, caller.Rotation.Yaw, caller.Rotation.Roll)
        # If the RBState Position is 0 it means it's not on the ground
        if caller.RBState.Position.X != 0:
            for rarity in self.Rarities[self.ModPackSpinner.CurrentValue]:
                if caller.InventoryRarityLevel in range(rarity["min_level"], rarity["max_level"] + 1):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(rarity["particle"]), Location, Rotation)
                    caller.PlayAkEvent(self.GetSound(rarity["sound"]))
                    break

    def Enable(self):
        super().Enable()

    def Disable(self):
        super().Disable()


RegisterMod(Lootbeams())
