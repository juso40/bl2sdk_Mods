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

class _FontAtlas(object):
    """
    _FontAtlas()
    Font atlas object responsible for controling and loading fonts.
    
        This class is not intended to be instantiated by user (thus `_`
        name prefix). It should be accessed through :any:`_IO.fonts` attribute
        of :class:`_IO` obtained with :func:`get_io` function.
    
        Example::
    
            import imgui
    
            io = imgui.get_io()
            io.fonts.add_font_default()
    """
    def add_font_default(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.add_font_default(self) """
        pass

    def add_font_from_file_ttf(self, str_filename, float_size_pixels, font_config=None, glyph_ranges=None): # real signature unknown; restored from __doc__
        """ _FontAtlas.add_font_from_file_ttf(self, str filename, float size_pixels, font_config=None, glyph_ranges=None) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.clear(self) """
        pass

    def clear_fonts(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.clear_fonts(self) """
        pass

    def clear_input_data(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.clear_input_data(self) """
        pass

    def clear_tex_data(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.clear_tex_data(self) """
        pass

    def get_glyph_ranges_chinese(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_chinese(self) """
        pass

    def get_glyph_ranges_chinese_full(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_chinese_full(self) """
        pass

    def get_glyph_ranges_cyrillic(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_cyrillic(self) """
        pass

    def get_glyph_ranges_default(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_default(self) """
        pass

    def get_glyph_ranges_japanese(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_japanese(self) """
        pass

    def get_glyph_ranges_korean(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_korean(self) """
        pass

    def get_glyph_ranges_latin(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_latin(self) """
        pass

    def get_glyph_ranges_thai(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_thai(self) """
        pass

    def get_glyph_ranges_vietnamese(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_glyph_ranges_vietnamese(self) """
        pass

    def get_tex_data_as_alpha8(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_tex_data_as_alpha8(self) """
        pass

    def get_tex_data_as_rgba32(self): # real signature unknown; restored from __doc__
        """ _FontAtlas.get_tex_data_as_rgba32(self) """
        pass

    def _require_pointer(self): # real signature unknown; restored from __doc__
        """ _FontAtlas._require_pointer(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _FontAtlas.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _FontAtlas.__setstate_cython__(self, __pyx_state) """
        pass

    texture_desired_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Note: difference in mapping (maps actual TexID and not TextureID)

        Note: texture ID type is implementation dependent. It is usually
        integer (at least for OpenGL).

        """

    texture_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCEAA0>'


