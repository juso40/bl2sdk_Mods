from typing import cast

import imgui

from Mods.mateditor.materials import MaterialInstanceConstant, Materials, Texture2D

from .popups import draw_texture_parameter_popup


def draw() -> None:
    if not Materials.selected:
        imgui.text("Select a Material to edit it.")
        return

    if imgui.collapsing_header("Texture Parameters")[0]:
        draw_texture_parameters()
    with imgui.begin_popup_modal("Select Texture") as select_texture_popup:
        if select_texture_popup.opened:
            draw_texture_parameter_popup()

    if imgui.collapsing_header("Vector Parameters")[0]:
        draw_vector_parameters()

    if imgui.collapsing_header("Scalar Parameters")[0]:
        draw_scalar_parameters()


def draw_texture_parameters() -> None:
    material = cast(MaterialInstanceConstant, Materials.selected)
    for parameter_name in material.texture_parameters:
        if imgui.button(parameter_name, width=-1):
            Texture2D.backup = material.get_texture_parameter_value(parameter_name)[1]
            Texture2D.texture_parameter = parameter_name
            imgui.open_popup("Select Texture")


def draw_vector_parameters() -> None:
    material = cast(MaterialInstanceConstant, Materials.selected)
    for parameter_name, parameter_value in material.vector_parameters.items():
        r, g, b, a = parameter_value
        # If the parameter name contains the word "color" we assume it is a color
        # and use the color picker instead of the float sliders
        if "color" not in parameter_name.lower():
            changed, col = imgui.drag_float4(
                parameter_name, r, g, b, a, change_speed=0.5
            )
            r, g, b, a = col
        else:
            changed, col = imgui.color_edit4(
                parameter_name, r / 2.55, g / 2.55, b / 2.55, a / 2.55
            )
            r, g, b, a = col
            r *= 2.55
            g *= 2.55
            b *= 2.55
            a *= 2.55
        if changed:
            material.vector_parameters[parameter_name] = (r, g, b, a)
            material.set_vector_parameter_value(parameter_name, (r, g, b, a))


def draw_scalar_parameters() -> None:
    material = cast(MaterialInstanceConstant, Materials.selected)
    for parameter_name, parameter_value in material.scalar_parameters.items():
        changed, material.scalar_parameters[parameter_name] = imgui.slider_float(
            label=parameter_name,
            value=parameter_value,
            min_value=-10,
            max_value=10,
        )
        if changed:
            material.set_scalar_parameter_value(parameter_name, parameter_value)
