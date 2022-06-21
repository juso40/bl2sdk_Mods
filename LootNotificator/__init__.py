import bl2sdk
import unrealsdk
from Mods import ModMenu
from Mods.ModMenu import EnabledSaveType, Mods, ModTypes, Options,  OptionManager, RegisterMod, SDKMod, Hook

import os
import json

class Lootbeams(SDKMod):
    Name: str = "Loot Notificator"
    Version: str = "2.0"
    Description: str = "Adds Special Particles to all Red Text gear dropped. Also plays a sound. " \
                       "Configure which modpack you are running in the Mod Options."
    Author: str = "Juso and SilverBeam"
    Types: ModTypes = ModTypes.Utility
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    def __init__(self):
        super(Lootbeams, self).__init__()

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "rarities.json"), "r") as f:
            self.Rarities = json.load(f)

        self.SelectedModpack = "Exodus"

        self.Particles = [
            'FX_ENV_Misc.Particles.Part_Confetti',#Lowest
            'FX_Aster_Knight.Particles.Paladin.Part_DivineShard_HitImpact', 
            'FX_Aster_Knight.Particles.Paladin.Part_PillarOfSmite', #Middle Rarity          
            'FX_Aster_Knight.Particles.Paladin.Part_DivineFavor',  #High Rarity
            'FX_Aster_Knight.Particles.Paladin.Part_ConcecrateGround', #Highest Rarity     
            'FX_Aster_ButtStallion.Particles.Part_ButtStallionSavesTheWorld' #Rainbow Rarity
        ]

        self.EventSounds = [
            'Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward',
            'Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger'
        ]

        self.Options = [
            OptionManager.Options.Spinner(
                "Mod Pack",
                f"Select which modpack you are running.",
                StartingValue="Exodus",
                Choices=list(self.Rarities.keys())
            )
        ]

    def ModOptionChanged(self, option, new_value):
        if option.Caption == "Mod Pack":
            self.SelectedModpack = new_value   
           
    # This is how we know that we're in the main menu. We run the hook on the first tick of the main menu, then we unhook.
    # This is needed due to the fact that not all packages are available to load until the MainMenu has loaded.
    @Hook("WillowGame.FrontendGFxMovie.OnTick","ForceLoadParticles")
    def ForceLoad(self, caller, function, params):
        bl2sdk.LoadPackage("SanctuaryAir_Dynamic")
        bl2sdk.LoadPackage("CastleKeep_FX")
        bl2sdk.LoadPackage("CastleKeep_Combat")
        bl2sdk.LoadPackage("CastleKeep_Mission")
        for Particle in self.Particles:
            temp = bl2sdk.FindObject("ParticleSystem", Particle)
            bl2sdk.KeepAlive(temp)
        unrealsdk.RemoveHook("WillowGame.FrontendGFxMovie.OnTick","ForceLoadParticles")

    def GetParticle(self, index): 
        return bl2sdk.FindObject("ParticleSystem", self.Particles[index])

    def GetSound(self,index):
        return bl2sdk.FindObject("AkEvent", self.EventSounds[index])

    @Hook("WillowGame.WillowPickup.ConvertRigidBodyToFixed")
    def HandleLootBeams(self, caller, function, params):
        #We search for the EmitterPool to spawn our particles from, also we need a location.
        EmitterSpawner = bl2sdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool
        Location = (caller.Location.X, caller.Location.Y, caller.Location.Z)
        Rotation = (caller.Rotation.Pitch, caller.Rotation.Yaw, caller.Rotation.Roll)
        #If the RBState Position is 0 it means its not on the ground
        if caller.RBState.Position.X != 0:
            for rarity in self.Rarities[self.SelectedModpack]:
                if caller.InventoryRarityLevel in range(rarity["min_level"], rarity["max_level"] + 1):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(rarity["particle"]), Location, Rotation)
                    caller.PlayAkEvent(self.GetSound(rarity["sound"]))
                    break

    def Enable(self):
        super().Enable()
    def Disable(self):
        super().Disable()


unrealsdk.RegisterMod(Lootbeams())