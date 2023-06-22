# encoding: utf-8
# module imgui.internal
# from C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\imgui\internal.cp37-win32.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from imgui.core import ImGuiError


# Variables with simple values

AXIS_NONE = -1
AXIS_X = 0
AXIS_Y = 1

BUTTON_ALIGN_TEXT_BASE_LINE = 32768

BUTTON_ALLOW_ITEM_OVERLAP = 4096

BUTTON_DISABLED = 16384

BUTTON_DONT_CLOSE_POPUPS = 8192

BUTTON_FLATTEN_CHILDREN = 2048

BUTTON_NO_HOLDING_ACTIVE_ID = 131072

BUTTON_NO_HOVERED_ON_FOCUS = 524288

BUTTON_NO_KEY_MODIFIERS = 65536

BUTTON_NO_NAV_FOCUS = 262144

BUTTON_PRESSED_ON_CLICK = 16

BUTTON_PRESSED_ON_CLICK_RELEASE = 32

BUTTON_PRESSED_ON_CLICK_RELEASE_ANYWHERE = 64

BUTTON_PRESSED_ON_DEFAULT = 32

BUTTON_PRESSED_ON_DOUBLE_CLICK = 256

BUTTON_PRESSED_ON_DRAG_DROP_HOLD = 512

BUTTON_PRESSED_ON_MASK = 1008
BUTTON_PRESSED_ON_RELEASE = 128

BUTTON_REPEAT = 1024

INPUT_READ_MODE_DOWN = 0
INPUT_READ_MODE_PRESSED = 1
INPUT_READ_MODE_RELEASED = 2
INPUT_READ_MODE_REPEAT = 3

INPUT_READ_MODE_REPEAT_FAST = 5
INPUT_READ_MODE_REPEAT_SLOW = 4

INPUT_SOURCE_COUNT = 5
INPUT_SOURCE_GAMEPAD = 3
INPUT_SOURCE_KEYBOARD = 2
INPUT_SOURCE_MOUSE = 1
INPUT_SOURCE_NAV = 4
INPUT_SOURCE_NONE = 0

ITEM_BUTTON_REPEAT = 2

ITEM_DEFAULT = 0
ITEM_DISABLED = 4

ITEM_MIXED_VALUE = 64

ITEM_NONE = 0

ITEM_NO_NAV = 8

ITEM_NO_NAV_DEFAULT_FOCUS = 16

ITEM_NO_TAB_STOP = 1

ITEM_READ_ONLY = 128

ITEM_SELECTABLE_DONT_CLOSE_POPUP = 32

ITEM_STATUS_DEACTIVATED = 64
ITEM_STATUS_EDITED = 4

ITEM_STATUS_HAS_DEACTIVATED = 32

ITEM_STATUS_HAS_DISPLAY_RECT = 2

ITEM_STATUS_HOVERED_RECT = 1

ITEM_STATUS_NONE = 0

ITEM_STATUS_TOGGLED_OPEN = 16
ITEM_STATUS_TOGGLED_SELECTION = 8

LAYOUT_TYPE_HORIZONTAL = 0
LAYOUT_TYPE_VERTICAL = 1

LOG_TYPE_LOG_TYPE_BUFFER = 3
LOG_TYPE_LOG_TYPE_CLIPBOARD = 4
LOG_TYPE_LOG_TYPE_FILE = 2
LOG_TYPE_LOG_TYPE_TTY = 1

LOG_TYPE_NONE = 0

NAV_DIR_SOURCE_KEYBOARD = 1
NAV_DIR_SOURCE_NONE = 0

NAV_DIR_SOURCE_PAD_D_PAD = 2

NAV_DIR_SOURCE_PAD_L_STICK = 4

NAV_FORWARD_FORWARD_ACTIVE = 2
NAV_FORWARD_FORWARD_QUEUED = 1

NAV_FORWARD_NONE = 0

NAV_HIGHLIGHT_ALWAYS_DRAW = 4

NAV_HIGHLIGHT_NONE = 0

NAV_HIGHLIGHT_NO_ROUNDING = 8

NAV_HIGHLIGHT_TYPE_DEFAULT = 1
NAV_HIGHLIGHT_TYPE_THIN = 2

NAV_LAYER_COUNT = 2
NAV_LAYER_MAIN = 0
NAV_LAYER_MENU = 1

NAV_MOVE_ALLOW_CURRENT_NAV_ID = 16

NAV_MOVE_ALSO_SCORE_VISIBLE_SET = 32

NAV_MOVE_LOOP_X = 1
NAV_MOVE_LOOP_Y = 2

NAV_MOVE_NONE = 0

NAV_MOVE_SCROLL_TO_EDGE = 64

NAV_MOVE_WRAP_X = 4
NAV_MOVE_WRAP_Y = 8

NEXT_ITEM_DATA_HAS_OPEN = 2
NEXT_ITEM_DATA_HAS_WIDTH = 1

NEXT_ITEM_DATA_NONE = 0

NEXT_WINDOW_DATA_HAS_BACKGROUND_ALPHA = 64

NEXT_WINDOW_DATA_HAS_COLLAPSED = 8

NEXT_WINDOW_DATA_HAS_CONTENT_SIZE = 4

NEXT_WINDOW_DATA_HAS_FOCUS = 32
NEXT_WINDOW_DATA_HAS_POS = 1
NEXT_WINDOW_DATA_HAS_SCROLL = 128
NEXT_WINDOW_DATA_HAS_SIZE = 2

NEXT_WINDOW_DATA_HAS_SIZE_CONSTRAINT = 16

NEXT_WINDOW_DATA_NONE = 0

OLD_COLUMNS_GROW_PARENT_CONTENTS_SIZE = 16

OLD_COLUMNS_NONE = 0

OLD_COLUMNS_NO_BORDER = 1

OLD_COLUMNS_NO_FORCE_WIDTHIN_WINDOW = 8

OLD_COLUMNS_NO_PRESERVE_WIDTHS = 4

OLD_COLUMNS_NO_RESIZE = 2

PLOT_TYPE_HISTOGRAM = 1
PLOT_TYPE_LINES = 0

POPUP_POSITION_POLICY_COMBO_BOX = 1

POPUP_POSITION_POLICY_DEFAULT = 0
POPUP_POSITION_POLICY_TOOLTIP = 2

SELECTABLE_DRAW_HOVERED_WHEN_HELD = 16777216

SELECTABLE_NO_HOLDING_ACTIVE_ID = 1048576

SELECTABLE_NO_PAD_WIDHT_HALF_SPACING = 67108864

SELECTABLE_SELECT_ON_CLICK = 2097152
SELECTABLE_SELECT_ON_RELEASE = 4194304

SELECTABLE_SET_NAV_ID_ON_HOVER = 33554432

SELECTABLE_SPAN_AVAILABLE_WIDTH = 8388608

SEPARATOR_HORIZONTAL = 1
SEPARATOR_NONE = 0

SEPARATOR_SPAN_ALL_COLUMNS = 4

SEPARATOR_VERTICAL = 2

SLIDER_READ_ONLY = 2097152

SLIDER_VERTICAL = 1048576

TAB_BAR_DOCK_NODE = 1048576

TAB_BAR_IS_FOCUSED = 2097152

TAB_BAR_SAVE_SETTINGS = 4194304

TAB_ITEM_BUTTON = 2097152

TAB_ITEM_NO_CLOSE_BUTTON = 1048576

TEXT_NONE = 0

TEXT_NO_WIDTH_FRO_LARGE_CLIPPED_TEXT = 1

TOOLTIP_NONE = 0

TOOLTIP_OVERRIDE_PREVIOUS_TOOLTIP = 1

TREE_NODE_CLIP_LABEL_FOR_TRAILING_BUTTON = 1048576

# functions

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def pop_item_flag(): # real signature unknown; restored from __doc__
    """ pop_item_flag() """
    pass

def push_item_flag(ImGuiItemFlags_option, bool_enabled): # real signature unknown; restored from __doc__
    """ push_item_flag(ImGuiItemFlags option, bool enabled) """
    pass

# classes

class Vec2(tuple):
    """ Vec2(x, y) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Vec2 object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new Vec2 object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, x, y): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, x, y): # reliably restored by inspect
        """ Create new instance of Vec2(x, y) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'x',
        'y',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()


class Vec4(tuple):
    """ Vec4(x, y, z, w) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Vec4 object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new Vec4 object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, x, y, z, w): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, x, y, z, w): # reliably restored by inspect
        """ Create new instance of Vec4(x, y, z, w) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""


    _fields = (
        'x',
        'y',
        'z',
        'w',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x032E5AF0>'

__pyx_capi__ = {
    'UpdateImGuiContext': None, # (!) real value is '<capsule object "PyObject *(ImGuiContext *)" at 0x032AEEC0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='imgui.internal', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x032E5AF0>, origin='C:\\\\Users\\\\justi\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python37-32\\\\lib\\\\site-packages\\\\imgui\\\\internal.cp37-win32.pyd')"

__test__ = {}

