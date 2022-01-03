import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, RegisterMod, Hook, ModTypes


class PickupMessage(SDKMod):
    Name: str = "Pickup Message"
    Description: str = "Shows a message with the item you just picked up."
    Author: str = "Juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.0"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu

    @Hook("WillowGame.WillowHUD.DisplayCustomMessage")
    def display_custom_hud_message(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if "</font>" not in params.MessageString:
            return True

        HUD = caller.GetHUDMovie()
        if HUD:
            if params.MsgType == 0:
                message: str = params.MessageString
                title = message[:message.find("<font")]
                message = message[message.find("<font"):].replace("INVALID", "")
                HUD.AddTrainingText(message, title, params.Duration, (), "", False, 0.0, params.RelatedPRI_1, True)
                return False
        return True

    @Hook("WillowGame.WillowPlayerController.DisplayHUDMessage")
    def handle_pickup(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        # Picked Up Loot Message Type
        if params.MsgType != 0:
            caller.DisplayHUDMessage(
                0,
                params.MessageString,
                params.Duration,
                (255, 255, 255, 255),
                params.InMessageClass,
                params.Switch,
                params.RelatedPRI_1,
                params.OptionalObject
            )
            return False
        return True


RegisterMod(PickupMessage())
