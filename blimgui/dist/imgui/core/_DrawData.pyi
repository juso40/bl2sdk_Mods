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

class _DrawData(object):
    """ _DrawData() """
    def deindex_all_buffers(self): # real signature unknown; restored from __doc__
        """ _DrawData.deindex_all_buffers(self) """
        pass

    def scale_clip_rects(self, width, height): # real signature unknown; restored from __doc__
        """ _DrawData.scale_clip_rects(self, width, height) """
        pass

    def _require_pointer(self): # real signature unknown; restored from __doc__
        """ _DrawData._require_pointer(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _DrawData.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _DrawData.__setstate_cython__(self, __pyx_state) """
        pass

    cmd_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    commands_lists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_buffer_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_idx_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_vtx_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCEA28>'


