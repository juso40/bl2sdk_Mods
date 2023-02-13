import unrealsdk

from Mods.ModMenu import EnabledSaveType, Game, ModTypes, OptionManager, RegisterMod, SDKMod
from Mods.coroutines import PostRenderCoroutine, WaitWhile, start_coroutine_post_render
from Mods.uemath import Vector

PosX = OptionManager.Options.Slider(
    "Position X",
    "The x position of the speedometer in percentage of the screen width.",
    95, 5, 100, 1
)
PosY = OptionManager.Options.Slider(
    "Position Y",
    "The y position of the speedometer in percentage of the screen height.",
    15, 0, 90, 1
)
FreedomUnits = OptionManager.Options.Boolean(
    "Freedom Units",
    "Use Freedom Units instead of km/h.",
    False
)
RawVector = OptionManager.Options.Boolean(
    "Show Vector",
    "Show the velocity vector, instead of only the speed",
    False
)


def wait_condition() -> bool:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    return pc.Pawn is None or pc.IsPauseMenuOpen() or pc.bStatusMenuOpen


Font_18pt_JPN = unrealsdk.FindObject("Font", "UI_Fonts.Font_Willowbody_18pt_JPN")
Font_Tiny = unrealsdk.FindObject("Font", "EngineFonts.TinyFont")
FontRenderInfo = (False, True, ())


def draw_speedometer() -> PostRenderCoroutine:
    while True:
        yield WaitWhile(wait_condition)
        canvas = yield
        width = canvas.SizeX
        height = canvas.SizeY
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        velocity = Vector(pc.Pawn.Velocity)
        speed = velocity.magnitude
        # 1 unit = 1 cm ?
        speed_m = speed / 100
        speed_kmh = speed_m * 3.6
        if FreedomUnits.CurrentValue:
            speed_kmh *= 0.621371
        speed_txt = f"{speed_kmh:.2f}"

        font_backup = canvas.Font
        canvas.Font = Font_18pt_JPN
        speed_txt_x, speed_txt_y = canvas.TextSize(speed_txt)
        x_pos = int(width * (PosX.CurrentValue / 100))
        y_pos = int(height * (PosY.CurrentValue / 100))
        canvas.SetPos(x_pos - speed_txt_x, y_pos)  # - speed_txt_x to align the text to the right
        canvas.SetDrawColorStruct((0, 255, 0, 255))
        canvas.DrawText(speed_txt, False, 1, 1, FontRenderInfo)

        canvas.Font = Font_Tiny
        metric = "mph" if FreedomUnits.CurrentValue else "km/h"
        metric_x, metric_y = canvas.TextSize(metric)
        canvas.SetPos(x_pos - metric_x, y_pos + speed_txt_y)
        canvas.SetDrawColorStruct((150, 150, 150, 255))
        canvas.DrawText(metric, False, 1, 1, FontRenderInfo)

        if RawVector.CurrentValue:
            velocity_txt = f"Velocity: {velocity.x:.0f} {velocity.y:.0f} {velocity.z:.0f}"
            velocity_txt_x, velocity_txt_y = canvas.TextSize(velocity_txt)
            canvas.SetPos(x_pos - velocity_txt_x, y_pos + speed_txt_y + metric_y)
            canvas.SetDrawColorStruct((180, 180, 180, 255))
            canvas.DrawText(velocity_txt, False, 1, 1, FontRenderInfo)

        canvas.Font = font_backup
        if not mod_instance.IsEnabled:
            break


class Speedometer(SDKMod):
    Name: str = "Speedometer"
    Description: str = "Show the current speed of the player."
    Author: str = "juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.0"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    SupportedGames: Game = Game.BL2 | Game.TPS | Game.AoDK
    Options = [PosX, PosY, FreedomUnits, RawVector]

    def Enable(self) -> None:
        start_coroutine_post_render(draw_speedometer())


mod_instance = Speedometer()
RegisterMod(mod_instance)
