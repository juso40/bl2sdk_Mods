import re
from dataclasses import dataclass
from typing import List, Tuple

import unrealsdk

from Mods.ModMenu import EnabledSaveType, Hook, ModTypes, Options, RegisterMod, SDKMod
from Mods.coroutines import PostRenderCoroutine, Time, WaitWhile, start_coroutine_post_render

MaxMessages = Options.Slider(
    Caption="Max Messages",
    Description="Maximum number of messages to display at once.",
    StartingValue=5,
    MinValue=1,
    MaxValue=20,
    Increment=1
)

YOffset = Options.Slider(
    Caption="Y Offset",
    Description="How far down the screen the messages should be displayed in percent of the screen height.",
    StartingValue=5,
    MinValue=0,
    MaxValue=30,
    Increment=1
)

MessageSpacing = Options.Slider(
    Caption="MessageSpacing",
    Description="How far apart the messages should be displayed vertically in pixels.",
    StartingValue=14,
    MinValue=9,
    MaxValue=30,
    Increment=1
)

MessageDuration = Options.Slider(
    Caption="Message Duration",
    Description="How long the message should be displayed in seconds.",
    StartingValue=5,
    MinValue=1,
    MaxValue=30,
    Increment=1
)


@dataclass
class Message:
    title: str
    message: str
    message_color: Tuple[int, int, int, int]  # BGRA
    duration_remaining: float


MESSAGES: List[Message] = []


def hex_to_rgb(hex_color: str) -> tuple:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def coroutine_post_render() -> PostRenderCoroutine:
    while True:
        yield WaitWhile(lambda: unrealsdk.GetEngine().GamePlayers[0].Actor.IsPauseMenuOpen())
        canvas = yield
        screen_width = canvas.SizeX
        screen_height = canvas.SizeY
        start_y = int(screen_height * (YOffset.CurrentValue / 100))
        x_center = screen_width // 2
        for message in MESSAGES.copy():
            message.duration_remaining -= Time.delta_time
            if message.duration_remaining <= 0:
                MESSAGES.remove(message)
                continue

            full_message = f"{message.title} {message.message}"
            xl, yl = canvas.TextSize(full_message)
            title_start_x = x_center - xl // 2
            # draw the title in white
            canvas.SetPos(title_start_x, start_y)
            canvas.SetDrawColorStruct((255, 255, 255, 255))
            canvas.DrawText(message.title, False, 1, 1, ())
            # draw the message in the specified color
            xl, yl = canvas.TextSize(message.title)
            title_end_x = title_start_x + xl + 1
            canvas.SetPos(title_end_x, start_y)
            canvas.SetDrawColorStruct(message.message_color)
            canvas.DrawText(message.message, False, 1, 1, ())
            start_y += MessageSpacing.CurrentValue

            if not mod_instance.IsEnabled:
                return None


class PickupMessage(SDKMod):
    Name: str = "Pickup Message"
    Description: str = "Shows a message with the item you just picked up."
    Author: str = "Juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.1"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    Options = [MaxMessages, YOffset, MessageSpacing, MessageDuration]

    def Enable(self) -> None:
        super().Enable()
        start_coroutine_post_render(coroutine_post_render())

    @Hook("WillowGame.WillowHUD.DisplayCustomMessage")
    def display_custom_hud_message(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:

        message = params.MessageString
        # try to get the hex color from the optional <font> tag
        color = re.search(r"<font color = \"#(.*?)\">", message)
        if color:
            color = hex_to_rgb(color.group(1))
            color = (color[2], color[1], color[0], 255)
        else:
            color = (255, 255, 255, 255)

        # Title is everything before the <font> tag
        # Message is everything between the <font> </font> tags
        title = message[:message.find("<font")]
        message_match = re.search(r"<font color = \"#(.*?)\">(.*?)</font>", message)
        if message_match:
            message = message_match.group(2).replace("INVALID", "")
        else:
            message = ""
        MESSAGES.append(
            Message(title, message, color, MessageDuration.CurrentValue)
        )
        if len(MESSAGES) > MaxMessages.CurrentValue:
            MESSAGES.pop(0)

        return True


mod_instance = PickupMessage()
RegisterMod(mod_instance)
