from typing import Optional

import unrealsdk  # type: ignore

from Mods.ModMenu import EnabledSaveType, Hook, RegisterMod, SDKMod


class Bossbar(SDKMod):
    Name: str = "Bossbar"
    Description: str = (
        "Adds a bossbar to minibosses and named enemies."
    )
    Author: str = "Juso"
    Version: str = "1.2"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    

    def __init__(self) -> None:
        super().__init__()
        self.boss_pawn: Optional[unrealsdk.UObject] = None
        self.bar_active: bool = False

    @Hook("Engine.Pawn.Destroyed")
    @Hook("WillowGame.WillowPawn.Died")
    def hk_pawn_died(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if caller == self.boss_pawn:
            self.boss_pawn = None
            gri = unrealsdk.GetEngine().GetCurrentWorldInfo().GRI
            gri.UpdateBossBarInfo()
            unrealsdk.DoInjectedCallNext()
            gri.InitBossBar(False, self.boss_pawn)
            self.bar_active = False
        return True

    @Hook("WillowGame.WillowPawn.TakeDamage")
    def hk_pawn_take_damage(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if BBInstance.boss_pawn is None and (caller.IsChampion() or caller.IsBoss()):
            if caller.IsEnemy(unrealsdk.GetEngine().GamePlayers[0].Actor.Pawn): # Not friendly NPCs (flamerock citizens get here)
                
                if not caller.GetParent():  # It seems that GetTargetName crashes the game if the AIPawn has a GetParent (Sheriff Posse Riders in Lynchwood)
                    if "Badass " in caller.GetTargetName():
                        return True
                    
                self.boss_pawn = caller
                gri: unrealsdk.UObject = unrealsdk.GetEngine().GetCurrentWorldInfo().GRI
                if gri:
                    unrealsdk.DoInjectedCallNext()
                    gri.InitBossBar(True, self.boss_pawn)
                    self.bar_active = True

        return True

    @Hook("WillowGame.WillowGameReplicationInfo.InitBossBar")
    def hk_init_bossbar(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        # Hooking into this also sets actual bosses so we don't overwrite them
        if params.bEnable:
            self.boss_pawn = params.BossActor
        else:
            self.boss_pawn = None
        return True

BBInstance = Bossbar()
RegisterMod(BBInstance)
