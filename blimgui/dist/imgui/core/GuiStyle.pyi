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

class GuiStyle(object):
    """ Container for ImGui style information """
    def color(self, ImGuiCol_variable): # real signature unknown; restored from __doc__
        """ GuiStyle.color(self, ImGuiCol variable) """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ GuiStyle.create() """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ GuiStyle.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ GuiStyle.__setstate_cython__(self, __pyx_state) """
        pass

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Global alpha blending parameter for windows

        Returns:
            float
        """

    anti_aliased_fill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    anti_aliased_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    anti_aliased_line_use_tex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_text_align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cell_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_border_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    circle_segment_max_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    circle_tessellation_max_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve and modify style colors through list-like interface.

        .. visual-example::
            :width: 700
            :height: 500
            :auto_layout:

            style = imgui.get_style()
            imgui.begin("Color window")
            imgui.columns(4)
            for color in range(0, imgui.COLOR_COUNT):
                imgui.text("Color: {}".format(color))
                imgui.color_button("color#{}".format(color), *style.colors[color])
                imgui.next_column()

            imgui.end()
        """

    color_button_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    columns_min_spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    curve_tessellation_tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_safe_area_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_window_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_border_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_min_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indent_spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    item_inner_spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    item_spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    log_slider_deadzone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_cursor_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    popup_border_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    popup_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scrollbar_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scrollbar_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selectable_text_align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tab_border_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tab_min_width_for_close_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tab_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touch_extra_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_border_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_menu_button_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_min_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_title_align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCE938>'


