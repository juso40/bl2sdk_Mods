import bl2sdk

class Lootbeams(bl2sdk.BL2MOD):
    Name = "Loot Notificator"
    Description = "Adds Special Particles to all Red Text gear. Also plays a sound. src and Reborn."
    Author = "Juso"
    SettingsInputs = {"Enter": "src"}
    _Exodus = False
    _Reborn = False
    def SettingsInputPressed(self, name):
        if name == "src":
            self.Status = "src"
            self.SettingsInputs = { 'Enter': "Reborn" }
            self._Exodus = True
            self._Reborn = False
            self.Enable()
        elif name == "Reborn":
            self.Status = "Reborn"
            self.SettingsInputs = { 'Enter': "Disable" }
            self._Exodus = False
            self._Reborn = True
            self.Enable()
        elif name == "Disable":
            self.Status = "Disabled"
            self.SettingsInputs = { 'Enter': "src" }
            self.Enable()
       
    Particles = [
                'FX_ENV_Misc.Particles.Part_Confetti',#Lowest
                'FX_Aster_Knight.Particles.Paladin.Part_DivineShard_HitImpact', 
                'FX_Aster_Knight.Particles.Paladin.Part_PillarOfSmite', #Middle Rarity          
                'FX_Aster_Knight.Particles.Paladin.Part_DivineFavor',  #High Rarity
                'FX_Aster_Knight.Particles.Paladin.Part_ConcecrateGround', #Highest Rarity     
                'FX_Aster_ButtStallion.Particles.Part_ButtStallionSavesTheWorld' #Rainbow Rarity
                ]       
    
    def ForceLoad(self):
        bl2sdk.LoadPackage("SanctuaryAir_Dynamic")
        bl2sdk.LoadPackage("CastleKeep_FX")
        bl2sdk.LoadPackage("CastleKeep_Combat")
        bl2sdk.LoadPackage("CastleKeep_Mission")
        for Particle in self.Particles:
            temp = bl2sdk.FindObject("ParticleSystem", Particle)
            bl2sdk.KeepAlive(temp)

    def GetParticle(self, index): 
        temp = bl2sdk.FindObject("ParticleSystem", self.Particles[index])
        print(temp)
        return temp

    def HandleLootBeams(self, caller, function, params):
        #We search for the EmitterPool to spawn our particles from, also we need a location.
        EmitterSpawner = bl2sdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool
        Location = (caller.Location.X, caller.Location.Y, caller.Location.Z)
        Rotation = (caller.Rotation.Pitch, caller.Rotation.Yaw, caller.Rotation.Roll)
        #If the RBState Position is 0 it means its not on the ground
        if caller.RBState.Position.X != 0:
            if self._Exodus == True:
                #These are the RarityLevels of src
                #RareUnique
                if caller.InventoryRarityLevel in range(11, 21):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(0), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward"))
                #Seraph
                elif caller.InventoryRarityLevel in range(61, 71):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(1), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward"))
                 #Fabled/Vile
                elif caller.InventoryRarityLevel in range(71, 86):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(2), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward"))
                 #Legendary/Malevolent
                elif caller.InventoryRarityLevel in range(86, 101):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(3), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))
                #Pearlescent/Augment
                elif caller.InventoryRarityLevel in range(101, 151) or caller.InventoryRarityLevel == 500:
                    EmitterSpawner.SpawnEmitter(self.GetParticle(4), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))
                #Rainbow
                elif caller.InventoryRarityLevel in range(551, 551):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(5), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))

            elif self._Reborn == True:
                #These are the RarityLevels of Reborn
                #Legendary and Unique Legendary
                if caller.InventoryRarityLevel in range(5, 11) or caller.InventoryRarityLevel in range(61, 81):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(2), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))
                #Unique Blue
                elif caller.InventoryRarityLevel in range(41, 51):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(1), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward"))
                 #Moxxi
                elif caller.InventoryRarityLevel in range(51, 61):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(0), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward"))
                 #Seraph
                elif caller.InventoryRarityLevel in range(81, 91):
                    EmitterSpawner.SpawnEmitter(self.GetParticle(3), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))
                #Pearl
                elif caller.InventoryRarityLevel in range(91, 171) or caller.InventoryRarityLevel == 500:
                    EmitterSpawner.SpawnEmitter(self.GetParticle(4), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))
                #Rainbow
                elif caller.InventoryRarityLevel == 506:
                    EmitterSpawner.SpawnEmitter(self.GetParticle(5), Location, Rotation)
                    caller.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Chapter_Stinger"))

    def Enable(self):
        self.ForceLoad()
        bl2sdk.RegisterHook("WillowGame.WillowPickup.ConvertRigidBodyToFixed", "LootBeamHook", BeamHook)
    def Disable(self):
        bl2sdk.RemoveHook("WillowGame.WillowPickup.ConvertRigidBodyToFixed", "LootBeamHook")

LootbeamInstance = Lootbeams()

def BeamHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    LootbeamInstance.HandleLootBeams(caller, function, params)
    return True

bl2sdk.Mods.append(LootbeamInstance)