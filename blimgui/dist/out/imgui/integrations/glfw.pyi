from . import compute_fb_scale as compute_fb_scale
from .opengl import ProgrammablePipelineRenderer as ProgrammablePipelineRenderer
from typing import Any

class GlfwRenderer(ProgrammablePipelineRenderer):
    window: Any = ...
    def __init__(self, window: Any, attach_callbacks: bool=...) -> None: ...
    def keyboard_callback(self, window: Any, key: Any, scancode: Any, action: Any, mods: Any) -> None: ...
    def char_callback(self, window: Any, char: Any) -> None: ...
    def resize_callback(self, window: Any, width: Any, height: Any) -> None: ...
    def mouse_callback(self, *args: Any, **kwargs: Any) -> None: ...
    def scroll_callback(self, window: Any, x_offset: Any, y_offset: Any) -> None: ...
    def process_inputs(self) -> None: ...
