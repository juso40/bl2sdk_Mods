from typing import TYPE_CHECKING, Set, cast

import imgui

from Mods.mateditor.materials import MaterialInstanceConstant, Materials, Texture2D

from .popups import draw_texture_parameter_popup

if TYPE_CHECKING:
    import unrealsdk  # type: ignore


LOCKED_PARAMETERS: Set[str] = {
    # It's very unlikely that we ever want to change these parameters
    "p_Masks",
    "p_NormalScopesEmissive",
    "p_Diffuse",
    "p_DigiStruct",
}
VECTOR_AS_COLOR: bool = True


def draw() -> None:
    if not Materials.selected:
        imgui.text("Select a Material to edit it.")
        return

    if imgui.button("Randomize Parameters", width=-1):
        Materials.selected.randomize_parameters(LOCKED_PARAMETERS)

    if imgui.collapsing_header("Texture Parameters")[0]:
        draw_texture_parameters()
    with imgui.begin_popup_modal("Select Texture") as select_texture_popup:
        if select_texture_popup.opened:
            draw_texture_parameter_popup()

    if imgui.collapsing_header("Vector Parameters")[0]:
        global VECTOR_AS_COLOR
        _, VECTOR_AS_COLOR = imgui.checkbox("Interpret as Color", VECTOR_AS_COLOR)
        draw_vector_parameters()

    if imgui.collapsing_header("Scalar Parameters")[0]:
        draw_scalar_parameters()


def draw_texture_parameters() -> None:
    material = cast(MaterialInstanceConstant, Materials.selected)
    for parameter_name in material.texture_parameters:
        lockable_parameter(parameter_name)
        texture: unrealsdk.UObject = material.get_texture_parameter_value(
            parameter_name
        )
        button_text: str = (
            f"{parameter_name: <30}: {texture.PathName(texture) if texture else 'None'}"
        )
        if (
            imgui.button(
                button_text.ljust(150, " "),
                width=-1,
            )
            and parameter_name not in LOCKED_PARAMETERS
        ):
            Texture2D.backup = material.get_texture_parameter_value(parameter_name)
            Texture2D.texture_parameter = parameter_name
            imgui.open_popup("Select Texture")


def draw_vector_parameters() -> None:
    material = cast(MaterialInstanceConstant, Materials.selected)
    for parameter_name, parameter_value in material.vector_parameters.items():
        lockable_parameter(parameter_name)
        r, g, b, a = parameter_value
        # If the parameter name contains the word "color" we assume it is a color
        # and use the color picker instead of the float sliders
        if not VECTOR_AS_COLOR or "color" not in parameter_name.lower():
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
        if changed and parameter_name not in LOCKED_PARAMETERS:
            material.vector_parameters[parameter_name] = (r, g, b, a)
            material.set_vector_parameter_value(parameter_name, (r, g, b, a))


def draw_scalar_parameters() -> None:
    material = cast(MaterialInstanceConstant, Materials.selected)
    for parameter_name, parameter_value in material.scalar_parameters.items():
        lockable_parameter(parameter_name)
        changed, val = imgui.slider_float(
            label=parameter_name,
            value=parameter_value,
            min_value=-2,
            max_value=10,
        )
        if changed and parameter_name not in LOCKED_PARAMETERS:
            material.scalar_parameters[parameter_name] = val
            material.set_scalar_parameter_value(parameter_name, parameter_value)


def lockable_parameter(parameter_name: str) -> None:
    changed, state = imgui.checkbox(
        f"##Lock{parameter_name}", parameter_name in LOCKED_PARAMETERS
    )
    if changed:
        if state:
            LOCKED_PARAMETERS.add(parameter_name)
        else:
            LOCKED_PARAMETERS.remove(parameter_name)
    imgui.same_line()
