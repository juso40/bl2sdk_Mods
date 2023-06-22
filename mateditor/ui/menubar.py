import imgui

from .popups import draw_save_modal, draw_usage_modal


def draw() -> None:
    save_file_modal: bool = False
    usage_modal: bool = False
    with imgui.begin_menu("File") as file_menu:
        if file_menu.opened and imgui.menu_item("Save To File")[0]:
            save_file_modal = True
    with imgui.begin_menu("Help") as help_menu:
        if help_menu.opened and imgui.menu_item("Usage")[0]:
            usage_modal = True

    if save_file_modal:
        imgui.open_popup("Save File")
    with imgui.begin_popup_modal(
        title="Save File", flags=imgui.WINDOW_ALWAYS_AUTO_RESIZE
    ) as save_modal:
        if save_modal.opened:
            draw_save_modal()
    if usage_modal:
        imgui.open_popup("Usage")
    with imgui.begin_popup_modal(
        title="Usage", flags=imgui.WINDOW_ALWAYS_AUTO_RESIZE
    ) as usage_popup_modal:
        if usage_popup_modal.opened:
            draw_usage_modal()