import bl2sdk

class Hitsounds(bl2sdk.BL2MOD):
    Name = "Hitsounds"
    Description = "Plays a Hitsound on damaging an enemy."
    Author = "Juso"

    def SettingsInputPressed(self, name):
        if name == "Enable":
            self.Status = "Enabled"
            self.SettingsInputs = { 'Enter': "Enabled with Particles" }
            self.Enable()
        elif name == "Disable":
            self.Status = "Disabled"
            self.SettingsInputs = { 'Enter': "Enable" }
            self.Disable()
        elif name == "Enabled with Particles":
            self.Status = "Enabled+Particles"
            self.SettingsInputs = { 'Enter': "Disable" }
            self.Enable()

    #Loads the Package requierd for the Particle once
    def ForceLoad(self):
        bl2sdk.LoadPackage("SanctuaryAir_Dynamic")
        temp = bl2sdk.FindObject("ParticleSystem", "FX_ENV_Misc.Particles.Part_Confetti")
        bl2sdk.KeepAlive(temp)

    def GetParticle(self):
        return bl2sdk.FindObject("ParticleSystem", "FX_ENV_Misc.Particles.Part_Confetti")

    def AddParticle(self, params):
        #First we need the EmitterPool
        EmitterSpawner = bl2sdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool
        #We get the location and rotation from the parameters of our hook
        Location = (params.DamageEventData.DamageLocation.X, params.DamageEventData.DamageLocation.Y, params.DamageEventData.DamageLocation.Z)
        Rotation = (params.PC.Rotation.Pitch, params.PC.Rotation.Yaw, params.PC.Rotation.Roll)
        #Now we actually call the games function that emitts the particles
        EmitterSpawner.SpawnEmitter(self.GetParticle(), Location, Rotation);

    
    def PlaySound(self, PlayerController):
        AkEvent = bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Generic.Ak_Play_UI_Generic_InGame_Select")
        PlayerController.PlayAkEvent(AkEvent)
    
    def PlayCritSound(self, PlayerController):
		#AkEvent = bl2sdk.FindObject("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_Alert_CoOp_Ding")
        AkEvent = bl2sdk.FindObject("AkEvent", "Ake_UI.UI_Generic.Ak_Play_UI_Generic_InGame_Close")
        PlayerController.PlayAkEvent(AkEvent)

    def HandleDamage(self, caller, function, params):
        #We only want to play a sound if we were the ones who actually dealt the damage
        if params.PC == bl2sdk.GetEngine().GamePlayers[0].Actor:
            #DamageEventFlags = 1 -> Crit therefore if its not equal to 1 then it wasnt a crit
            if params.DamageEventData.DamageEventFlags != 1:
                self.PlaySound(params.PC)
            else:
                self.PlayCritSound(params.PC)
                if self.Status == "Enabled+Particles":
                    self.AddParticle(params)

    def Enable(self):
        self.ForceLoad()
        bl2sdk.RegisterHook("WillowGame.WillowDamageTypeDefinition.DisplayRecentDamageForPlayer", "DamageHook", HandleDamageHook)
    def Disable(self):
        bl2sdk.RemoveHook("WillowGame.WillowDamageTypeDefinition.DisplayRecentDamageForPlayer", "DamageHook")


HitsoundsInstance = Hitsounds()

#The "return True" means that after our hook the original function will still play
def HandleDamageHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
	HitsoundsInstance.HandleDamage(caller, function, params)
	return True

bl2sdk.Mods.append(HitsoundsInstance)


