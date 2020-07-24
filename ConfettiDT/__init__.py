import bl2sdk


class Confetti(bl2sdk.BL2MOD):

    Name = "Confetti DT"
    Description = "Replaces Death-Trap with a handful of confetti. Idea by ilovecheese2"
    Author = "Juso"
  
    def Load(self):
        bl2sdk.LoadPackage("SanctuaryAir_Dynamic")
        bl2sdk.KeepAlive(bl2sdk.FindObject("ParticleSystem", "FX_ENV_Misc.Particles.Part_Confetti"))
        bl2sdk.KeepAlive(bl2sdk.FindObject("AkEvent", "Ake_Seq_Missions.SQ.Ak_Play_SQ_ClaptrapParty_hornBlow"))

    def PlaySMD(self, caller, function, params):
        BPD = caller.BehaviorProviderDefinition
        BPD.BehaviorSequences[0].BehaviorData2[7].Behavior.SpawnFactory = None
        EmitterPool = bl2sdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool
        Arms = bl2sdk.GetEngine().GamePlayers[0].Actor.Pawn.Arms
        EmitterPool.SpawnEmitterMeshAttachment(bl2sdk.FindObject("ParticleSystem", "FX_ENV_Misc.Particles.Part_Confetti"), Arms, "L_Forearm")
        bl2sdk.GetEngine().GamePlayers[0].Actor.Pawn.PlayAkEvent(bl2sdk.FindObject("AkEvent", "Ake_Seq_Missions.SQ.Ak_Play_SQ_ClaptrapParty_hornBlow"))

    def Enable(self):
        self.Load()
        bl2sdk.RegisterHook("WillowGame.DeathtrapActionSkill.OnActionSkillStarted", "DTHook", NoDT)

    def Disable(self):
        bl2sdk.RemoveHook("WillowGame.DeathtrapActionSkill.OnActionSkillStarted", "DTHook")


ConfettiInstance = Confetti()

def NoDT(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    ConfettiInstance.PlaySMD(caller, function, params)
    return True

bl2sdk.Mods.append(ConfettiInstance)
