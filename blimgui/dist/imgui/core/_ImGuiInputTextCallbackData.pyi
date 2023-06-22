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

class _ImGuiInputTextCallbackData(object):
    """ _ImGuiInputTextCallbackData() """
    def clear_selection(self): # real signature unknown; restored from __doc__
        """ _ImGuiInputTextCallbackData.clear_selection(self) """
        pass

    def delete_chars(self, int_pos, int_bytes_count): # real signature unknown; restored from __doc__
        """ _ImGuiInputTextCallbackData.delete_chars(self, int pos, int bytes_count) """
        pass

    def has_selection(self): # real signature unknown; restored from __doc__
        """ _ImGuiInputTextCallbackData.has_selection(self) """
        pass

    def insert_chars(self, int_pos, str_text): # real signature unknown; restored from __doc__
        """ _ImGuiInputTextCallbackData.insert_chars(self, int pos, str text) """
        pass

    def select_all(self): # real signature unknown; restored from __doc__
        """ _ImGuiInputTextCallbackData.select_all(self) """
        pass

    def _require_pointer(self): # real signature unknown; restored from __doc__
        """ _ImGuiInputTextCallbackData._require_pointer(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _ImGuiInputTextCallbackData.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _ImGuiInputTextCallbackData.__setstate_cython__(self, __pyx_state) """
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_dirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_text_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCEB60>'


