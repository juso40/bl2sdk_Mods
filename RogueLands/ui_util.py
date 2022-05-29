class Colors:
    GREEN: str = "#0BDA51"
    RED: str = "#d91d1e"
    YELLOW: str = "#FFD300"


def color_text(text: str, color: str) -> str:
    """Returns a string with the given text in the given color"""
    return f"<font color=\"{color}\">{text}</font>"


def color_text_conditional(text: str, col_true: str, col_false: str, condition: bool) -> str:
    """Returns a string with the given text in the given color"""
    if condition:
        return color_text(text, col_true)
    else:
        return color_text(text, col_false)


def size_text(text: str, size: int) -> str:
    """Returns a string with the given text in the given size"""
    return f"<font size=\"{size}\">{text}</font>"
