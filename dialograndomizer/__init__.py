import random
from typing import List

import unrealsdk


class DialogRando(unrealsdk.BL2MOD):
    Name = "Dialog Randomizer"
    Version = "2.0"
    Author = "Juso"
    Description = "Randomizes Dialogs." \
                  f"\n\nVersion: {Version}"

    def __init__(self):
        self.ak_events: List[unrealsdk.UObject] = []

    def Enable(self):
        def map_loaded(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            pc = unrealsdk.GetEngine().GamePlayers[0].Actor
            if pc and pc.Pawn:
                self.ak_events = [ak for ak in unrealsdk.FindAll("AkEvent")[1:] if ak.bVoice]
            return True

        def talk(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            for talk_event in caller.TalkData:
                talk_event.TalkAkEvent = random.choice(self.ak_events)

            return True

        def event(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if caller.Group:
                for acts in caller.Group.TalkActs:
                    try:
                        for data in acts.TalkData:
                            data.TalkAkEvent = random.choice(self.ak_events)
                    except:
                        pass
            return True

        unrealsdk.RegisterHook("WillowGame.WillowDialogAct_Talk.Activate", f"{__file__}Talk", talk)
        unrealsdk.RegisterHook("GearboxFramework.Behavior_TriggerDialogEvent.ApplyBehaviorToContext",
                               f"{__file__}Event", event)
        unrealsdk.RegisterHook("WillowGame.WillowHUD.CreateWeaponScopeMovie", f"{__file__}TalkMapLoaded", map_loaded)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowDialogAct_Talk.Activate", f"{__file__}Talk")
        unrealsdk.RemoveHook("GearboxFramework.Behavior_TriggerDialogEvent.ApplyBehaviorToContext", f"{__file__}Event")
        unrealsdk.RemoveHook("WillowGame.WillowHUD.CreateWeaponScopeMovie", f"{__file__}TalkMapLoaded")


unrealsdk.RegisterMod(DialogRando())
