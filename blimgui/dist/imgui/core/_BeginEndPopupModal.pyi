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

class _BeginEndPopupModal(object):
    """
    Return value of :func:`begin_popup_modal` exposing ``opened`` and ``visible`` boolean attributes.
        See :func:`begin_popup_modal` for an explanation and examples.
    
        For legacy support, the attributes can also be accessed by unpacking or indexing into this object.
    
        Can be used as a context manager (in a ``with`` statement) to automatically call :func:`end_popup`
        (if necessary) to end the popup created with :func:`begin_popup_modal` when the block ends,
        even if an exception is raised.
    
        This class is not intended to be instantiated by the user (thus the `_` name prefix).
        It should be obtained as the return value of the :func:`begin_popup_modal` function.
    """
    def __enter__(self): # real signature unknown; restored from __doc__
        """ _BeginEndPopupModal.__enter__(self) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb): # real signature unknown; restored from __doc__
        """ _BeginEndPopupModal.__exit__(self, exc_type, exc_val, exc_tb) """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ For legacy support, returns ``(opened, visible)[item]``. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ For legacy support, returns ``iter((opened, visible))``. """
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
        """ _BeginEndPopupModal.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _BeginEndPopupModal.__setstate_cython__(self, __pyx_state) """
        pass

    opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


