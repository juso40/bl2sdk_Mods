from . import BaseUnlockable

import unrealsdk


class IncreasedXPUnlockable(BaseUnlockable):
    def __init__(self) -> None:
        super(IncreasedXPUnlockable, self).__init__("+150% XP Gain")
        self.xp_multiplier = 2.5

    def unlock(self) -> None:
        def xp_gain(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            unrealsdk.DoInjectedCallNext()

            caller.ExpEarn(int(params.Exp * self.xp_multiplier), params.Source, params.ExpType)

            return False

        def combat_xp_gain(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            unrealsdk.DoInjectedCallNext()
            caller.AwardCombatExperience(
                params.KillerWPC,
                params.KilledActor,
                params.TotalExpPoints * self.xp_multiplier
            )
            return False

        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ExpEarn", str(id(self)), xp_gain)
        unrealsdk.RegisterHook("WillowGame.WillowGameInfo.AwardCombatExperience", str(id(self)), combat_xp_gain)

    def lock(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ExpEarn", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.WillowGameInfo.AwardCombatExperience", str(id(self)))
