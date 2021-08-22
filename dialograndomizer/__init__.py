import random
from typing import List

import unrealsdk

from ..ModMenu import EnabledSaveType, Hook, SDKMod


class DialogRando(SDKMod):
    Name = "Dialog Randomizer"
    Version = "2.1"
    Author = "Juso"
    Description = "Randomizes Dialogs."
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu

    def __init__(self):
        self.ak_events: List[unrealsdk.UObject] = []

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def map_loaded(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        if pc and pc.Pawn:
            self.ak_events = [ak for ak in unrealsdk.FindAll("AkEvent")[1:] if ak.bVoice]
        return True

    @Hook("WillowGame.WillowDialogAct_Talk.Activate")
    def talk(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        for talk_event in caller.TalkData:
            talk_event.TalkAkEvent = random.choice(self.ak_events)

        return True

    @Hook("GearboxFramework.Behavior_TriggerDialogEvent.ApplyBehaviorToContext")
    def event(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        if caller.Group:
            for acts in caller.Group.TalkActs:
                try:
                    for data in acts.TalkData:
                        data.TalkAkEvent = random.choice(self.ak_events)
                except:
                    pass
        return True


unrealsdk.RegisterMod(DialogRando())
