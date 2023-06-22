from typing import List, Tuple

import imgui


def combo_with_title(
    title: str, current: int, items: List[str], spacing: bool = False
) -> Tuple[bool, int]:
    """Draws a combo box with a title above it."""
    if spacing:
        imgui.spacing()
        imgui.spacing()
    imgui.text(title)
    imgui.push_item_width(-1)
    clicked, current = imgui.combo(
        f"##{title}",
        current=current,
        items=items,
    )
    imgui.pop_item_width()
    return clicked, current
