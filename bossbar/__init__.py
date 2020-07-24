import bl2sdk
from bl2sdk import *


class Bossbar(bl2sdk.BL2MOD):
    Name = "Bossbar"
    Description = "Bossbar"
    Author = "Juso"

    boss_pawn = None
    bar_active = False

    def HandleKill(self, caller, function, params):
        if caller == self.boss_pawn:
            self.boss_pawn = None
            GetEngine().GetCurrentWorldInfo().GRI.UpdateBossBarInfo()
            GetEngine().GetCurrentWorldInfo().GRI.InitBossBar(False, self.boss_pawn)
            self.bar_active = False
        return True

    def InitBar(self):
        if GetEngine().GetCurrentWorldInfo().GRI:
            GetEngine().GetCurrentWorldInfo().GRI.InitBossBar(True, self.boss_pawn)
            self.bar_active = True

    def Enable(self):
        bl2sdk.RegisterHook("WillowGame.WillowPawn.Died", "KillHook", KilledHook)
        bl2sdk.RegisterHook("WillowGame.WillowPawn.TakeDamage", "TakeDamageHook", PawnDamageHook)

    def Disable(self):
        bl2sdk.RemoveHook("WillowGame.WillowPawn.Died", "KillHook")
        bl2sdk.RemoveHook("WillowGame.WillowPawn.TakeDamage", "TakeDamageHook")


BBInstance = Bossbar()


def KilledHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    BBInstance.HandleKill(caller, function, params)
    return True


def PawnDamageHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    if BBInstance.boss_pawn is None:
        Log(caller.PathName(caller))
        if caller.IsChampion() or caller.IsBoss():
            BBInstance.boss_pawn = caller
            BBInstance.InitBar()
    # elif BBInstance.bar_active:
       #  GetEngine().GetCurrentWorldInfo().GRI.UpdateBossBarInfo()
    return True


bl2sdk.Mods.append(BBInstance)
