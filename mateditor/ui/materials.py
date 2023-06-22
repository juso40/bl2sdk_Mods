import imgui

from Mods.mateditor.materials import Materials


class State:
    number_items: int = 16
    search: str = ""
    index: int = -1


def draw() -> None:
    imgui.push_item_width(-1)
    imgui.text("Search:")
    _, State.search = imgui.input_text("##Search", State.search, 32)
    material_names = Materials.all_materials(State.search)
    listbox_clicked, State.index = imgui.listbox(
        "##Materials", State.index, material_names, State.number_items
    )
    if listbox_clicked:
        Materials.select(material_names[State.index])
    imgui.text("Number of Materials shown:")
    _, State.number_items = imgui.slider_int(
        "##Number of Materials", State.number_items, 1, 32
    )
    imgui.pop_item_width()
