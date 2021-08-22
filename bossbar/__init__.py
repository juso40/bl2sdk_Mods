import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod


class Bossbar(SDKMod):
    Name: str = "Bossbar"
    Description: str = "Adds a bossbar to minibosses and named enemies, for example Saturn."
    Author: str = "Juso"
    Version: str = "1.1"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu

    boss_pawn = None
    bar_active = False

    def HandleKill(self, caller, function, params):
        if caller == self.boss_pawn:
            self.boss_pawn = None
            gri = unrealsdk.GetEngine().GetCurrentWorldInfo().GRI
            gri.UpdateBossBarInfo()
            gri.InitBossBar(False, self.boss_pawn)
            self.bar_active = False
        return True

    def InitBar(self):
        gri = unrealsdk.GetEngine().GetCurrentWorldInfo().GRI
        if gri:
            gri.InitBossBar(True, self.boss_pawn)
            self.bar_active = True

    def Enable(self):
        unrealsdk.RegisterHook("WillowGame.WillowPawn.Died", "KillHook", KilledHook)
        unrealsdk.RegisterHook("WillowGame.WillowPawn.TakeDamage", "TakeDamageHook", PawnDamageHook)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowPawn.Died", "KillHook")
        unrealsdk.RemoveHook("WillowGame.WillowPawn.TakeDamage", "TakeDamageHook")


BBInstance = Bossbar()


def KilledHook(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    BBInstance.HandleKill(caller, function, params)
    return True


def PawnDamageHook(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    if BBInstance.boss_pawn is None:
        if caller.IsChampion() or caller.IsBoss():
            BBInstance.boss_pawn = caller
            BBInstance.InitBar()
    # elif BBInstance.bar_active:
    #  GetEngine().GetCurrentWorldInfo().GRI.UpdateBossBarInfo()
    return True


unrealsdk.RegisterMod(BBInstance)
