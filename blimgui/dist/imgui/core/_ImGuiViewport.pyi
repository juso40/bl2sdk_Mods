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

class _ImGuiViewport(object):
    """
    _ImGuiViewport()
    Currently represents the Platform Window created by the application which is hosting our Dear ImGui windows.
           
           About Main Area vs Work Area:
           - Main Area = entire viewport.
           - Work Area = entire viewport minus sections used by main menu bars (for platform windows), or by task bar (for platform monitor).
           - Windows are generally trying to stay within the Work Area of their host viewport.
    """
    def get_center(self): # real signature unknown; restored from __doc__
        """ _ImGuiViewport.get_center(self) """
        pass

    def get_work_center(self): # real signature unknown; restored from __doc__
        """ _ImGuiViewport.get_work_center(self) """
        pass

    def _require_pointer(self): # real signature unknown; restored from __doc__
        """ _ImGuiViewport._require_pointer(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _ImGuiViewport.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _ImGuiViewport.__setstate_cython__(self, __pyx_state) """
        pass

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Main Area: Position of the viewport (Dear ImGui coordinates are the same as OS desktop/native coordinates)"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Main Area: Size of the viewport."""

    work_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Work Area: Position of the viewport minus task bars, menus bars, status bars (>= Pos)"""

    work_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Work Area: Size of the viewport minus task bars, menu bars, status bars (<= Size)"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCE9F8>'


