import unrealsdk

from Mods.ModMenu import EnabledSaveType, Game, ModTypes, OptionManager, RegisterMod, SDKMod
from Mods.canvaslib import Canvas, DepthFieldGlowInfo, FontRenderInfo, Fonts, HorizontalAlign, VerticalAlign
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

FRI: FontRenderInfo = FontRenderInfo(
    clip_text=False,
    enable_shadow=True,
    shadow_info=DepthFieldGlowInfo(
        enable_glow=True,
        glow_color=(100, 100, 100, 255),
        glow_outer_radius=(202, 202),
        glow_inner_radius=(55, 55)
    )
)


def wait_condition() -> bool:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    return pc.Pawn is None or pc.IsPauseMenuOpen() or pc.bStatusMenuOpen


_green = (0, 255, 0, 255)
_gray = (150, 150, 150, 255)


def draw_speedometer() -> PostRenderCoroutine:
    while True:
        yield WaitWhile(wait_condition)
        canvas = yield

        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        velocity = Vector(pc.Pawn.Velocity)
        speed = velocity.magnitude
        # 1 unit = 1 cm ?
        speed_m = speed / 100
        speed_kmh = speed_m * 3.6
        if FreedomUnits.CurrentValue:
            speed_kmh *= 0.621371
        speed_txt = f"{speed_kmh:.2f}"

        with Canvas(canvas, ufont=Fonts.Font_Willowbody_18pt_KOR) as c:
            _, bottom = c.draw_text(
                text=speed_txt,
                x=PosX.CurrentValue / 100,
                y=PosY.CurrentValue / 100,
                horizontal_align=HorizontalAlign.RIGHT,
                vertical_align=VerticalAlign.TOP,
                scale_x=1.5,
                scale_y=1.5,
                color=_green,
                font_render_info=FRI
            )

        with Canvas(canvas, ufont=Fonts.TinyFont) as c:
            metric = "mph" if FreedomUnits.CurrentValue else "km/h"
            _, bottom = c.draw_text(
                text=metric,
                x=PosX.CurrentValue / 100,
                y=bottom,
                horizontal_align=HorizontalAlign.RIGHT,
                vertical_align=VerticalAlign.TOP,
                color=_gray,
                font_render_info=FRI
            )

        if RawVector.CurrentValue:
            velocity_txt = f"Velocity: {velocity.x:.0f} {velocity.y:.0f} {velocity.z:.0f}"
            with Canvas(canvas, ufont=Fonts.TinyFont) as c:
                c.draw_text(
                    text=velocity_txt,
                    x=PosX.CurrentValue / 100,
                    y=bottom,
                    horizontal_align=HorizontalAlign.RIGHT,
                    vertical_align=VerticalAlign.TOP,
                    color=_gray,
                )

        if not mod_instance.IsEnabled:
            break


class Speedometer(SDKMod):
    Name: str = "Speedometer"
    Description: str = "Show the current speed of the player."
    Author: str = "juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.1"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    SupportedGames: Game = Game.BL2 | Game.TPS | Game.AoDK
    Options = [PosX, PosY, FreedomUnits, RawVector]

    def Enable(self) -> None:
        start_coroutine_post_render(draw_speedometer())


mod_instance = Speedometer()
RegisterMod(mod_instance)
