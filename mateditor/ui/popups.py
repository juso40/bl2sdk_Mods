from typing import cast

import imgui

from Mods.mateditor.export import PATH, BLCMExport
from Mods.mateditor.materials import MaterialInstanceConstant, Materials, Texture2D


def draw_usage_modal() -> None:
    imgui.text_unformatted(
        """
This tool allows real-time editing of the various Parameters of a MaterialInstanceConstant.

Float values will be exported the same as shown in this tool.
Color values will be divided by 100, that means 255 equals to 2.55 in the exported file. 
(Note this might cause some inconsistencies as the games color system is kinda weird.)

All values shown are sliders, that means you need to drag the slider to the desired value.
To do fine adjustments you can CTRL+LeftClick on the slider to change the value manually."""
    )
    if imgui.button("Close"):
        imgui.close_current_popup()


def draw_save_modal() -> None:
    imgui.text("Save Current Skin to file:")
    _, BLCMExport.file_name = imgui.input_text("File Name", BLCMExport.file_name, 32)
    imgui.text(
        f"Will be saved as '{(PATH / f'../{BLCMExport.file_name}').resolve()}.blcm'"
    )
    imgui.text("Saving this file will overwrite any existing file with the same name!")

    if imgui.button("Save"):
        if Materials.selected:
            BLCMExport.save_to_file(
                PATH / f"../{BLCMExport.file_name}.blcm",
                material=Materials.selected.material_instance_constant,
            )
        BLCMExport.file_name = "Skin"
        imgui.close_current_popup()
    imgui.same_line()
    if imgui.button("Cancel"):
        BLCMExport.file_name = "Skin"
        imgui.close_current_popup()


def draw_texture_parameter_popup() -> None:
    selected_material = cast(MaterialInstanceConstant, Materials.selected)
    imgui.text("Select any material and press 'Select' or 'Cancel'")

    _, Texture2D.search = imgui.input_text("Search##2", Texture2D.search, 32)
    textures = Texture2D.all_textures(Texture2D.search)

    changed, Texture2D.index = imgui.listbox(
        "##TextureListBox", Texture2D.index, textures, 16
    )
    if changed:
        selected_material.set_texture_parameter_value(
            Texture2D.texture_parameter, textures[Texture2D.index]
        )

    if imgui.button("Select##2"):
        selected_material.set_texture_parameter_value(
            Texture2D.texture_parameter, textures[Texture2D.index]
        )
        imgui.close_current_popup()

    imgui.same_line()
    if imgui.button("Cancel##2"):
        selected_material.set_texture_parameter_value(
            Texture2D.texture_parameter, Texture2D.backup
        )
        imgui.close_current_popup()
