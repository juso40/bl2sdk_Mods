import unrealsdk

import random


class DialogRando(unrealsdk.BL2MOD):
    Name = "Dialog Randomizer"
    Version = "1.0"
    Author = "Juso"
    Description = "Randomizes Dialogs." \
                  f"\n\nVersion: {Version}"

    def __init__(self):
        pass

    def Enable(self):
        def talk(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            dialog_acts = unrealsdk.FindAll("WillowDialogAct_Talk")[1:]
            for talk_event in caller.TalkData:
                try:
                    talk_event.TalkAkEvent = random.choice(
                        [x.TalkAkEvent for x in random.choice(dialog_acts).TalkData]
                    )
                except:
                    pass
            return True

        unrealsdk.RegisterHook("WillowGame.WillowDialogAct_Talk.Activate", "Talk", talk)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowDialogAct_Talk.Activate", "Talk")


unrealsdk.RegisterMod(DialogRando())
