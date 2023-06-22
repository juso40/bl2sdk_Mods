import site
from typing import Any, Callable, Union, cast

import unrealsdk  # type: ignore

from Mods.ModMenu import (
    EnabledSaveType,
    LoadModSettings,
    ModPriorities,
    ModTypes,
    Options,
    RegisterMod,
    SaveAllModSettings,
    SDKMod,
)

site.addsitedir("Mods/blimgui/dist")

__version__ = "2.0"

import imgui  # noqa: E402
import pyglet  # noqa: E402
from imgui.integrations.pyglet import PygletRenderer, create_renderer  # noqa: E402
from pyglet import gl  # noqa: E402

DRAW_FUN = Callable[[], None]

WINDOW = None
IMPL = None

SizeX = Options.Hidden("WindowX", StartingValue=1280)
SizeY = Options.Hidden("WindowY", StartingValue=720)
ImguiStyle = Options.Spinner(
    "ImguiStyle",
    Description="Change the look of the Imgui window",
    Choices=["Classic", "Dark", "Light", "Modern Dark"],
    StartingChoice="Modern Dark",
)


def create_window(
    caption: str,
    width: Union[int, Options.Hidden] = SizeX,
    height: Union[int, Options.Hidden] = SizeY,
    resizable: bool = True,
) -> None:
    """
    Create a new window with the given parameters. If a window already exists, rename only.

    :param caption: The caption of the window
    :param width: The width of the window
    :param height: The height of the window
    :param resizable: If True, window is resizable, else cannot be resized.
    :return: None
    """
    global WINDOW
    global IMPL
    if not WINDOW and not IMPL:
        gl.glClearColor(1, 1, 1, 1)
        imgui.create_context()
        WINDOW = pyglet.window.Window(
            width=width if isinstance(width, int) else width.CurrentValue,
            height=height if isinstance(height, int) else height.CurrentValue,
            resizable=resizable,
            caption=caption,
        )
        IMPL = create_renderer(WINDOW)

        def on_resize(w: int, h: int) -> None:
            SizeX.CurrentValue = w
            SizeY.CurrentValue = h
            SaveAllModSettings()

        WINDOW.push_handlers(on_resize)
        style_ui(ImguiStyle.CurrentValue)

    elif WINDOW:
        WINDOW.set_caption(caption=caption)
        style_ui(ImguiStyle.CurrentValue)


def close_window() -> bool:
    """
    Close the current window if any is open.

    :return: Bool, True if window successfully closed, else False
    """
    global WINDOW
    global IMPL
    global ACTIVE_CALLBACK
    try:
        cast(PygletRenderer, IMPL).shutdown()
        cast(pyglet.window.Window, WINDOW).close()

        WINDOW = None
        IMPL = None
        ACTIVE_CALLBACK = update
        return True
    except Exception as e:
        unrealsdk.Log(e)
        return False


def update() -> None:
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item("Quit", "Cmd+Q", False, True)
            if clicked_quit:
                close_window()
            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.begin("Hello World", True)
    imgui.text("This is a text!")
    imgui.text_colored("Colored Text, wow!", 0.2, 1.0, 0.0)

    imgui.end()


def draw() -> None:
    """
    Calls the currently active callback function to update the rendered content in the new window.

    :return: None
    """
    if not WINDOW:
        return
    imgui.new_frame()
    ACTIVE_CALLBACK()
    WINDOW.clear()
    imgui.render()
    cast(PygletRenderer, IMPL).render(imgui.get_draw_data())


ACTIVE_CALLBACK = update


def set_draw_callback(callback: DRAW_FUN) -> None:
    """
    Set the given callable as active callback each draw tick.

    :param callback: Reference to the callable.
    :return: None
    """
    global ACTIVE_CALLBACK
    ACTIVE_CALLBACK = callback


def _on_tick(
    caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct
) -> bool:
    draw()
    for w in pyglet.app.windows:
        w.switch_to()
        w.dispatch_events()
        w.dispatch_event("on_draw")
        w.flip()
    return True


unrealsdk.RunHook("WillowGame.WillowGameViewportClient.Tick", "WindowTick", _on_tick)


def style_ui(new_style: str) -> None:
    if new_style == "Classic":
        return imgui.style_colors_classic()
    elif new_style == "Dark":
        return imgui.style_colors_dark()
    elif new_style == "Light":
        return imgui.style_colors_light()
    imgui.style_colors_dark()

    s = imgui.get_style()
    s.frame_rounding = 4
    s.popup_rounding = 2
    s.frame_padding = (8, 3)
    s.item_spacing = (4, 2)
    s.item_inner_spacing = (2, 4)
    s.indent_spacing = 16
    s.scrollbar_size = 12
    s.grab_min_size = 6
    s.window_rounding = 0
    s.scrollbar_rounding = 12
    s.grab_rounding = 12

    colors = s.colors

    colors[imgui.COLOR_TEXT] = (0.90, 0.90, 0.90, 1.00)
    colors[imgui.COLOR_WINDOW_BACKGROUND] = (0.10, 0.10, 0.10, 0.94)
    colors[imgui.COLOR_POPUP_BACKGROUND] = (0.10, 0.10, 0.10, 0.94)
    colors[imgui.COLOR_BORDER] = (0.22, 0.22, 0.22, 1.00)
    colors[imgui.COLOR_FRAME_BACKGROUND] = (0.16, 0.16, 0.16, 1.00)
    colors[imgui.COLOR_FRAME_BACKGROUND_HOVERED] = (0.20, 0.20, 0.20, 1.00)
    colors[imgui.COLOR_FRAME_BACKGROUND_ACTIVE] = (0.13, 0.26, 0.45, 1.00)
    colors[imgui.COLOR_TITLE_BACKGROUND] = (0.16, 0.16, 0.16, 1.00)
    colors[imgui.COLOR_TITLE_BACKGROUND_ACTIVE] = (0.13, 0.26, 0.45, 1.00)
    colors[imgui.COLOR_TITLE_BACKGROUND_COLLAPSED] = (0.16, 0.16, 0.16, 1.00)
    colors[imgui.COLOR_MENUBAR_BACKGROUND] = (0.16, 0.16, 0.16, 1.00)
    colors[imgui.COLOR_SCROLLBAR_BACKGROUND] = (0.10, 0.10, 0.10, 1.00)
    colors[imgui.COLOR_SCROLLBAR_GRAB] = (0.27, 0.27, 0.27, 1.00)
    colors[imgui.COLOR_SCROLLBAR_GRAB_HOVERED] = (0.45, 0.45, 0.45, 1.00)
    colors[imgui.COLOR_SCROLLBAR_GRAB_ACTIVE] = (0.45, 0.45, 0.45, 1.00)
    colors[imgui.COLOR_CHECK_MARK] = (0.93, 0.79, 0.00, 1.00)
    colors[imgui.COLOR_SLIDER_GRAB] = (0.13, 0.26, 0.45, 1.00)
    colors[imgui.COLOR_SLIDER_GRAB_ACTIVE] = (0.22, 0.53, 0.94, 1.00)
    colors[imgui.COLOR_BUTTON] = (0.92, 0.52, 0.14, 1.00)
    colors[imgui.COLOR_BUTTON_HOVERED] = (0.93, 0.82, 0.21, 1.00)
    colors[imgui.COLOR_BUTTON_ACTIVE] = (0.93, 0.75, 0.03, 1.00)
    colors[imgui.COLOR_BUTTON_HOVERED] = (0.83, 0.61, 0.13, 1.00)
    colors[imgui.COLOR_BUTTON_ACTIVE] = (0.98, 0.79, 0.15, 1.00)
    colors[imgui.COLOR_HEADER] = (0.22, 0.53, 0.94, 1.00)
    colors[imgui.COLOR_HEADER_HOVERED] = (0.50, 0.50, 0.50, 1.00)
    colors[imgui.COLOR_HEADER_ACTIVE] = (0.22, 0.53, 0.94, 1.00)
    colors[imgui.COLOR_RESIZE_GRIP] = (0.13, 0.26, 0.45, 1.00)
    colors[imgui.COLOR_RESIZE_GRIP_HOVERED] = (0.22, 0.53, 0.94, 1.00)
    colors[imgui.COLOR_RESIZE_GRIP_ACTIVE] = (0.22, 0.53, 0.94, 1.00)
    colors[imgui.COLOR_TEXT_SELECTED_BACKGROUND] = (0.09, 0.22, 0.39, 1.00)
    colors[imgui.COLOR_MODAL_WINDOW_DIM_BACKGROUND] = (0.00, 0.00, 0.00, 0.61)


class BLImgui(SDKMod):
    Name = "BLImgui"
    Author = "juso"
    Description = (
        "A library that allows the creation of a separate window with imgui support."
    )
    Version = __version__

    Options = [SizeX, SizeY, ImguiStyle]
    Types = ModTypes.Library
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    Priority = ModPriorities.Library
    Status = "Enabled"

    def ModOptionChanged(self, option, new_value: Any) -> None:  # noqa: N802
        if option == ImguiStyle:
            if WINDOW:
                style_ui(new_value)
            else:
                return


instance = BLImgui()
RegisterMod(instance)
LoadModSettings(instance)
