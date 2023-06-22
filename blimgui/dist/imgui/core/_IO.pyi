# encoding: utf-8
# module imgui.core
# from C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\imgui\core.cp37-win32.pyd
# by generator 1.147
"""
.. todo:: consider inlining every occurence of ``_cast_args_ImVecX`` (profile)
.. todo: verify mem safety of char* variables and check for leaks
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\warnings.py
from itertools import izip_longest


from .object import object

class _IO(object):
    """
    _IO()
    Main ImGui I/O context class used for ImGui configuration.
    
        This class is not intended to be instantiated by user (thus `_`
        name prefix). It should be accessed through obtained with :func:`get_io`
        function.
    
        Example::
    
            import imgui
    
            io = imgui.get_io()
    """
    def add_input_character(self, unsigned_int_c): # real signature unknown; restored from __doc__
        """ _IO.add_input_character(self, unsigned int c) """
        pass

    def add_input_characters_utf8(self, str_utf8_chars): # real signature unknown; restored from __doc__
        """ _IO.add_input_characters_utf8(self, str utf8_chars) """
        pass

    def add_input_character_utf16(self, str_utf16_chars): # real signature unknown; restored from __doc__
        """ _IO.add_input_character_utf16(self, str utf16_chars) """
        pass

    def clear_input_characters(self): # real signature unknown; restored from __doc__
        """ _IO.clear_input_characters(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _IO.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _IO.__setstate_cython__(self, __pyx_state) """
        pass

    backend_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_cursor_blink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_drag_click_to_input_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_mac_osx_behaviors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_memory_compact_timer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_windows_move_from_title_bar_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_windows_resize_from_edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delta_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_fb_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fonts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_allow_user_scaling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_global_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    framerate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_clipboard_text_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ini_file_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ini_saving_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keys_down = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_alt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_ctrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_repeat_delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_repeat_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_super = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    log_file_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metrics_active_allocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metrics_active_windows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metrics_render_indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metrics_render_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metrics_render_windows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_double_click_max_distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_double_click_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_down = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_drag_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_draw_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_wheel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_wheel_horizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nav_active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nav_inputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nav_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_clipboard_text_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    want_capture_keyboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    want_capture_mouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    want_save_ini_settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    want_set_mouse_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    want_text_input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCEAD0>'


