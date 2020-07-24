import bl2sdk

class CritOnly(bl2sdk.BL2MOD):
    Name = "Crits Only"
    Description = "Only crits deal damage.\nEnemies that do not have a crit spot still can normally be damaged.\nWritten by Juso"

    def HandleDamage(self, caller, function, params):
        #check if the damaged target actually has a crit spot
        if any(str(tmp.bCriticalHit)=="True" for tmp in caller.BodyClass.HitRegionList):
            #let the game decide where we hit the target
            HitInfo = (params.HitInfo.Material, params.HitInfo.PhysMaterial, params.HitInfo.Item, params.HitInfo.LevelIndex, params.HitInfo.BoneName, params.HitInfo.HitComponent)
            BodyHitRegionDefinition = caller.GetHitRegionForTakenDamage(params.InstigatedBy, HitInfo)
            #if the hit bodyregion is a crit spot return true -> deal damage
            if str(BodyHitRegionDefinition.bCriticalHit) == "True":
                return True
            else:
                return False
        #If the damaged enemy doesent have any critspots, then deal damage
        return True

    def Enable(self):
        bl2sdk.RegisterHook("WillowGame.WillowPawn.TakeDamage", "TakeDamageHook", DamageHook)
    def Disable(self):
        bl2sdk.RemoveHook("WillowGame.WillowPawn.TakeDamage", "TakeDamageHook")

CritOnlyInstance = CritOnly()


def DamageHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
	return CritOnlyInstance.HandleDamage(caller, function, params)

bl2sdk.Mods.append(CritOnlyInstance)


