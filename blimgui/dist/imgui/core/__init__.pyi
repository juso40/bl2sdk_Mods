# encoding: utf-8
# module imgui.core
# from C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\imgui\core.cp37-win32.pyd
# by generator 1.147
"""
.. todo:: consider inlining every occurence of ``_cast_args_ImVecX`` (profile)
.. todo: verify mem safety of char* variables and check for leaks
"""

# imports
import builtins as __builtins__
from typing import Optional, Tuple # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\warnings.py
from itertools import izip_longest


# Variables with simple values

ALWAYS = 1

APPEARING = 8

BACKEND_HAS_GAMEPAD = 1

BACKEND_HAS_MOUSE_CURSORS = 2

BACKEND_HAS_SET_MOUSE_POS = 4

BACKEND_NONE = 0

BACKEND_RENDERER_HAS_VTX_OFFSET = 8

BUTTON_MOUSE_BUTTON_LEFT = 1
BUTTON_MOUSE_BUTTON_MIDDLE = 4
BUTTON_MOUSE_BUTTON_RIGHT = 2

BUTTON_NONE = 0

COLOR_BORDER = 5

COLOR_BORDER_SHADOW = 6

COLOR_BUTTON = 21

COLOR_BUTTON_ACTIVE = 23
COLOR_BUTTON_HOVERED = 22

COLOR_CHECK_MARK = 18

COLOR_CHILD_BACKGROUND = 3

COLOR_COUNT = 53

COLOR_DRAG_DROP_TARGET = 48

COLOR_EDIT_ALPHA_BAR = 65536
COLOR_EDIT_ALPHA_PREVIEW = 131072

COLOR_EDIT_ALPHA_PREVIEW_HALF = 262144

COLOR_EDIT_DEFAULT_OPTIONS = 177209344

COLOR_EDIT_DISPLAY_HEX = 4194304
COLOR_EDIT_DISPLAY_HSV = 2097152
COLOR_EDIT_DISPLAY_RGB = 1048576

COLOR_EDIT_FLOAT = 16777216
COLOR_EDIT_HDR = 524288

COLOR_EDIT_INPUT_HSV = 268435456
COLOR_EDIT_INPUT_RGB = 134217728

COLOR_EDIT_NONE = 0

COLOR_EDIT_NO_ALPHA = 2
COLOR_EDIT_NO_BORDER = 1024

COLOR_EDIT_NO_DRAG_DROP = 512

COLOR_EDIT_NO_INPUTS = 32
COLOR_EDIT_NO_LABEL = 128
COLOR_EDIT_NO_OPTIONS = 8
COLOR_EDIT_NO_PICKER = 4

COLOR_EDIT_NO_SIDE_PREVIEW = 256

COLOR_EDIT_NO_SMALL_PREVIEW = 16

COLOR_EDIT_NO_TOOLTIP = 64

COLOR_EDIT_PICKER_HUE_BAR = 33554432
COLOR_EDIT_PICKER_HUE_WHEEL = 67108864

COLOR_EDIT_UINT8 = 8388608

COLOR_FRAME_BACKGROUND = 7

COLOR_FRAME_BACKGROUND_ACTIVE = 9
COLOR_FRAME_BACKGROUND_HOVERED = 8

COLOR_HEADER = 24

COLOR_HEADER_ACTIVE = 26
COLOR_HEADER_HOVERED = 25

COLOR_MENUBAR_BACKGROUND = 13

COLOR_MODAL_WINDOW_DIM_BACKGROUND = 52

COLOR_NAV_HIGHLIGHT = 49

COLOR_NAV_WINDOWING_DIM_BACKGROUND = 51

COLOR_NAV_WINDOWING_HIGHLIGHT = 50

COLOR_PLOT_HISTOGRAM = 40

COLOR_PLOT_HISTOGRAM_HOVERED = 41

COLOR_PLOT_LINES = 38

COLOR_PLOT_LINES_HOVERED = 39

COLOR_POPUP_BACKGROUND = 4

COLOR_RESIZE_GRIP = 30

COLOR_RESIZE_GRIP_ACTIVE = 32
COLOR_RESIZE_GRIP_HOVERED = 31

COLOR_SCROLLBAR_BACKGROUND = 14
COLOR_SCROLLBAR_GRAB = 15

COLOR_SCROLLBAR_GRAB_ACTIVE = 17
COLOR_SCROLLBAR_GRAB_HOVERED = 16

COLOR_SEPARATOR = 27

COLOR_SEPARATOR_ACTIVE = 29
COLOR_SEPARATOR_HOVERED = 28

COLOR_SLIDER_GRAB = 19

COLOR_SLIDER_GRAB_ACTIVE = 20

COLOR_TAB = 33

COLOR_TABLE_BORDER_LIGHT = 44
COLOR_TABLE_BORDER_STRONG = 43

COLOR_TABLE_HEADER_BACKGROUND = 42

COLOR_TABLE_ROW_BACKGROUND = 45

COLOR_TABLE_ROW_BACKGROUND_ALT = 46

COLOR_TAB_ACTIVE = 35
COLOR_TAB_HOVERED = 34
COLOR_TAB_UNFOCUSED = 36

COLOR_TAB_UNFOCUSED_ACTIVE = 37

COLOR_TEXT = 0

COLOR_TEXT_DISABLED = 1

COLOR_TEXT_SELECTED_BACKGROUND = 47

COLOR_TITLE_BACKGROUND = 10

COLOR_TITLE_BACKGROUND_ACTIVE = 11
COLOR_TITLE_BACKGROUND_COLLAPSED = 12

COLOR_WINDOW_BACKGROUND = 2

COMBO_HEIGHT_LARGE = 8
COMBO_HEIGHT_LARGEST = 16
COMBO_HEIGHT_MASK = 30
COMBO_HEIGHT_REGULAR = 4
COMBO_HEIGHT_SMALL = 2

COMBO_NONE = 0

COMBO_NO_ARROW_BUTTON = 32

COMBO_NO_PREVIEW = 64

COMBO_POPUP_ALIGN_LEFT = 1

CONFIG_IS_RGB = 1048576

CONFIG_IS_TOUCH_SCREEN = 2097152

CONFIG_NAV_ENABLE_GAMEPAD = 2
CONFIG_NAV_ENABLE_KEYBOARD = 1

CONFIG_NAV_ENABLE_SET_MOUSE_POS = 4

CONFIG_NAV_NO_CAPTURE_KEYBOARD = 8

CONFIG_NONE = 0

CONFIG_NO_MOUSE = 16

CONFIG_NO_MOUSE_CURSOR_CHANGE = 32

DATA_TYPE_DOUBLE = 9
DATA_TYPE_FLOAT = 8
DATA_TYPE_S16 = 2
DATA_TYPE_S32 = 4
DATA_TYPE_S64 = 6
DATA_TYPE_S8 = 0
DATA_TYPE_U16 = 3
DATA_TYPE_U32 = 5
DATA_TYPE_U64 = 7
DATA_TYPE_U8 = 1

DIRECTION_DOWN = 3
DIRECTION_LEFT = 0
DIRECTION_NONE = -1
DIRECTION_RIGHT = 1
DIRECTION_UP = 2

DRAG_DROP_ACCEPT_BEFORE_DELIVERY = 1024

DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT = 2048

DRAG_DROP_ACCEPT_NO_PREVIEW_TOOLTIP = 4096

DRAG_DROP_ACCEPT_PEEK_ONLY = 3072

DRAG_DROP_NONE = 0

DRAG_DROP_SOURCE_ALLOW_NULL_ID = 8

DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD = 32

DRAG_DROP_SOURCE_EXTERN = 16

DRAG_DROP_SOURCE_NO_DISABLE_HOVER = 2

DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS = 4

DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP = 1

DRAW_CLOSED = 1

DRAW_CORNER_ALL = 240
DRAW_CORNER_BOTTOM = 192

DRAW_CORNER_BOTTOM_LEFT = 64
DRAW_CORNER_BOTTOM_RIGHT = 128

DRAW_CORNER_LEFT = 80
DRAW_CORNER_NONE = 256
DRAW_CORNER_RIGHT = 160
DRAW_CORNER_TOP = 48

DRAW_CORNER_TOP_LEFT = 16
DRAW_CORNER_TOP_RIGHT = 32

DRAW_LIST_ALLOW_VTX_OFFSET = 8

DRAW_LIST_ANTI_ALIASED_FILL = 4
DRAW_LIST_ANTI_ALIASED_LINES = 1

DRAW_LIST_ANTI_ALIASED_LINES_USE_TEX = 2

DRAW_LIST_NONE = 0

DRAW_NONE = 0

DRAW_ROUND_CORNERS_ALL = 240
DRAW_ROUND_CORNERS_BOTTOM = 192

DRAW_ROUND_CORNERS_BOTTOM_LEFT = 64
DRAW_ROUND_CORNERS_BOTTOM_RIGHT = 128

DRAW_ROUND_CORNERS_LEFT = 80
DRAW_ROUND_CORNERS_NONE = 256
DRAW_ROUND_CORNERS_RIGHT = 160
DRAW_ROUND_CORNERS_TOP = 48

DRAW_ROUND_CORNERS_TOP_LEFT = 16
DRAW_ROUND_CORNERS_TOP_RIGHT = 32

FIRST_USE_EVER = 4

MAX : float= 3.4028234663852886e+38
MIN : float= 1.1754943508222875e-38

FOCUS_ANY_WINDOW = 4

FOCUS_CHILD_WINDOWS = 1

FOCUS_NONE = 0

FOCUS_ROOT_AND_CHILD_WINDOWS = 3

FOCUS_ROOT_WINDOW = 2

FONT_ATLAS_NONE = 0

FONT_ATLAS_NO_BAKED_LINES = 4

FONT_ATLAS_NO_MOUSE_CURSOR = 2

FONT_ATLAS_NO_POWER_OF_TWO_HEIGHT = 1

HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM = 32

HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP = 8

HOVERED_ALLOW_WHEN_DISABLED = 128
HOVERED_ALLOW_WHEN_OVERLAPPED = 64

HOVERED_ANY_WINDOW = 4

HOVERED_CHILD_WINDOWS = 1

HOVERED_NONE = 0

HOVERED_RECT_ONLY = 104

HOVERED_ROOT_AND_CHILD_WINDOWS = 3

HOVERED_ROOT_WINDOW = 2

INPUT_TEXT_ALLOW_TAB_INPUT = 1024

INPUT_TEXT_ALWAYS_INSERT_MODE = 8192

INPUT_TEXT_ALWAYS_OVERWRITE = 8192

INPUT_TEXT_AUTO_SELECT_ALL = 16

INPUT_TEXT_CALLBACK_ALWAYS = 256

INPUT_TEXT_CALLBACK_CHAR_FILTER = 512

INPUT_TEXT_CALLBACK_COMPLETION = 64
INPUT_TEXT_CALLBACK_EDIT = 524288
INPUT_TEXT_CALLBACK_HISTORY = 128
INPUT_TEXT_CALLBACK_RESIZE = 262144

INPUT_TEXT_CHARS_DECIMAL = 1
INPUT_TEXT_CHARS_HEXADECIMAL = 2

INPUT_TEXT_CHARS_NO_BLANK = 8

INPUT_TEXT_CHARS_SCIENTIFIC = 131072
INPUT_TEXT_CHARS_UPPERCASE = 4

INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE = 2048

INPUT_TEXT_ENTER_RETURNS_TRUE = 32

INPUT_TEXT_NONE = 0

INPUT_TEXT_NO_HORIZONTAL_SCROLL = 4096

INPUT_TEXT_NO_UNDO_REDO = 65536

INPUT_TEXT_PASSWORD = 32768

INPUT_TEXT_READ_ONLY = 16384

KEY_A = 16
KEY_BACKSPACE = 11
KEY_C = 17
KEY_DELETE = 10

KEY_DOWN_ARROW = 4

KEY_END = 8
KEY_ENTER = 13
KEY_ESCAPE = 14
KEY_HOME = 7
KEY_INSERT = 9

KEY_LEFT_ARROW = 1

KEY_MOD_ALT = 4
KEY_MOD_CTRL = 1
KEY_MOD_NONE = 0
KEY_MOD_SHIFT = 2
KEY_MOD_SUPER = 8

KEY_PAD_ENTER = 15

KEY_PAGE_DOWN = 6
KEY_PAGE_UP = 5

KEY_RIGHT_ARROW = 2

KEY_SPACE = 12
KEY_TAB = 0

KEY_UP_ARROW = 3

KEY_V = 18
KEY_X = 19
KEY_Y = 20
KEY_Z = 21

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 2
MOUSE_BUTTON_RIGHT = 1

MOUSE_CURSOR_ARROW = 0
MOUSE_CURSOR_HAND = 7
MOUSE_CURSOR_NONE = -1

MOUSE_CURSOR_NOT_ALLOWED = 8

MOUSE_CURSOR_RESIZE_ALL = 2
MOUSE_CURSOR_RESIZE_EW = 4
MOUSE_CURSOR_RESIZE_NESW = 5
MOUSE_CURSOR_RESIZE_NS = 3
MOUSE_CURSOR_RESIZE_NWSE = 6

MOUSE_CURSOR_TEXT_INPUT = 1

NAV_INPUT_ACTIVATE = 0
NAV_INPUT_CANCEL = 1
NAV_INPUT_COUNT = 21

NAV_INPUT_DPAD_DOWN = 7
NAV_INPUT_DPAD_LEFT = 4
NAV_INPUT_DPAD_RIGHT = 5
NAV_INPUT_DPAD_UP = 6

NAV_INPUT_FOCUS_NEXT = 13
NAV_INPUT_FOCUS_PREV = 12

NAV_INPUT_INPUT = 2

NAV_INPUT_L_STICK_DOWN = 11
NAV_INPUT_L_STICK_LEFT = 8
NAV_INPUT_L_STICK_RIGHT = 9
NAV_INPUT_L_STICK_UP = 10

NAV_INPUT_MENU = 3

NAV_INPUT_TWEAK_FAST = 15
NAV_INPUT_TWEAK_SLOW = 14

NONE = 0

ONCE = 2

POPUP_ANY_POPUP = 384

POPUP_ANY_POPUP_ID = 128
POPUP_ANY_POPUP_LEVEL = 256

POPUP_MOUSE_BUTTON_DEFAULT = 1
POPUP_MOUSE_BUTTON_LEFT = 0
POPUP_MOUSE_BUTTON_MASK = 31
POPUP_MOUSE_BUTTON_MIDDLE = 2
POPUP_MOUSE_BUTTON_RIGHT = 1

POPUP_NONE = 0

POPUP_NO_OPEN_OVER_EXISTING_POPUP = 32

POPUP_NO_OPEN_OVER_ITEMS = 64

SELECTABLE_ALLOW_DOUBLE_CLICK = 4

SELECTABLE_ALLOW_ITEM_OVERLAP = 16

SELECTABLE_DISABLED = 8

SELECTABLE_DONT_CLOSE_POPUPS = 1

SELECTABLE_NONE = 0

SELECTABLE_SPAN_ALL_COLUMNS = 2

SLIDER_FLAGS_ALWAYS_CLAMP = 16

SLIDER_FLAGS_LOGARITHMIC = 32
SLIDER_FLAGS_NONE = 0

SLIDER_FLAGS_NO_INPUT = 128

SLIDER_FLAGS_NO_ROUND_TO_FORMAT = 64

SORT_DIRECTION_ASCENDING = 1
SORT_DIRECTION_DESCENDING = 2
SORT_DIRECTION_NONE = 0

STYLE_ALPHA = 0

STYLE_BUTTON_TEXT_ALIGN = 22

STYLE_CELL_PADDING = 16

STYLE_CHILD_BORDERSIZE = 7
STYLE_CHILD_ROUNDING = 6

STYLE_FRAME_BORDERSIZE = 12
STYLE_FRAME_PADDING = 10
STYLE_FRAME_ROUNDING = 11

STYLE_GRAB_MIN_SIZE = 19

STYLE_GRAB_ROUNDING = 20

STYLE_INDENT_SPACING = 15

STYLE_ITEM_INNER_SPACING = 14

STYLE_ITEM_SPACING = 13

STYLE_POPUP_BORDERSIZE = 9
STYLE_POPUP_ROUNDING = 8

STYLE_SCROLLBAR_ROUNDING = 18
STYLE_SCROLLBAR_SIZE = 17

STYLE_SELECTABLE_TEXT_ALIGN = 23

STYLE_TAB_ROUNDING = 21

STYLE_WINDOW_BORDERSIZE = 3

STYLE_WINDOW_MIN_SIZE = 4

STYLE_WINDOW_PADDING = 1
STYLE_WINDOW_ROUNDING = 2

STYLE_WINDOW_TITLE_ALIGN = 5

TABLE_BACKGROUND_TARGET_CELL_BG = 3

TABLE_BACKGROUND_TARGET_NONE = 0

TABLE_BACKGROUND_TARGET_ROW_BG0 = 1
TABLE_BACKGROUND_TARGET_ROW_BG1 = 2

TABLE_BORDERS = 1920

TABLE_BORDERS_HORIZONTAL = 384
TABLE_BORDERS_INNER = 640

TABLE_BORDERS_INNER_HORIZONTAL = 128
TABLE_BORDERS_INNER_VERTICAL = 512

TABLE_BORDERS_OUTER = 1280

TABLE_BORDERS_OUTER_HORIZONTAL = 256
TABLE_BORDERS_OUTER_VERTICAL = 1024

TABLE_BORDERS_VERTICAL = 1536

TABLE_COLUMN_DEFAULT_HIDE = 1
TABLE_COLUMN_DEFAULT_SORT = 2

TABLE_COLUMN_INDENT_DISABLE = 32768
TABLE_COLUMN_INDENT_ENABLE = 16384

TABLE_COLUMN_IS_ENABLED = 1048576
TABLE_COLUMN_IS_HOVERED = 8388608
TABLE_COLUMN_IS_SORTED = 4194304
TABLE_COLUMN_IS_VISIBLE = 2097152

TABLE_COLUMN_NONE = 0

TABLE_COLUMN_NO_CLIP = 128

TABLE_COLUMN_NO_HEADER_WIDTH = 2048

TABLE_COLUMN_NO_HIDE = 64
TABLE_COLUMN_NO_REORDER = 32
TABLE_COLUMN_NO_RESIZE = 16
TABLE_COLUMN_NO_SORT = 256

TABLE_COLUMN_NO_SORT_ASCENDING = 512
TABLE_COLUMN_NO_SORT_DESCENDING = 1024

TABLE_COLUMN_PREFER_SORT_ASCENDING = 4096
TABLE_COLUMN_PREFER_SORT_DESCENDING = 8192

TABLE_COLUMN_WIDTH_FIXED = 8
TABLE_COLUMN_WIDTH_STRETCH = 4

TABLE_CONTEXT_MENU_IN_BODY = 32

TABLE_HIDEABLE = 4
TABLE_NONE = 0

TABLE_NO_BORDERS_IN_BODY = 2048

TABLE_NO_BORDERS_IN_BODY_UTIL_RESIZE = 4096

TABLE_NO_CLIP = 1048576

TABLE_NO_HOST_EXTEND_X = 65536
TABLE_NO_HOST_EXTEND_Y = 131072

TABLE_NO_KEEP_COLUMNS_VISIBLE = 262144

TABLE_NO_PAD_INNER_X = 8388608

TABLE_NO_PAD_OUTER_X = 4194304

TABLE_NO_SAVED_SETTINGS = 16

TABLE_PAD_OUTER_X = 2097152

TABLE_PRECISE_WIDTHS = 524288

TABLE_REORDERABLE = 2
TABLE_RESIZABLE = 1

TABLE_ROW_BACKGROUND = 64
TABLE_ROW_HEADERS = 1
TABLE_ROW_NONE = 0

TABLE_SCROLL_X = 16777216
TABLE_SCROLL_Y = 33554432

TABLE_SIZING_FIXED_FIT = 8192
TABLE_SIZING_FIXED_SAME = 16384

TABLE_SIZING_STRETCH_PROP = 24576
TABLE_SIZING_STRETCH_SAME = 32768

TABLE_SORTABLE = 8

TABLE_SORT_MULTI = 67108864
TABLE_SORT_TRISTATE = 134217728

TAB_BAR_AUTO_SELECT_NEW_TABS = 2

TAB_BAR_FITTING_POLICY_DEFAULT = 64
TAB_BAR_FITTING_POLICY_MASK = 192

TAB_BAR_FITTING_POLICY_RESIZE_DOWN = 64

TAB_BAR_FITTING_POLICY_SCROLL = 128

TAB_BAR_NONE = 0

TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON = 8

TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS = 16

TAB_BAR_NO_TOOLTIP = 32

TAB_BAR_REORDERABLE = 1

TAB_BAR_TAB_LIST_POPUP_BUTTON = 4

TAB_ITEM_LEADING = 64
TAB_ITEM_NONE = 0

TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON = 4

TAB_ITEM_NO_PUSH_ID = 8

TAB_ITEM_NO_REORDER = 32
TAB_ITEM_NO_TOOLTIP = 16

TAB_ITEM_SET_SELECTED = 2

TAB_ITEM_TRAILING = 128

TAB_ITEM_UNSAVED_DOCUMENT = 1

TREE_NODE_ALLOW_ITEM_OVERLAP = 4

TREE_NODE_BULLET = 512

TREE_NODE_COLLAPSING_HEADER = 26

TREE_NODE_DEFAULT_OPEN = 32

TREE_NODE_FRAMED = 2

TREE_NODE_FRAME_PADDING = 1024

TREE_NODE_LEAF = 256

TREE_NODE_NAV_LEFT_JUPS_BACK_HERE = 8192

TREE_NODE_NONE = 0

TREE_NODE_NO_AUTO_OPEN_ON_LOG = 16

TREE_NODE_NO_TREE_PUSH_ON_OPEN = 8

TREE_NODE_OPEN_ON_ARROW = 128

TREE_NODE_OPEN_ON_DOUBLE_CLICK = 64

TREE_NODE_SELECTED = 1

TREE_NODE_SPAN_AVAILABLE_WIDTH = 2048

TREE_NODE_SPAN_FULL_WIDTH = 4096

VIEWPORT_FLAGS_IS_PLATFORM_MONITOR = 2
VIEWPORT_FLAGS_IS_PLATFORM_WINDOW = 1

VIEWPORT_FLAGS_NONE = 0

VIEWPORT_FLAGS_OWNED_BY_APP = 4

WINDOW_ALWAYS_AUTO_RESIZE = 64

WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR = 32768

WINDOW_ALWAYS_USE_WINDOW_PADDING = 65536

WINDOW_ALWAYS_VERTICAL_SCROLLBAR = 16384

WINDOW_HORIZONTAL_SCROLLING_BAR = 2048

WINDOW_MENU_BAR = 1024

WINDOW_NONE = 0

WINDOW_NO_BACKGROUND = 128

WINDOW_NO_BRING_TO_FRONT_ON_FOCUS = 8192

WINDOW_NO_COLLAPSE = 32
WINDOW_NO_DECORATION = 43

WINDOW_NO_FOCUS_ON_APPEARING = 4096

WINDOW_NO_INPUTS = 786944

WINDOW_NO_MOUSE_INPUTS = 512

WINDOW_NO_MOVE = 4
WINDOW_NO_NAV = 786432

WINDOW_NO_NAV_FOCUS = 524288
WINDOW_NO_NAV_INPUTS = 262144

WINDOW_NO_RESIZE = 2

WINDOW_NO_SAVED_SETTINGS = 256

WINDOW_NO_SCROLLBAR = 8

WINDOW_NO_SCROLL_WITH_MOUSE = 16

WINDOW_NO_TITLE_BAR = 1

WINDOW_UNSAVED_DOCUMENT = 1048576

# functions

def accept_drag_drop_payload(type: str, ImGuiDragDropFlags_flags=0): # real signature unknown; restored from __doc__
    """
    accept_drag_drop_payload(str type, ImGuiDragDropFlags flags=0)
    Get the drag and drop payload. Only call after :func:`begin_drag_drop_target`
        returns True.
    
        **Note:** this is a beta API.
    
        For a complete example see :func:`begin_drag_drop_source`.
    
        Args:
            type (str): user defined type with maximum 32 bytes.
            flags (ImGuiDragDropFlags): DragDrop flags.
    
        Returns:
            bytes: the payload data that was set by :func:`set_drag_drop_payload`.
    
        .. wraps::
            const ImGuiPayload* AcceptDragDropPayload(const char* type, ImGuiDragDropFlags flags = 0)
    """
    pass

def align_text_to_frame_padding(): # real signature unknown; restored from __doc__
    """ align_text_to_frame_padding() """
    pass

def arrow_button(label: str, ImGuiDir_direction=None): # real signature unknown; restored from __doc__
    """
    arrow_button(str label, ImGuiDir direction=DIRECTION_NONE)
    Display an arrow button
    
        .. visual-example::
            :auto_layout:
            :height: 100
    
            imgui.begin("Arrow button")
            imgui.arrow_button("Button", imgui.DIRECTION_LEFT)
            imgui.end()
    
        Args:
            label (str): button label.
            direction = imgui direction constant
    
        Returns:
            bool: True if clicked.
    
        .. wraps::
            bool ArrowButton(const char*, ImGuiDir)
    """
    pass

def begin(label: str, closable=False, flags=0): # real signature unknown; restored from __doc__
    """
    begin(str label, closable=False, ImGuiWindowFlags flags=0)
    Begin a window.
    
        .. visual-example::
            :auto_layout:
    
            with imgui.begin("Example: empty window"):
                pass
    
        Example::
            imgui.begin("Example: empty window")
            imgui.end()
    
        Args:
            label (str): label of the window.
            closable (bool): define if window is closable.
            flags: Window flags. See:
                :ref:`list of available flags <window-flag-options>`.
    
        Returns:
            _BeginEnd: ``(expanded, opened)`` struct of bools. If window is collapsed
            ``expanded==True``. The value of ``opened`` is always True for
            non-closable and open windows but changes state to False on close
            button click for closable windows. Use with ``with`` to automatically call
            :func:`end` when the block ends.
    
        .. wraps::
            Begin(
                const char* name,
                bool* p_open = NULL,
                ImGuiWindowFlags flags = 0
            )
    """
    pass

def begin_child(label: str , width: float = 0, height: float = 0, border: bool = False, flags=None): # real signature unknown; restored from __doc__
    """
    begin_child(signatures, args, kwargs, defaults)
    Begin a scrolling region.
    
        **Note:** sizing of child region allows for three modes:
        * ``0.0`` - use remaining window size
        * ``>0.0`` - fixed size
        * ``<0.0`` - use remaining window size minus abs(size)
    
        .. visual-example::
            :width: 200
            :height: 200
            :auto_layout:
    
            with imgui.begin("Example: child region"):
                with imgui.begin_child("region", 150, -50, border=True):
                    imgui.text("inside region")
                imgui.text("outside region")
    
        Example::
            imgui.begin("Example: child region")
    
            imgui.begin_child("region", 150, -50, border=True)
            imgui.text("inside region")
            imgui.end_child()
    
            imgui.text("outside region")
            imgui.end()
    
        Args:
            label (str or int): Child region identifier.
            width (float): Region width. See note about sizing.
            height (float): Region height. See note about sizing.
            border (bool): True if should display border. Defaults to False.
            flags: Window flags. See:
                :ref:`list of available flags <window-flag-options>`.
    
        Returns:
            _BeginEndChild: Struct with ``visible`` bool attribute. Use with ``with``
            to automatically call :func:`end_child` when the block ends.`
    
        .. wraps::
            bool BeginChild(
                const char* id: str,
                const ImVec2& size = ImVec2(0,0),
                bool border = false,
                ImGuiWindowFlags flags = 0
            )
    
            bool BeginChild(
                ImGuiID id,
                const ImVec2& size = ImVec2(0,0),
                bool border = false,
                ImGuiWindowFlags flags = 0
            )
    """
    pass

def begin_combo(label: str, preview_value: str, ImGuiComboFlags_flags=0): # real signature unknown; restored from __doc__
    """
    begin_combo(str label, str preview_value, ImGuiComboFlags flags=0)
    Begin a combo box with control over how items are displayed.
    
        .. visual-example::
            :width: 200
            :height: 200
            :auto_layout:
    
            selected = 0
            items = ["AAAA", "BBBB", "CCCC", "DDDD"]
            
            # ...
            
            with imgui.begin("Example: begin combo"):
                with imgui.begin_combo("combo", items[selected]) as combo:
                    if combo.opened:
                        for i, item in enumerate(items):
                            is_selected = (i == selected)
                            if imgui.selectable(item, is_selected)[0]:
                                selected = i
    
                            # Set the initial focus when opening the combo (scrolling + keyboard navigation focus)
                            if is_selected:
                                imgui.set_item_default_focus()
        
        Example::
        
            selected = 0
            items = ["AAAA", "BBBB", "CCCC", "DDDD"]
            
            # ...
    
            imgui.begin("Example: begin combo")
            if imgui.begin_combo("combo", items[selected]):
                for i, item in enumerate(items):
                    is_selected = (i == selected)
                    if imgui.selectable(item, is_selected)[0]:
                        selected = i
                        
                    # Set the initial focus when opening the combo (scrolling + keyboard navigation focus)                    
                    if is_selected:
                        imgui.set_item_default_focus()
    
                imgui.end_combo()
    
            imgui.end()
    
        Args:
            label (str): Identifier for the combo box.
            preview_value (str): String preview for currently selected item.
            flags: Combo flags. See:
                :ref:`list of available flags <combo-flag-options>`.
    
        Returns:
            _BeginEndCombo: Struct with ``opened`` bool attribute. Use with ``with`` to automatically call :func:`end_combo` when the block ends.`
    
        .. wraps::
            bool BeginCombo(
                const char* label,
                const char* preview_value,
                ImGuiComboFlags flags = 0
            )
    """
    pass

def begin_drag_drop_source(ImGuiDragDropFlags_flags=0): # real signature unknown; restored from __doc__
    """
    begin_drag_drop_source(ImGuiDragDropFlags flags=0)
    Set the current item as a drag and drop source. If ``dragging`` is True, you
        can call :func:`set_drag_drop_payload` and :func:`end_drag_drop_source`.
        Use with ``with`` to automatically call :func:`end_drag_drop_source` if necessary.
    
        **Note:** this is a beta API.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            with imgui.begin("Example: drag and drop"):
    
                imgui.button('source')
                with imgui.begin_drag_drop_source() as drag_drop_src:
                    if drag_drop_src.dragging:
                        imgui.set_drag_drop_payload('itemtype', b'payload')
                        imgui.button('dragged source')
    
                imgui.button('dest')
                with imgui.begin_drag_drop_target() as drag_drop_dst:
                    if drag_drop_dst.hovered:
                        payload = imgui.accept_drag_drop_payload('itemtype')
                        if payload is not None:
                            print('Received:', payload)
    
        Example::
    
            imgui.begin("Example: drag and drop")
    
            imgui.button('source')
            if imgui.begin_drag_drop_source():
                imgui.set_drag_drop_payload('itemtype', b'payload')
                imgui.button('dragged source')
                imgui.end_drag_drop_source()
    
            imgui.button('dest')
            if imgui.begin_drag_drop_target():
                payload = imgui.accept_drag_drop_payload('itemtype')
                if payload is not None:
                    print('Received:', payload)
                imgui.end_drag_drop_target()
    
            imgui.end()
    
        Args:
            flags (ImGuiDragDropFlags): DragDrop flags.
    
        Returns:
            _BeginEndDragDropSource: Use ``dragging`` to tell if a drag starting at this source is occurring.
            Only call :func:`end_drag_drop_source` if ``dragging`` is True.
            Use with ``with`` to automatically call :func:`end_drag_drop_source` if necessary when the block ends.
    
        .. wraps::
            bool BeginDragDropSource(ImGuiDragDropFlags flags = 0)
    """
    pass

def begin_drag_drop_target(): # real signature unknown; restored from __doc__
    """
    begin_drag_drop_target()
    Set the current item as a drag and drop target. If ``hovered`` is True, you
        can call :func:`accept_drag_drop_payload` and :func:`end_drag_drop_target`.
        Use with ``with`` to automatically call :func:`end_drag_drop_target` if necessary.
    
        For a complete example see :func:`begin_drag_drop_source`.
    
        **Note:** this is a beta API.
    
        Returns:
            _BeginEndDragDropTarget: Use ``hovered` to tell if a drag hovers over the target.
            Only call :func:`end_drag_drop_target` if ``hovered`` is True.
            Use with ``with`` to automatically call :func:`end_drag_drop_target` if necessary when the block ends.
    
        .. wraps::
            bool BeginDragDropTarget()
    """
    pass

def begin_group(): # real signature unknown; restored from __doc__
    """
    begin_group()
    Start item group and lock its horizontal starting position.
    
        Captures group bounding box into one "item". Thanks to this you can use
        :any:`is_item_hovered()` or layout primitives such as :any:`same_line()`
        on whole group, etc.
    
        .. visual-example::
            :auto_layout:
            :width: 500
    
            with imgui.begin("Example: item groups"):
    
                with imgui.begin_group():
                    imgui.text("First group (buttons):")
                    imgui.button("Button A")
                    imgui.button("Button B")
    
                imgui.same_line(spacing=50)
    
                with imgui.begin_group():
                    imgui.text("Second group (text and bullet texts):")
                    imgui.bullet_text("Bullet A")
                    imgui.bullet_text("Bullet B")
    
        Example::
    
            imgui.begin("Example: item groups")
    
            imgui.begin_group()
            imgui.text("First group (buttons):")
            imgui.button("Button A")
            imgui.button("Button B")
            imgui.end_group()
    
            imgui.same_line(spacing=50)
    
            imgui.begin_group()
            imgui.text("Second group (text and bullet texts):")
            imgui.bullet_text("Bullet A")
            imgui.bullet_text("Bullet B")
            imgui.end_group()
    
            imgui.end()
    
        Returns:
            _BeginEndGrouop; use with ``with`` to automatically call :func:`end_group` when the block ends.
    
        .. wraps::
            void BeginGroup()
    """
    pass

def begin_list_box(label: str, width=0, height=0): # real signature unknown; restored from __doc__
    """
    begin_list_box(str label, width=0, height=0)
    Open a framed scrolling region.
    
        For use if you want to reimplement :func:`listbox` with custom data
        or interactions. You need to call :func:`end_list_box` at the end
        if ``opened`` is True, or use ``with`` to do so automatically.
    
        .. visual-example::
            :auto_layout:
            :height: 200
            :width: 200
            :click: 80 40
    
            with imgui.begin("Example: custom listbox"):
                with imgui.begin_list_box("List", 200, 100) as list_box:
                    if list_box.opened:
                        imgui.selectable("Selected", True)
                        imgui.selectable("Not Selected", False)
    
        Example::
            imgui.begin("Example: custom listbox")
    
            if imgui.begin_list_box("List", 200, 100).opened:
    
                imgui.selectable("Selected", True)
                imgui.selectable("Not Selected", False)
    
                imgui.end_list_box()
    
            imgui.end()
    
        Args:
            label (str): The label.
            width (float): Button width. w > 0.0f: custom; w < 0.0f or -FLT_MIN: right-align; w = 0.0f (default): use current ItemWidth
            height (float): Button height. h > 0.0f: custom; h < 0.0f or -FLT_MIN: bottom-align; h = 0.0f (default): arbitrary default height which can fit ~7 items
    
        Returns:
            _BeginEndListBox: Use ``opened`` bool attribute to tell if the item is opened or closed.
            Only call :func:`end_list_box` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_list_box` if necessary when the block ends.
    
        .. wraps::
            bool BeginListBox(
                const char* label,
                const ImVec2& size = ImVec2(0,0)
            )
    """
    pass

def begin_main_menu_bar(): # real signature unknown; restored from __doc__
    """
    begin_main_menu_bar()
    Create new full-screen menu bar.
    
        Use with ``with`` to automatically call :func:`end_main_menu_bar` if necessary.
        Otherwise, only call :func:`end_main_menu_bar` if ``opened`` is True.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
            :click: 10 10
    
            with imgui.begin_main_menu_bar() as main_menu_bar:
                if main_menu_bar.opened:
                    # first menu dropdown
                    with imgui.begin_menu('File', True) as file_menu:
                        if file_menu.opened:
                            imgui.menu_item('New', 'Ctrl+N', False, True)
                            imgui.menu_item('Open ...', 'Ctrl+O', False, True)
    
                            # submenu
                            with imgui.begin_menu('Open Recent', True) as open_recent_menu:
                                if open_recent_menu.opened:
                                    imgui.menu_item('doc.txt', None, False, True)
    
        Example::
    
            if imgui.begin_main_menu_bar().opened:
                # first menu dropdown
                if imgui.begin_menu('File', True).opened:
                    imgui.menu_item('New', 'Ctrl+N', False, True)
                    imgui.menu_item('Open ...', 'Ctrl+O', False, True)
    
                    # submenu
                    if imgui.begin_menu('Open Recent', True).opened:
                        imgui.menu_item('doc.txt', None, False, True)
                        imgui.end_menu()
    
                    imgui.end_menu()
    
                imgui.end_main_menu_bar()
    
        Returns:
            _BeginEndMainMenuBar: Use ``opened`` to tell if main menu bar is displayed (opened).
            Only call :func:`end_main_menu_bar` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_main_menu_bar` if necessary when the block ends.
    
        .. wraps::
            bool BeginMainMenuBar()
    """
    pass

def begin_menu(label: str, enabled=True): # real signature unknown; restored from __doc__
    """
    begin_menu(str label, enabled=True)
    Create new expandable menu in current menu bar.
    
        Use with ``with`` to automatically call :func:`end_menu` if necessary.
        Otherwise, only call :func:`end_menu` if ``opened`` is True.
    
        For practical example how to use this function, please see documentation
        of :func:`begin_main_menu_bar` or :func:`begin_menu_bar`.
    
        Args:
            label (str): label of the menu.
            enabled (bool): define if menu is enabled or disabled.
    
        Returns:
            _BeginEndMenu: Use ``opened`` to tell if the menu is displayed (opened).
            Only call :func:`end_menu` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_menu` if necessary when the block ends.
    
        .. wraps::
            bool BeginMenu(
                const char* label,
                bool enabled
            )
    """
    pass

def begin_menu_bar(): # real signature unknown; restored from __doc__
    """
    begin_menu_bar()
    Append new menu menu bar to current window.
    
        This function is different from :func:`begin_main_menu_bar`, as this is
        child-window specific. Use with ``with`` to automatically call
        :func:`end_menu_bar` if necessary.
        Otherwise, only call :func:`end_menu_bar` if ``opened`` is True.
    
        **Note:** this requires :ref:`WINDOW_MENU_BAR <window-flag-options>` flag
        to be set for the current window. Without this flag set the
        ``begin_menu_bar()`` function will always return ``False``.
    
        .. visual-example::
            :auto_layout:
            :click: 25 30
    
            flags = imgui.WINDOW_MENU_BAR
    
            with imgui.begin("Child Window - File Browser", flags=flags):
                with imgui.begin_menu_bar() as menu_bar:
                    if menu_bar.opened:
                        with imgui.begin_menu('File') as file_menu:
                            if file_menu.opened:
                                imgui.menu_item('Close')
    
        Example::
    
            flags = imgui.WINDOW_MENU_BAR
    
            imgui.begin("Child Window - File Browser", flags=flags)
    
            if imgui.begin_menu_bar().opened:
                if imgui.begin_menu('File').opened:
                    imgui.menu_item('Close')
                    imgui.end_menu()
    
                imgui.end_menu_bar()
    
            imgui.end()
    
        Returns:
            _BeginEndMenuBar: Use ``opened`` to tell if menu bar is displayed (opened).
            Only call :func:`end_menu_bar` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_menu_bar` if necessary when the block ends.
    
        .. wraps::
            bool BeginMenuBar()
    """
    pass

def begin_popup(label: str, ImGuiWindowFlags_flags=0): # real signature unknown; restored from __doc__
    """
    begin_popup(str label, ImGuiWindowFlags flags=0)
    Open a popup window.
    
        The attribute ``opened`` is True if the popup is open and you can start outputting
        content to it.
        Use with ``with`` to automatically call :func:`end_popup` if necessary.
        Otherwise, only call :func:`end_popup` if ``opened`` is True.
    
        .. visual-example::
            :title: Simple popup window
            :height: 100
            :width: 220
            :auto_layout:
    
            with imgui.begin("Example: simple popup"):
                if imgui.button("select"):
                    imgui.open_popup("select-popup")
    
                imgui.same_line()
    
                with imgui.begin_popup("select-popup") as select_popup:
                    if select_popup.opened:
                        imgui.text("Select one")
                        imgui.separator()
                        imgui.selectable("One")
                        imgui.selectable("Two")
                        imgui.selectable("Three")
    
        Example::
    
            imgui.begin("Example: simple popup")
    
            if imgui.button("select"):
                imgui.open_popup("select-popup")
    
            imgui.same_line()
    
            if imgui.begin_popup("select-popup"):
                imgui.text("Select one")
                imgui.separator()
                imgui.selectable("One")
                imgui.selectable("Two")
                imgui.selectable("Three")
                imgui.end_popup()
    
            imgui.end()
    
        Args:
            label (str): label of the modal window.
    
        Returns:
            _BeginEndPopup: Use ``opened`` bool attribute to tell if the popup is opened.
            Only call :func:`end_popup` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.
    
        .. wraps::
            bool BeginPopup(
                const char* id: str,
                ImGuiWindowFlags flags = 0
            )
    """
    pass

def begin_popup_context_item(label: Optional[str]=None, ImGuiPopupFlags_mouse_button=1): # real signature unknown; restored from __doc__
    """
    begin_popup_context_item(str label=None, ImGuiPopupFlags mouse_button=1)
    This is a helper function to handle the most simple case of associating
        one named popup to one given widget.
    
        .. visual-example::
            :title: Popup context view
            :height: 100
            :width: 200
            :auto_layout:
            :click: 40 40
    
            with imgui.begin("Example: popup context view"):
                imgui.text("Right-click to set value.")
                with imgui.begin_popup_context_item("Item Context Menu", mouse_button=0) as popup:
                    if popup.opened:
                        imgui.selectable("Set to Zero")
    
        Example::
    
            imgui.begin("Example: popup context view")
            imgui.text("Right-click to set value.")
            if imgui.begin_popup_context_item("Item Context Menu", mouse_button=0):
                imgui.selectable("Set to Zero")
                imgui.end_popup()
            imgui.end()
    
        Args:
            label (str): label of item.
            mouse_button: ImGuiPopupFlags
    
        Returns:
            _BeginEndPopup: Use ``opened`` bool attribute to tell if the popup is opened.
            Only call :func:`end_popup` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.
    
        .. wraps::
            bool BeginPopupContextItem(
                const char* id : str= NULL,
                int mouse_button = 1
            )
    """
    pass

def begin_popup_context_void(label: Optional[str]=None, ImGuiPopupFlags_popup_flags=1): # real signature unknown; restored from __doc__
    """
    begin_popup_context_void(str label=None, ImGuiPopupFlags popup_flags=1)
    Open+begin popup when clicked in void (where there are no windows).
    
        Args:
            label (str): label of the window
            popup_flags: ImGuiPopupFlags
    
        Returns:
            _BeginEndPopup: Use ``opened`` bool attribute to tell if the context window is opened.
            Only call :func:`end_popup` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.
    
        .. wraps::
            bool BeginPopupContextVoid(const char* id : str= NULL, ImGuiPopupFlags popup_flags = 1)
    """
    pass

def begin_popup_context_window(label: Optional[str]=None, ImGuiPopupFlags_popup_flags=1, bool_also_over_items=True): # real signature unknown; restored from __doc__
    """
    begin_popup_context_window(str label=None, ImGuiPopupFlags popup_flags=1, bool also_over_items=True)
    Helper function to open and begin popup when clicked on current window.
    
        As all popup functions it should end with :func:`end_popup`.
    
        .. visual-example::
            :title: Popup context view
            :height: 100
            :width: 200
            :auto_layout:
            :click: 40 40
    
            with imgui.begin("Example: popup context window"):
                with imgui.begin_popup_context_window(popup_flags=imgui.POPUP_NONE) as context_window:
                    if context_window.opened:
                        imgui.selectable("Clear")
    
        Example::
    
            imgui.begin("Example: popup context window")
            if imgui.begin_popup_context_window(popup_flags=imgui.POPUP_NONE):
                imgui.selectable("Clear")
                imgui.end_popup()
            imgui.end()
    
        Args:
            label (str): label of the window
            popup_flags: ImGuiPopupFlags
            also_over_items (bool): display on top of widget. OBSOLETED in ImGui 1.77 (from June 2020)
    
        Returns:
            _BeginEndPopup: Use ``opened`` bool attribute to tell if the context window is opened.
            Only call :func:`end_popup` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.
    
        .. wraps::
            bool BeginPopupContextWindow(
                const char* id : str= NULL,
                ImGuiPopupFlags popup_flags = 1
            )
    """
    pass

def begin_popup_modal(title: str, visible=None, flags=0): # real signature unknown; restored from __doc__
    """
    begin_popup_modal(str title, visible=None, ImGuiWindowFlags flags=0)
    Begin pouring popup contents.
    
        Differs from :func:`begin_popup` with its modality - meaning it
        opens up on top of every other window.
    
        The attribute ``opened`` is True if the popup is open and you can start outputting
        content to it.
        Use with ``with`` to automatically call :func:`end_popup` if necessary.
        Otherwise, only call :func:`end_popup` if ``opened`` is True.
    
        .. visual-example::
            :title: Simple popup window
            :height: 100
            :width: 220
            :auto_layout:
    
            with imgui.begin("Example: simple popup modal"):
                if imgui.button("Open Modal popup"):
                    imgui.open_popup("select-popup")
    
                imgui.same_line()
    
                with imgui.begin_popup_modal("select-popup") as select_popup:
                    if select_popup.opened:
                        imgui.text("Select an option:")
                        imgui.separator()
                        imgui.selectable("One")
                        imgui.selectable("Two")
                        imgui.selectable("Three")
    
        Example::
    
            imgui.begin("Example: simple popup modal")
    
            if imgui.button("Open Modal popup"):
                imgui.open_popup("select-popup")
    
            imgui.same_line()
    
            if imgui.begin_popup_modal("select-popup").opened:
                imgui.text("Select an option:")
                imgui.separator()
                imgui.selectable("One")
                imgui.selectable("Two")
                imgui.selectable("Three")
                imgui.end_popup()
    
            imgui.end()
    
        Args:
            title (str): label of the modal window.
            visible (bool): define if popup is visible or not.
            flags: Window flags. See:
                :ref:`list of available flags <window-flag-options>`.
    
        Returns:
            _BeginEndPopupModal: ``(opened, visible)`` struct of bools.
            Only call :func:`end_popup` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.
            The ``opened`` attribute can be False when the popup is completely clipped
            (e.g. zero size display).
    
        .. wraps::
            bool BeginPopupModal(
                const char* name,
                bool* p_open = NULL,
                ImGuiWindowFlags extra_flags = 0
            )
    """
    pass

def begin_table(label: str, column: int, ImGuiTableFlags_flags=0, outer_size_width: float=0.0, outer_size_height: float=0.0, inner_width: float=0.0): # real signature unknown; restored from __doc__
    """
    begin_table(str label, int column, ImGuiTableFlags flags=0, float outer_size_width=0.0, float outer_size_height=0.0, float inner_width=0.0)
    
    
        Returns:
            _BeginEndPopup: Use ``opened`` bool attribute to tell if the table is opened.
            Only call :func:`end_table` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_table` if necessary when the block ends.
    
        .. wraps::
            bool BeginTable(
                const char* id: str,
                int column,
                ImGuiTableFlags flags = 0,
                const ImVec2& outer_size = ImVec2(0.0f, 0.0f),
                float inner_width = 0.0f
            )
    """
    pass

def begin_tab_bar(identifier: str, ImGuiTabBarFlags_flags=0): # real signature unknown; restored from __doc__
    """
    begin_tab_bar(str identifier, ImGuiTabBarFlags flags=0)
    Create and append into a TabBar
    
        Args:
            identifier(str): String identifier of the tab window
            flags: ImGuiTabBarFlags flags. See:
                :ref:`list of available flags <tabbar-flag-options>`.
    
        Returns:
            _BeginEndTabBar: Use ``opened`` bool attribute to tell if the Tab Bar is open.
            Only call :func:`end_tab_bar` if ``opened`` is True.
            Use with ``with`` to automatically call :func:`end_tab_bar` if necessary when the block ends.
    
        .. wraps::
            bool BeginTabBar(const char* id: str, ImGuiTabBarFlags flags = 0)
    """
    pass

def begin_tab_item(label: str, opened=None, ImGuiTabItemFlags_flags=0): # real signature unknown; restored from __doc__
    """
    begin_tab_item(str label, opened=None, ImGuiTabItemFlags flags=0)
    Create a Tab.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            opened_state = True
    
            #...
    
            with imgui.begin("Example Tab Bar"):
                with imgui.begin_tab_bar("MyTabBar") as tab_bar:
                    if tab_bar.opened:
                        with imgui.begin_tab_item("Item 1") as item1:
                            if item1.selected:
                                imgui.text("Here is the tab content!")
    
                        with imgui.begin_tab_item("Item 2") as item2:
                            if item2.selected:
                                imgui.text("Another content...")
    
                        with imgui.begin_tab_item("Item 3", opened=opened_state) as item3:
                            opened_state = item3.opened
                            if item3.selected:
                                imgui.text("Hello Saylor!")
    
        Example::
    
            opened_state = True
    
            #...
    
            imgui.begin("Example Tab Bar")
            if imgui.begin_tab_bar("MyTabBar"):
    
                if imgui.begin_tab_item("Item 1").selected:
                    imgui.text("Here is the tab content!")
                    imgui.end_tab_item()
    
                if imgui.begin_tab_item("Item 2").selected:
                    imgui.text("Another content...")
                    imgui.end_tab_item()
    
                selected, opened_state = imgui.begin_tab_item("Item 3", opened=opened_state)
                if selected:
                    imgui.text("Hello Saylor!")
                    imgui.end_tab_item()
    
                imgui.end_tab_bar()
            imgui.end()
    
        Args:
            label (str): Label of the tab item
            removable (bool): If True, the tab item can be removed
            flags: ImGuiTabItemFlags flags. See:
                :ref:`list of available flags <tabitem-flag-options>`.
    
        Returns:
            _BeginEndTabItem: ``(selected, opened)`` struct of bools. If tab item is selected
            ``selected==True``. The value of ``opened`` is always True for
            non-removable and open tab items but changes state to False on close
            button click for removable tab items.
            Only call :func:`end_tab_item` if ``selected`` is True.
            Use with ``with`` to automatically call :func:`end_tab_item` if necessary when the block ends.
    
        .. wraps::
            bool BeginTabItem(
                const char* label,
                bool* p_open = NULL,
                ImGuiTabItemFlags flags = 0
            )
    """
    pass

def begin_tooltip(): # real signature unknown; restored from __doc__
    """
    begin_tooltip()
    Use to create full-featured tooltip windows that aren't just text.
    
        .. visual-example::
            :auto_layout:
            :width: 600
            :height: 200
            :click: 80 40
    
            with imgui.begin("Example: tooltip"):
                imgui.button("Click me!")
                if imgui.is_item_hovered():
                    with imgui.begin_tooltip():
                        imgui.text("This button is clickable.")
                        imgui.text("This button has full window tooltip.")
                        texture_id = imgui.get_io().fonts.texture_id
                        imgui.image(texture_id, 512, 64, border_color=(1, 0, 0, 1))
        
        .. wraps::
            void BeginTooltip()
        
        Returns:
            _BeginEndTooltip: Use with ``with`` to automatically call :func:`end_tooltip` when the block ends.
    """
    pass

def bullet(): # real signature unknown; restored from __doc__
    """
    bullet()
    Display a small circle and keep the cursor on the same line.
    
        .. advance cursor x position by ``get_tree_node_to_label_spacing()``,
           same distance that TreeNode() uses
    
        .. visual-example::
            :auto_layout:
            :height: 80
    
            imgui.begin("Example: bullets")
    
            for i in range(10):
                imgui.bullet()
    
            imgui.end()
    
        .. wraps::
            void Bullet()
    """
    pass

def bullet_text(text: str): # real signature unknown; restored from __doc__
    """
    bullet_text(str text)
    Display bullet and text.
    
        This is shortcut for:
    
        .. code-block:: python
    
            imgui.bullet()
            imgui.text(text)
    
        .. visual-example::
            :auto_layout:
            :height: 100
    
            imgui.begin("Example: bullet text")
            imgui.bullet_text("Bullet 1")
            imgui.bullet_text("Bullet 2")
            imgui.bullet_text("Bullet 3")
            imgui.end()
    
        Args:
            text (str): text to display.
    
        .. wraps::
            void BulletText(const char* fmt, ...)
    """
    pass

def button(label: str, width=0, height=0): # real signature unknown; restored from __doc__
    """
    button(str label, width=0, height=0)
    Display button.
    
        .. visual-example::
            :auto_layout:
            :height: 100
    
            imgui.begin("Example: button")
            imgui.button("Button 1")
            imgui.button("Button 2")
            imgui.end()
    
        Args:
            label (str): button label.
            width (float): button width.
            height (float): button height.
    
        Returns:
            bool: True if clicked.
    
        .. wraps::
            bool Button(const char* label, const ImVec2& size = ImVec2(0,0))
    """
    pass

def calculate_item_width(): # real signature unknown; restored from __doc__
    """
    calculate_item_width()
    Calculate and return the current item width.
    
        Returns:
            float: calculated item width.
    
        .. wraps::
            float CalcItemWidth()
    """
    pass

def calc_text_size(text: str, bool_hide_text_after_double_hash=False, wrap_width: float=-1.0): # real signature unknown; restored from __doc__
    """
    calc_text_size(str text, bool hide_text_after_double_hash=False, float wrap_width=-1.0)
    Calculate text size.
        Text can be multi-line.
        Optionally ignore text after a ## marker.
    
        .. visual-example::
            :auto_layout:
            :width: 300
            :height: 100
    
            imgui.begin("Text size calculation")
            text_content = "This is a ##text##!"
            text_size1 = imgui.calc_text_size(text_content)
            imgui.text('"%s" has size %ix%i' % (text_content, text_size1[0], text_size1[1]))
            text_size2 = imgui.calc_text_size(text_content, True)
            imgui.text('"%s" has size %ix%i' % (text_content, text_size2[0], text_size2[1]))
            text_size3 = imgui.calc_text_size(text_content, False, 30.0)
            imgui.text('"%s" has size %ix%i' % (text_content, text_size3[0], text_size3[1]))
            imgui.end()
    
        Args:
            text (str): text
            hide_text_after_double_hash (bool): if True, text after '##' is ignored
            wrap_width (float): if > 0.0 calculate size using text wrapping
    
        .. wraps::
            CalcTextSize(const char* text, const char* text_end, bool hide_text_after_double_hash, float wrap_width)
    """
    pass

def capture_mouse_from_app(bool_want_capture_mouse_value=True): # real signature unknown; restored from __doc__
    """
    capture_mouse_from_app(bool want_capture_mouse_value=True)
    Attention: misleading name!
        Manually override io.WantCaptureMouse flag next frame
        (said flag is entirely left for your application to handle).
    
        This is equivalent to setting "io.WantCaptureMouse = want_capture_mouse_value;"
        after the next NewFrame() call.
    
        .. wraps::
            void CaptureMouseFromApp(bool want_capture_mouse_value = true)
    """
    pass

def checkbox(label: str, bool_state): # real signature unknown; restored from __doc__
    """
    checkbox(str label, bool state)
    Display checkbox widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
    
    
            # note: these should be initialized outside of the main interaction
            #       loop
            checkbox1_enabled = True
            checkbox2_enabled = False
    
            imgui.new_frame()
            imgui.begin("Example: checkboxes")
    
            # note: first element of return two-tuple notifies if there was a click
            #       event in currently processed frame and second element is actual
            #       checkbox state.
            _, checkbox1_enabled = imgui.checkbox("Checkbox 1", checkbox1_enabled)
            _, checkbox2_enabled = imgui.checkbox("Checkbox 2", checkbox2_enabled)
    
            imgui.text("Checkbox 1 state value: {}".format(checkbox1_enabled))
            imgui.text("Checkbox 2 state value: {}".format(checkbox2_enabled))
    
            imgui.end()
    
    
        Args:
            label (str): text label for checkbox widget.
            state (bool): current (desired) state of the checkbox. If it has to
                change, the new state will be returned as a second item of
                the return value.
    
        Returns:
            tuple: a ``(clicked, state)`` two-tuple indicating click event and the
            current state of the checkbox.
    
        .. wraps::
            bool Checkbox(const char* label, bool* v)
    """
    pass

def checkbox_flags(label: str, unsigned_flags: int, unsigned_flags_value: int): # real signature unknown; restored from __doc__
    """
    checkbox_flags(str label, unsigned int flags, unsigned int flags_value)
    Display checkbox widget that handle integer flags (bit fields).
    
        It is useful for handling window/style flags or any kind of flags
        implemented as integer bitfields.
    
        .. visual-example::
            :auto_layout:
            :width: 500
    
            flags = imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE
    
            imgui.begin("Example: checkboxes for flags", flags=flags)
    
            clicked, flags = imgui.checkbox_flags(
                "No resize", flags, imgui.WINDOW_NO_RESIZE
            )
            clicked, flags = imgui.checkbox_flags(
                "No move", flags, imgui.WINDOW_NO_MOVE
            )
            clicked, flags = imgui.checkbox_flags(
                "No collapse", flags, imgui.WINDOW_NO_COLLAPSE
            )
            # note: it also allows to use multiple flags at once
            clicked, flags = imgui.checkbox_flags(
                "No resize & no move", flags,
                imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE
            )
            imgui.text("Current flags value: {0:b}".format(flags))
            imgui.end()
    
        Args:
            label (str): text label for checkbox widget.
            flags (int): current state of the flags associated with checkbox.
                Actual state of checkbox (toggled/untoggled) is calculated from
                this argument and ``flags_value`` argument. If it has to change,
                the new state will be returned as a second item of the return
                value.
            flags_value (int): values of flags this widget can toggle. Represents
                bitmask in flags bitfield. Allows multiple flags to be toggled
                at once (specify using bit OR operator `|`, see example above).
    
        Returns:
            tuple: a ``(clicked, flags)`` two-tuple indicating click event and the
            current state of the flags controlled with this checkbox.
    
        .. wraps::
            bool CheckboxFlags(
                const char* label, unsigned int* flags,
                unsigned int flags_value
            )
    """
    pass

def close_current_popup(): # real signature unknown; restored from __doc__
    """
    close_current_popup()
    Close the current popup window begin-ed directly above this call.
        Clicking on a :func:`menu_item()` or :func:`selectable()` automatically
        close the current popup.
    
        For practical example how to use this function, please see documentation
        of :func:`open_popup`.
    
        .. wraps::
            void CloseCurrentPopup()
    """
    pass

def collapsing_header(text: str, visible=None, ImGuiTreeNodeFlags_flags=0): # real signature unknown; restored from __doc__
    """
    collapsing_header(str text, visible=None, ImGuiTreeNodeFlags flags=0)
    Collapsable/Expandable header view.
    
        Returns 'true' if the header is open. Doesn't indent or push to stack,
        so no need to call any pop function.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
            :click: 80 40
    
            visible = True
    
            imgui.begin("Example: collapsing header")
            expanded, visible = imgui.collapsing_header("Expand me!", visible)
    
            if expanded:
                imgui.text("Now you see me!")
            imgui.end()
    
        Args:
            text (str): Tree node label
            visible (bool or None): Force visibility of a header. If set to True
                shows additional (X) close button. If set to False header is not
                visible at all. If set to None header is always visible and close
                button is not displayed.
            flags: TreeNode flags. See:
                :ref:`list of available flags <treenode-flag-options>`.
    
        Returns:
            tuple: a ``(expanded, visible)`` two-tuple indicating if item was
            expanded and whether the header is visible or not (only if ``visible``
            input argument is True/False).
    
        .. wraps::
            bool CollapsingHeader(const char* label, ImGuiTreeNodeFlags flags = 0)
    
            bool CollapsingHeader(
                const char* label,
                bool* p_visible,
                ImGuiTreeNodeFlags flags = 0
            )
    """
    pass

def color_button(desc_id: str, r: float, g: float, b: float, a=1., flags=0, width: float=0, height: float=0): # real signature unknown; restored from __doc__
    """
    color_button(str desc_id, float r, float g, float b, a=1., flags=0, float width=0, float height=0)
    Display colored button.
    
        .. visual-example::
            :auto_layout:
            :height: 150
    
            imgui.begin("Example: color button")
            imgui.color_button("Button 1", 1, 0, 0, 1, 0, 10, 10)
            imgui.color_button("Button 2", 0, 1, 0, 1, 0, 10, 10)
            imgui.color_button("Wide Button", 0, 0, 1, 1, 0, 20, 10)
            imgui.color_button("Tall Button", 1, 0, 1, 1, 0, 10, 20)
            imgui.end()
    
        Args:
            #r (float): red color intensity.
            #g (float): green color intensity.
            #b (float): blue color instensity.
            #a (float): alpha intensity.
            #ImGuiColorEditFlags: Color edit flags.  Zero for none.
            #width (float): Width of the color button
            #height (float): Height of the color button
    
        Returns:
            bool: True if button is clicked.
    
        .. wraps::
            bool ColorButton(
                const char* desc_id,
                const ImVec4& col,
                ImGuiColorEditFlags flags,
                ImVec2 size
            )
    """
    pass

def color_convert_float4_to_u32(r: float, g: float, b: float, a: float): # real signature unknown; restored from __doc__
    """
    color_convert_float4_to_u32(float r, float g, float b, float a)
    Convert a set of r, g, b, a floats to unsigned int 32 color
    
        Args:
            r, g, b, a (float): Components of the color
    
        Returns:
            ImU32: Unsigned int 32 color format
    
        .. wraps::
            ImU32 ColorConvertFloat4ToU32(const ImVec4& in)
    """
    pass

def color_convert_hsv_to_rgb(h: float, s: float, v: float): # real signature unknown; restored from __doc__
    """
    color_convert_hsv_to_rgb(float h, float s, float v)
    Convert color from HSV space to RGB space
    
        Args:
            h, s, v (float): HSV color format
    
        Returns:
            tuple: r, g, b RGB color format
    
        .. wraps::
            void ColorConvertHSVtoRGB(float h, float s, float v, float& out_r, float& out_g, float& out_b)
    """
    pass

def color_convert_rgb_to_hsv(r: float, g: float, b: float): # real signature unknown; restored from __doc__
    """
    color_convert_rgb_to_hsv(float r, float g, float b)
    Convert color from RGB space to HSV space
    
        Args:
            r, g, b (float): RGB color format
    
        Returns:
            tuple: h, s, v HSV color format
    
        .. wraps::
            void ColorConvertRGBtoHSV(float r, float g, float b, float& out_h, float& out_s, float& out_v)
    """
    pass

def color_convert_u32_to_float4(ImU32_in_): # real signature unknown; restored from __doc__
    """
    color_convert_u32_to_float4(ImU32 in_)
    Convert an unsigned int 32 to 4 component r, g, b, a
    
        Args:
            in_ (ImU32): Color in unsigned int 32 format
    
        Return:
            tuple: r, g, b, a components of the color
    
        .. wraps::
            ImVec4 ColorConvertU32ToFloat4(ImU32 in)
    """
    pass

def color_edit3(label: str, r: float, g: float, b: float, ImGuiColorEditFlags_flags=0): # real signature unknown; restored from __doc__
    """
    color_edit3(str label, float r, float g, float b, ImGuiColorEditFlags flags=0)
    Display color edit widget for color without alpha value.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            # note: the variable that contains the color data, should be initialized
            #       outside of the main interaction loop
            color_1 = 1., .0, .5
            color_2 = 0., .8, .3
    
            imgui.begin("Example: color edit without alpha")
    
            # note: first element of return two-tuple notifies if the color was changed
            #       in currently processed frame and second element is current value
            #       of color
            changed, color_1 = imgui.color_edit3("Color 1", *color_1)
            changed, color_2 = imgui.color_edit3("Color 2", *color_2)
    
            imgui.end()
    
        Args:
            label (str): color edit label.
            r (float): red color intensity.
            g (float): green color intensity.
            b (float): blue color instensity.
            flags (ImGuiColorEditFlags): Color edit flags.  Zero for none.
    
        Returns:
            tuple: a ``(bool changed, float color[3])`` tuple that contains indicator of color
            change and current value of color
    
        .. wraps::
            bool ColorEdit3(const char* label, float col[3], ImGuiColorEditFlags flags = 0)
    """
    pass

def color_edit4(label: str, r: float, g: float, b: float, a: float, ImGuiColorEditFlags_flags=0): # real signature unknown; restored from __doc__
    """
    color_edit4(str label, float r, float g, float b, float a, ImGuiColorEditFlags flags=0)
    Display color edit widget for color with alpha value.
    
        .. visual-example::
            :auto_layout:
            :width: 400
    
            # note: the variable that contains the color data, should be initialized
            #       outside of the main interaction loop
            color = 1., .0, .5, 1.
    
            imgui.begin("Example: color edit with alpha")
    
            # note: first element of return two-tuple notifies if the color was changed
            #       in currently processed frame and second element is current value
            #       of color and alpha
            _, color = imgui.color_edit4("Alpha", *color)
            _, color = imgui.color_edit4("No alpha", *color, imgui.COLOR_EDIT_NO_ALPHA)
    
            imgui.end()
    
        Args:
            label (str): color edit label.
            r (float): red color intensity.
            g (float): green color intensity.
            b (float): blue color instensity.
            a (float): alpha intensity.
            flags (ImGuiColorEditFlags): Color edit flags.  Zero for none.
    
        Returns:
            tuple: a ``(bool changed, float color[4])`` tuple that contains indicator of color
            change and current value of color and alpha
    
        .. wraps::
            ColorEdit4(
                const char* label, float col[4], ImGuiColorEditFlags flags
            )
    """
    pass

def columns(count: int=1, identifier: Optional[str]=None, bool_border=True): # real signature unknown; restored from __doc__
    """
    columns(int count=1, str identifier=None, bool border=True)
    Setup number of columns. Use an identifier to distinguish multiple
        column sets. close with ``columns(1)``.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        .. visual-example::
            :auto_layout:
            :width: 500
            :height: 300
    
            imgui.begin("Example: Columns - File list")
            imgui.columns(4, 'fileLlist')
            imgui.separator()
            imgui.text("ID")
            imgui.next_column()
            imgui.text("File")
            imgui.next_column()
            imgui.text("Size")
            imgui.next_column()
            imgui.text("Last Modified")
            imgui.next_column()
            imgui.separator()
            imgui.set_column_offset(1, 40)
    
            imgui.next_column()
            imgui.text('FileA.txt')
            imgui.next_column()
            imgui.text('57 Kb')
            imgui.next_column()
            imgui.text('12th Feb, 2016 12:19:01')
            imgui.next_column()
    
            imgui.next_column()
            imgui.text('ImageQ.png')
            imgui.next_column()
            imgui.text('349 Kb')
            imgui.next_column()
            imgui.text('1st Mar, 2016 06:38:22')
            imgui.next_column()
    
            imgui.columns(1)
            imgui.end()
    
        Args:
            count (int): Columns count.
            identifier (str): Table identifier.
            border (bool): Display border, defaults to ``True``.
    
        .. wraps::
            void Columns(
                int count = 1,
                const char* id = NULL,
                bool border = true
            )
    """
    pass

def combo(label: str, current: int, items: list, height_in_items: int=-1) -> Tuple[bool, int]: # real signature unknown; restored from __doc__
    """
    combo(str label, int current, list items, int height_in_items=-1)
    Display combo widget.
    
        .. visual-example::
            :auto_layout:
            :height: 200
            :click: 80 40
    
            current = 2
            imgui.begin("Example: combo widget")
    
            clicked, current = imgui.combo(
                "combo", current, ["first", "second", "third"]
            )
    
            imgui.end()
    
        Args:
            label (str): combo label.
            current (int): index of selected item.
            items (list): list of string labels for items.
            height_in_items (int): height of dropdown in items. Defaults to -1
                (autosized).
    
        Returns:
            tuple: a ``(changed, current)`` tuple indicating change of selection and current index of selected item.
    
        .. wraps::
            bool Combo(
                const char* label, int* current_item,
                const char* items_separated_by_zeros,
                int height_in_items = -1
            )
    """
    pass

def contextmanager(func): # reliably restored by inspect
    """
    @contextmanager decorator.
    
        Typical usage:
    
            @contextmanager
            def some_generator(<arguments>):
                <setup>
                try:
                    yield <value>
                finally:
                    <cleanup>
    
        This makes this:
    
            with some_generator(<arguments>) as <variable>:
                <body>
    
        equivalent to this:
    
            <setup>
            try:
                <variable> = <value>
                <body>
            finally:
                <cleanup>
    """
    pass

def create_context(_FontAtlas_shared_font_atlas=None): # real signature unknown; restored from __doc__
    """
    create_context(_FontAtlas shared_font_atlas=None)
    CreateContext
    
        .. todo::
            Add an example
    
        .. wraps::
            ImGuiContext* CreateContext(
                    # note: optional
                    ImFontAtlas* shared_font_atlas = NULL);
            )
    """
    pass

def destroy_context(_ImGuiContext_ctx=None): # real signature unknown; restored from __doc__
    """
    destroy_context(_ImGuiContext ctx=None)
    DestroyContext
    
        .. wraps::
            DestroyContext(
                    # note: optional
                    ImGuiContext* ctx = NULL);
    """
    pass

def drag_float(label: str, value: float, change_speed: float=1.0, min_value: float=0.0, max_value: float=0.0, format: str='%.3f', ImGuiSliderFlags_flags=0, power: float=1.): # real signature unknown; restored from __doc__
    """
    drag_float(str label, float value, float change_speed=1.0, float min_value=0.0, float max_value=0.0, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.)
    Display float drag widget.
    
        .. todo::
            Consider replacing ``format`` with something that allows
            for safer way to specify display format without loosing the
            functionality of wrapped function.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            value = 42.0
    
            imgui.begin("Example: drag float")
            changed, value = imgui.drag_float(
                "Default", value,
            )
            changed, value = imgui.drag_float(
                "Less precise", value, format="%.1f"
            )
            imgui.text("Changed: %s, Value: %s" % (changed, value))
            imgui.end()
    
        Args:
            label (str): widget label.
            value (float): drag values,
            change_speed (float): how fast values change on drag.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** Highly unsafe when used without care.
                May lead to segmentation faults and other memory violation issues.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            widget state change and the current drag value.
    
        .. wraps::
            bool DragFloat(
                const char* label,
                float* v,
                float v_speed = 1.0f,
                float v_min = 0.0f,
                float v_max = 0.0f,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_float2(label: str, value0: float, value1: float, change_speed: float=1.0, min_value: float=0.0, max_value: float=0.0, format: str='%.3f', ImGuiSliderFlags_flags=0, power: float=1.): # real signature unknown; restored from __doc__
    """
    drag_float2(str label, float value0, float value1, float change_speed=1.0, float min_value=0.0, float max_value=0.0, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.)
    Display float drag widget with 2 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88.0, 42.0
    
            imgui.begin("Example: drag float")
            changed, values = imgui.drag_float2(
                "Default", *values
            )
            changed, values = imgui.drag_float2(
                "Less precise", *values, format="%.1f"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (float): drag values.
            change_speed (float): how fast values change on drag.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current drag values.
    
        .. wraps::
            bool DragFloat2(
                const char* label,
                float v[2],
                float v_speed = 1.0f,
                float v_min = 0.0f,
                float v_max = 0.0f,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_float3(label: str, value0: float, value1: float, value2: float, change_speed: float=1.0, min_value: float=0.0, max_value: float=0.0, format: str='%.3f', ImGuiSliderFlags_flags=0, power: float=1.): # real signature unknown; restored from __doc__
    """
    drag_float3(str label, float value0, float value1, float value2, float change_speed=1.0, float min_value=0.0, float max_value=0.0, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.)
    Display float drag widget with 3 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88.0, 42.0, 69.0
    
            imgui.begin("Example: drag float")
            changed, values = imgui.drag_float3(
                "Default", *values
            )
            changed, values = imgui.drag_float3(
                "Less precise", *values, format="%.1f"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2 (float): drag values.
            change_speed (float): how fast values change on drag.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current drag values.
    
        .. wraps::
            bool DragFloat3(
                const char* label,
                float v[3],
                float v_speed = 1.0f,
                float v_min = 0.0f,
                float v_max = 0.0f,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_float4(label: str, value0: float, value1: float, value2: float, value3: float, change_speed: float = 1.0, min_value: float = 0.0, max_value: float = 0.0, format: str = '%.3f', flags=0, power: float = 1.): # real signature unknown; restored from __doc__
    """
    drag_float4(str label, float value0, float value1, float value2, float value3, float change_speed=1.0, float min_value=0.0, float max_value=0.0, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.)
    Display float drag widget with 4 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88.0, 42.0, 69.0, 0.0
    
            imgui.begin("Example: drag float")
            changed, values = imgui.drag_float4(
                "Default", *values
            )
            changed, values = imgui.drag_float4(
                "Less precise", *values, format="%.1f"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2, value3 (float): drag values.
            change_speed (float): how fast values change on drag.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current drag values.
    
        .. wraps::
            bool DragFloat4(
                const char* label,
                float v[4],
                float v_speed = 1.0f,
                float v_min = 0.0f,
                float v_max = 0.0f,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_range2(label: str, current_min: float, current_max: float, speed: float=1.0, min_value: float=0.0, max_value: float=0.0, format: str='%.3f', format_max: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__ # type: ignore
    """
    drag_range2(str label: float, float current_min, float current_max, float speed=1.0, float min_value=0.0, float max_value=0.0, str format='%.3f', str format_max=None, ImGuiSliderFlags flags=0)
    Display drag float range widget
    
        Args:
            label (str): widget label
            current_min (float): current value of minimum
            current_max (float): current value of maximum
            speed (float): widget speed of change
            min_value (float): minimal possible value
            max_value (float): maximal possible value
            format (str): display format
            format_max (str): display format for maximum. If None, ``format`` parameter is used.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a (changed, current_min, current_max) tuple, where ``changed`` indicate
                   that the value has been updated.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            vmin = 0
            vmax = 100
    
            imgui.begin("Example: drag float range")
            changed, vmin, vmax = imgui.drag_range2( "Drag Range": float, vmin, vmax )
            imgui.text("Changed: %s, Range: (%.2f, %.2f)" % (changed, vmin, vmax))
            imgui.end()
    
    
        .. wraps::
            bool DragFloatRange2(
                const char* label,
                float* v_current_min,
                float* v_current_max,
                float v_speed = 1.0f,
                float v_min = 0.0f,
                float v_max = 0.0f,
                const char* format = "%.3f",
                const char* format_max = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_int(label: str, value: int, change_speed: float=1.0, min_value: int=0, max_value: int=0, format: str='%d', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_int(str label, int value, float change_speed=1.0, int min_value=0, int max_value=0, str format='%d', ImGuiSliderFlags flags=0)
    Display int drag widget.
    
        .. todo::
            Consider replacing ``format`` with something that allows
            for safer way to specify display format without loosing the
            functionality of wrapped function.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            value = 42
    
            imgui.begin("Example: drag int")
            changed, value = imgui.drag_int("drag int", value,)
            imgui.text("Changed: %s, Value: %s" % (changed, value))
            imgui.end()
    
        Args:
            label (str): widget label.
            value (int): drag value,
            change_speed (float): how fast values change on drag.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** Highly unsafe when used without care.
                May lead to segmentation faults and other memory violation issues.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            widget state change and the current drag value.
    
        .. wraps::
            bool DragInt(
                const char* label,
                int* v,
                float v_speed = 1.0f,
                int v_min = 0.0f,
                int v_max = 0.0f,
                const char* format = "%d",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_int2(label: str, value0: int, value1: int, change_speed: float=1.0, min_value: int=0, max_value: int=0, format: str='%d', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_int2(str label, int value0, int value1, float change_speed=1.0, int min_value=0, int max_value=0, str format='%d', ImGuiSliderFlags flags=0)
    Display int drag widget with 2 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88, 42
    
            imgui.begin("Example: drag int")
            changed, values = imgui.drag_int2(
                "drag ints", *values
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (int): drag values.
            change_speed (float): how fast values change on drag.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current drag values.
    
        .. wraps::
            bool DragInt2(
                const char* label,
                int v[2],
                float v_speed = 1.0f,
                int v_min = 0.0f,
                int v_max = 0.0f,
                const char* format = "%d",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_int3(label: str, value0: int, value1: int, value2: int, change_speed: float=1.0, min_value: int=0, max_value: int=0, format: str='%d', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_int3(str label, int value0, int value1, int value2, float change_speed=1.0, int min_value=0, int max_value=0, str format='%d', ImGuiSliderFlags flags=0)
    Display int drag widget with 3 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88, 42, 69
    
            imgui.begin("Example: drag int")
            changed, values = imgui.drag_int3(
                "drag ints", *values
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (int): drag values.
            change_speed (float): how fast values change on drag.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current drag values.
    
        .. wraps::
            bool DragInt3(
                const char* label,
                int v[3],
                float v_speed = 1.0f,
                int v_min = 0.0f,
                int v_max = 0.0f,
                const char* format = "%d",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_int4(label: str, value0: int, value1: int, value2: int, value3: int, change_speed: float=1.0, min_value: int=0, max_value: int=0, format: str='%d', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_int4(str label, int value0, int value1, int value2, int value3, float change_speed=1.0, int min_value=0, int max_value=0, str format='%d', ImGuiSliderFlags flags=0)
    Display int drag widget with 4 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88, 42, 69, 0
    
            imgui.begin("Example: drag int")
            changed, values = imgui.drag_int4(
                "drag ints", *values
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (int): drag values.
            change_speed (float): how fast values change on drag.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current drag values.
    
        .. wraps::
            bool DragInt4(
                const char* label,
                int v[4],
                float v_speed = 1.0f,
                int v_min = 0.0f,
                int v_max = 0.0f,
                const char* format = "%d",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_range2(label: str, current_min: int, current_max: int, speed: float=1.0, min_value: int=0, max_value: int=0, format: str='%d', format_max: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_range2(str label: int, int current_min, int current_max, float speed=1.0, int min_value=0, int max_value=0, str format='%d', str format_max=None, ImGuiSliderFlags flags=0)
    Display drag int range widget
    
        Args:
            label (str): widget label
            current_min (int): current value of minimum
            current_max (int): current value of maximum
            speed (float): widget speed of change
            min_value (int): minimal possible value
            max_value (int): maximal possible value
            format (str): display format
            format_max (str): display format for maximum. If None, ``format`` parameter is used.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a (changed, current_min, current_max) tuple, where ``changed`` indicate
                   that the value has been updated.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            vmin = 0
            vmax = 100
    
            imgui.begin("Example: drag float range")
            changed, vmin, vmax = imgui.drag_range2( "Drag Range": int, vmin, vmax )
            imgui.text("Changed: %s, Range: (%d, %d)" % (changed, vmin, vmax))
            imgui.end()
    
    
        .. wraps::
            bool DragIntRange2(
                const char* label,
                int* v_current_min,
                int* v_current_max,
                float v_speed = 1.0f,
                int v_min = 0,
                int v_max = 0,
                const char* format = "%d",
                const char* format_max = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_scalar(label: str, ImGuiDataType_data_type, bytes_data, change_speed: float, bytes_min_value=None, bytes_max_value=None, format: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_scalar(str label, ImGuiDataType data_type, bytes data, float change_speed, bytes min_value=None, bytes max_value=None, str format=None, ImGuiSliderFlags flags=0)
    Display scalar drag widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            change_speed (float): how fast values change on drag
            min_value (bytes): min value allowed by widget
            max_value (bytes): max value allowed by widget
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: ImGuiSlider flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            drag state change and the current drag content.
    
        .. wraps::
            bool DragScalar(
                const char* label,
                ImGuiDataType data_type,
                void* p_data,
                float v_speed,
                const void* p_min = NULL,
                const void* p_max = NULL,
                const char* format = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def drag_scalar_N(label: str, ImGuiDataType_data_type, bytes_data, components: int, change_speed: float, bytes_min_value=None, bytes_max_value=None, format: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    drag_scalar_N(str label, ImGuiDataType data_type, bytes data, int components, float change_speed, bytes min_value=None, bytes max_value=None, str format=None, ImGuiSliderFlags flags=0)
    Display multiple scalar drag widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            components (int): number of widgets
            change_speed (float): how fast values change on drag
            min_value (bytes): min value allowed by widget
            max_value (bytes): max value allowed by widget
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: ImGuiSlider flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            drag state change and the current drag content.
    
        .. wraps::
            bool DragScalarN(
                const char* label,
                ImGuiDataType data_type,
                void* p_data,
                int components,
                float v_speed,
                const void* p_min = NULL,
                const void* p_max = NULL,
                const char* format = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def dummy(width, height): # real signature unknown; restored from __doc__
    """
    dummy(width, height)
    Add dummy element of given size.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            imgui.begin("Example: dummy elements")
    
            imgui.text("Some text with bullets:")
            imgui.bullet_text("Bullet A")
            imgui.bullet_text("Bullet B")
    
            imgui.dummy(0, 50)
            imgui.bullet_text("Text after dummy")
    
            imgui.end()
    
        .. wraps::
            void Dummy(const ImVec2& size)
    """
    pass

def end(): # real signature unknown; restored from __doc__
    """
    end()
    End a window.
    
        This finishes appending to current window, and pops it off the window
        stack. See: :any:`begin()`.
    
        .. wraps::
            void End()
    """
    pass

def end_child(): # real signature unknown; restored from __doc__
    """
    end_child()
    End scrolling region.
        Only call if ``begin_child().visible`` is True.
    
        .. wraps::
            void EndChild()
    """
    pass

def end_combo(): # real signature unknown; restored from __doc__
    """
    end_combo()
    End combo box.
        Only call if ``begin_combo().opened`` is True.
    
        .. wraps::
            void EndCombo()
    """
    pass

def end_drag_drop_source(): # real signature unknown; restored from __doc__
    """
    end_drag_drop_source()
    End the drag and drop source.
        Only call if ``begin_drag_drop_source().dragging`` is True.
    
        **Note:** this is a beta API.
    
        For a complete example see :func:`begin_drag_drop_source`.
    
        .. wraps::
            void EndDragDropSource()
    """
    pass

def end_drag_drop_target(): # real signature unknown; restored from __doc__
    """
    end_drag_drop_target()
    End the drag and drop source.
        Only call this function if ``begin_drag_drop_target().hovered`` is True.
    
        **Note:** this is a beta API.
    
        For a complete example see :func:`begin_drag_drop_source`.
    
        .. wraps::
            void EndDragDropTarget()
    """
    pass

def end_frame(): # real signature unknown; restored from __doc__
    """
    end_frame()
    End a frame.
    
        ends the ImGui frame. automatically called by Render(), so most likely
        don't need to ever call that yourself directly. If you don't need to
        render you may call end_frame() but you'll have wasted CPU already.
        If you don't need to render, better to not create any imgui windows
        instead!
    
        .. wraps::
            void EndFrame()
    """
    pass

def end_group(): # real signature unknown; restored from __doc__
    """
    end_group()
    End group (see: :any:`begin_group`).
    
        .. wraps::
            void EndGroup()
    """
    pass

def end_list_box(): # real signature unknown; restored from __doc__
    """
    end_list_box()
    
    
        Closing the listbox, previously opened by :func:`begin_list_box()`.
        Only call if ``begin_list_box().opened`` is True.
    
        See :func:`begin_list_box()` for usage example.
    
        .. wraps::
            void EndListBox()
    """
    pass

def end_main_menu_bar(): # real signature unknown; restored from __doc__
    """
    end_main_menu_bar()
    Close main menu bar context.
    
        Only call this function if the ``end_main_menu_bar().opened`` is True.
    
        For practical example how to use this function see documentation of
        :func:`begin_main_menu_bar`.
    
        .. wraps::
            bool EndMainMenuBar()
    """
    pass

def end_menu(): # real signature unknown; restored from __doc__
    """
    end_menu()
    Close menu context.
    
        Only call this function if ``begin_menu().opened`` returns True.
    
        For practical example how to use this function, please see documentation
        of :func:`begin_main_menu_bar` or :func:`begin_menu_bar`.
    
        .. wraps::
            void EndMenu()
    """
    pass

def end_menu_bar(): # real signature unknown; restored from __doc__
    """
    end_menu_bar()
    Close menu bar context.
    
        Only call this function if ``begin_menu_bar().opened`` is True.
    
        For practical example how to use this function see documentation of
        :func:`begin_menu_bar`.
    
        .. wraps::
            void EndMenuBar()
    """
    pass

def end_popup(): # real signature unknown; restored from __doc__
    """
    end_popup()
    End a popup window.
    
        Should be called after each XYZPopupXYZ function.
        Only call this function if ``begin_popup_XYZ().opened`` is True.
    
        For practical example how to use this function, please see documentation
        of :func:`open_popup`.
    
        .. wraps::
            void EndPopup()
    """
    pass

def end_table(): # real signature unknown; restored from __doc__
    """
    end_table()
    
        End a previously opened table.
        Only call this function if ``begin_table().opened`` is True.
    
        .. wraps::
            void EndTable()
    """
    pass

def end_tab_bar(): # real signature unknown; restored from __doc__
    """
    end_tab_bar()
    End a previously opened tab bar.
        Only call this function if ``begin_tab_bar().opened`` is True.
    
        .. wraps::
            void EndTabBar()
    """
    pass

def end_tab_item(): # real signature unknown; restored from __doc__
    """
    end_tab_item()
    End a previously opened tab item.
        Only call this function if ``begin_tab_item().selected`` is True.
    
        .. wraps::
            void EndTabItem()
    """
    pass

def end_tooltip(): # real signature unknown; restored from __doc__
    """
    end_tooltip()
    End tooltip window.
    
        See :func:`begin_tooltip()` for full usage example.
    
        .. wraps::
            void EndTooltip()
    """
    pass

def get_background_draw_list(): # real signature unknown; restored from __doc__
    """
    get_background_draw_list()
    This draw list will be the first rendering one.
        Useful to quickly draw shapes/text behind dear imgui contents.
    
        Returns:
            DrawList*
    
        .. wraps::
            ImDrawList* GetBackgroundDrawList()
    """
    pass

def get_clipboard_text(): # real signature unknown; restored from __doc__
    """
    get_clipboard_text()
    Also see the ``log_to_clipboard()`` function to capture GUI into clipboard,
        or easily output text data to the clipboard.
    
        Returns:
            str: Text content of the clipboard
    
        .. wraps::
            const char* GetClipboardText()
    """
    pass

def get_color_u32(ImU32_col): # real signature unknown; restored from __doc__
    """
    get_color_u32(ImU32 col)
    retrieve given style color with style alpha applied and optional extra alpha multiplier
    
        Returns:
            ImU32: 32-bit RGBA color
    
        .. wraps::
            ImU32 GetColorU32(ImU32 col)
    """
    pass

def get_color_u32_idx(ImGuiCol_idx, alpha_mul: float=1.0): # real signature unknown; restored from __doc__
    """
    get_color_u32_idx(ImGuiCol idx, float alpha_mul=1.0)
     retrieve given style color with style alpha applied and optional extra alpha multiplier
    
        Returns:
            ImU32: 32-bit RGBA color
    
        .. wraps::
            ImU32 GetColorU32(ImGuiCol idx, alpha_mul)
    """
    pass

def get_color_u32_rgba(r: float, g: float, b: float, a: float): # real signature unknown; restored from __doc__
    """
    get_color_u32_rgba(float r, float g, float b, float a)
     retrieve given color with style alpha applied
    
        Returns:
            ImU32: 32-bit RGBA color
    
        .. wraps::
            ImU32 GetColorU32(const ImVec4& col)
    """
    pass

def get_columns_count(): # real signature unknown; restored from __doc__
    """
    get_columns_count()
    Get count of the columns in the current table.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        Returns:
            int: columns count.
    
        .. wraps::
            int GetColumnsCount()
    """
    pass

def get_column_index(): # real signature unknown; restored from __doc__
    """
    get_column_index()
    Returns the current column index.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        Returns:
            int: the current column index.
    
        .. wraps::
            int GetColumnIndex()
    """
    pass

def get_column_offset(column_index: int=-1): # real signature unknown; restored from __doc__
    """
    get_column_offset(int column_index=-1)
    Returns position of column line (in pixels, from the left side of the
        contents region). Pass -1 to use current column, otherwise 0 to
        :func:`get_columns_count()`. Column 0 is usually 0.0f and not resizable
        unless you call this method.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        Args:
            column_index (int): index of the column to get the offset for.
    
        Returns:
            float: the position in pixels from the left side.
    
        .. wraps::
            float GetColumnOffset(int column_index = -1)
    """
    pass

def get_column_width(column_index: int=-1): # real signature unknown; restored from __doc__
    """
    get_column_width(int column_index=-1)
    Return the column width.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        Args:
            column_index (int): index of the column to get the width for.
    
        .. wraps::
            float GetColumnWidth(int column_index = -1)
    """
    pass

def get_content_region_available(): # real signature unknown; restored from __doc__
    """
    get_content_region_available()
    Get available content region.
    
        It is shortcut for:
    
        .. code-block: python
            imgui.get_content_region_max() - imgui.get_cursor_position()
    
        Returns:
            Vec2: available content region size two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetContentRegionMax()
    """
    pass

def get_content_region_available_width(): # real signature unknown; restored from __doc__
    """
    get_content_region_available_width()
    Get available content region width.
    
        Returns:
            float: available content region width.
    
        .. wraps::
            float GetContentRegionAvailWidth()
    """
    pass

def get_content_region_max(): # real signature unknown; restored from __doc__
    """
    get_content_region_max()
    Get current content boundaries in window coordinates.
    
        Typically window boundaries include scrolling, or current
        column boundaries.
    
        Returns:
            Vec2: content boundaries two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetContentRegionMax()
    """
    pass

def get_current_context(): # real signature unknown; restored from __doc__
    """
    get_current_context()
    GetCurrentContext
    
        .. wraps::
            ImGuiContext* GetCurrentContext();
    """
    pass

def get_cursor_pos(): # real signature unknown; restored from __doc__
    """
    get_cursor_pos()
    Get the cursor position.
    
        .. wraps::
            ImVec2 GetCursorPos()
    """
    pass

def get_cursor_position(*args, **kwargs): # real signature unknown
    """
    get_cursor_pos()
    Get the cursor position.
    
        .. wraps::
            ImVec2 GetCursorPos()
    """
    pass

def get_cursor_pos_x(): # real signature unknown; restored from __doc__
    """ get_cursor_pos_x() """
    pass

def get_cursor_pos_y(): # real signature unknown; restored from __doc__
    """ get_cursor_pos_y() """
    pass

def get_cursor_screen_pos(): # real signature unknown; restored from __doc__
    """
    get_cursor_screen_pos()
    Get the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)
    
        .. wraps::
            ImVec2 GetCursorScreenPos()
    """
    pass

def get_cursor_screen_position(*args, **kwargs): # real signature unknown
    """
    get_cursor_screen_pos()
    Get the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)
    
        .. wraps::
            ImVec2 GetCursorScreenPos()
    """
    pass

def get_cursor_start_pos(): # real signature unknown; restored from __doc__
    """
    get_cursor_start_pos()
    Get the initial cursor position.
    
        .. wraps::
            ImVec2 GetCursorStartPos()
    """
    pass

def get_cursor_start_position(*args, **kwargs): # real signature unknown
    """
    get_cursor_start_pos()
    Get the initial cursor position.
    
        .. wraps::
            ImVec2 GetCursorStartPos()
    """
    pass

def get_drag_drop_payload(): # real signature unknown; restored from __doc__
    """
    get_drag_drop_payload()
    Peek directly into the current payload from anywhere. 
        May return NULL. 
        
        .. todo:: Map ImGuiPayload::IsDataType() to test for the payload type.
        
        .. wraps::
            const ImGuiPayload* GetDragDropPayload()
    """
    pass

def get_draw_data(): # real signature unknown; restored from __doc__
    """
    get_draw_data()
    Get draw data.
    
        valid after :any:`render()` and until the next call
        to :any:`new_frame()`.  This is what you have to render.
    
        Returns:
            _DrawData: draw data for all draw calls required to display gui
    
        .. wraps::
            ImDrawData* GetDrawData()
    """
    pass

def get_font_size(): # real signature unknown; restored from __doc__
    """
    get_font_size()
    get current font size (= height in pixels) of current font with current scale applied
    
        Returns:
            float: current font size (height in pixels)
    
        .. wraps::
            float GetFontSize()
    """
    pass

def get_font_tex_uv_white_pixel(): # real signature unknown; restored from __doc__
    """ get_font_tex_uv_white_pixel() """
    pass

def get_foreground_draw_list(): # real signature unknown; restored from __doc__
    """
    get_foreground_draw_list()
    This draw list will be the last rendered one.
        Useful to quickly draw shapes/text over dear imgui contents.
    
        Returns:
            DrawList*
    
        .. wraps::
            ImDrawList* GetForegroundDrawList()
    """
    pass

def get_frame_height(): # real signature unknown; restored from __doc__
    """
    get_frame_height()
    ~ FontSize + style.FramePadding.y * 2
    
        .. wraps::
            float GetFrameHeight()
            float GetFrameHeightWithSpacing() except +
    """
    pass

def get_frame_height_with_spacing(): # real signature unknown; restored from __doc__
    """
    get_frame_height_with_spacing()
    ~ FontSize + style.FramePadding.y * 2 + style.ItemSpacing.y (distance in pixels between 2 consecutive lines of framed widgets)
    
        .. wraps::
            float GetFrameHeightWithSpacing()
    """
    pass

def get_io(): # real signature unknown; restored from __doc__
    """ get_io() """
    pass

def get_item_rect_max(): # real signature unknown; restored from __doc__
    """
    get_item_rect_max()
    Get bounding rect of the last item in screen space.
    
        Returns:
            Vec2: item maximum boundaries two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetItemRectMax()
    """
    pass

def get_item_rect_min(): # real signature unknown; restored from __doc__
    """
    get_item_rect_min()
    Get bounding rect of the last item in screen space.
    
        Returns:
            Vec2: item minimum boundaries two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetItemRectMin()
    """
    pass

def get_item_rect_size(): # real signature unknown; restored from __doc__
    """
    get_item_rect_size()
    Get bounding rect of the last item in screen space.
    
        Returns:
            Vec2: item boundaries two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetItemRectSize()
    """
    pass

def get_key_index(key: int): # real signature unknown; restored from __doc__
    """
    get_key_index(int key)
    Map ImGuiKey_* values into user's key index. == io.KeyMap[key]
    
        Returns:
           int: io.KeyMap[key]
    
        .. wraps::
            int GetKeyIndex(ImGuiKey imgui_key)
    """
    pass

def get_main_viewport(): # real signature unknown; restored from __doc__
    """
    get_main_viewport()
    Currently represents the Platform Window created by the application which is hosting
        our Dear ImGui windows.
    
        In the future we will extend this concept further to also represent Platform Monitor
        and support a "no main platform window" operation mode.
    
        Returns:
            _ImGuiViewport: Viewport
    
        .. wraps::
            ImGuiViewport* GetMainViewport()
    """
    pass

def get_mouse_cursor(): # real signature unknown; restored from __doc__
    """
    get_mouse_cursor()
    Return the mouse cursor id.
    
        .. wraps::
            ImGuiMouseCursor GetMouseCursor()
    """
    pass

def get_mouse_drag_delta(button: int=0, lock_threshold: float=-1.0): # real signature unknown; restored from __doc__
    """
    get_mouse_drag_delta(int button=0, float lock_threshold=-1.0)
    Dragging amount since clicking.
    
        Args:
            button (int): mouse button index.
            lock_threshold (float): if less than -1.0
                uses io.MouseDraggingThreshold.
    
        Returns:
            Vec2: mouse position two-tuple ``(x, y)``
    
        .. wraps::
            ImVec2 GetMouseDragDelta(int button = 0, float lock_threshold = -1.0f)
    """
    pass

def get_mouse_pos(): # real signature unknown; restored from __doc__
    """
    get_mouse_pos()
    Current mouse position.
    
        Returns:
            Vec2: mouse position two-tuple ``(x, y)``
    
        .. wraps::
            ImVec2 GetMousePos()
    """
    pass

def get_mouse_position(*args, **kwargs): # real signature unknown
    """
    get_mouse_pos()
    Current mouse position.
    
        Returns:
            Vec2: mouse position two-tuple ``(x, y)``
    
        .. wraps::
            ImVec2 GetMousePos()
    """
    pass

def get_overlay_draw_list(): # real signature unknown; restored from __doc__
    """
    get_overlay_draw_list()
    Get a special draw list that will be drawn last (over all windows).
    
        Useful for drawing overlays.
    
        Returns:
            ImDrawList*
    
        .. wraps::
            ImDrawList* GetWindowDrawList()
    """
    pass

def get_scroll_max_x(): # real signature unknown; restored from __doc__
    """
    get_scroll_max_x()
    get maximum scrolling amount ~~ ContentSize.X - WindowSize.X
    
        Returns:
            float: the maximum scroll X amount
    
        .. wraps::
            int GetScrollMaxX()
    """
    pass

def get_scroll_max_y(): # real signature unknown; restored from __doc__
    """
    get_scroll_max_y()
    get maximum scrolling amount ~~ ContentSize.X - WindowSize.X
    
        Returns:
            float: the maximum scroll Y amount
    
        .. wraps::
            int GetScrollMaxY()
    """
    pass

def get_scroll_x(): # real signature unknown; restored from __doc__
    """
    get_scroll_x()
    get scrolling amount [0..GetScrollMaxX()]
    
        Returns:
            float: the current scroll X value
    
        .. wraps::
            int GetScrollX()
    """
    pass

def get_scroll_y(): # real signature unknown; restored from __doc__
    """
    get_scroll_y()
    get scrolling amount [0..GetScrollMaxY()]
    
        Returns:
            float: the current scroll Y value
    
        .. wraps::
            int GetScrollY()
    """
    pass

def get_style(): # real signature unknown; restored from __doc__
    """ get_style() """
    pass

def get_style_color_name(index: int): # real signature unknown; restored from __doc__
    """
    get_style_color_name(int index)
    Get the style color name for a given ImGuiCol index.
    
        .. wraps::
            const char* GetStyleColorName(ImGuiCol idx)
    """
    pass

def get_style_color_vec_4(ImGuiCol_idx): # real signature unknown; restored from __doc__
    """ get_style_color_vec_4(ImGuiCol idx) """
    pass

def get_text_line_height(): # real signature unknown; restored from __doc__
    """
    get_text_line_height()
    Get text line height.
    
        Returns:
            int: text line height.
    
        .. wraps::
            void GetTextLineHeight()
    """
    pass

def get_text_line_height_with_spacing(): # real signature unknown; restored from __doc__
    """
    get_text_line_height_with_spacing()
    Get text line height, with spacing.
    
        Returns:
            int: text line height, with spacing.
    
        .. wraps::
            void GetTextLineHeightWithSpacing()
    """
    pass

def get_time(): # real signature unknown; restored from __doc__
    """
    get_time()
    Seconds since program start.
    
        Returns:
            float: the time (seconds since program start)
    
        .. wraps::
            float GetTime()
    """
    pass

def get_tree_node_to_label_spacing(): # real signature unknown; restored from __doc__
    """
    get_tree_node_to_label_spacing()
    Horizontal distance preceding label when using ``tree_node*()``
        or ``bullet() == (g.FontSize + style.FramePadding.x*2)`` for a
        regular unframed TreeNode
    
        Returns:
            float: spacing
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
    
            imgui.begin("TreeNode")
            imgui.text("<- 0px offset here")
            if imgui.tree_node("Expand me!", imgui.TREE_NODE_DEFAULT_OPEN):
                imgui.text("<- %.2fpx offset here" % imgui.get_tree_node_to_label_spacing())
                imgui.tree_pop()
            imgui.end()
    
        .. wraps::
            float GetTreeNodeToLabelSpacing()
    """
    pass

def get_version(): # real signature unknown; restored from __doc__
    """
    get_version()
    Get the version of Dear ImGui.
    
        .. wraps::
            void GetVersion()
    """
    pass

def get_window_content_region_max(): # real signature unknown; restored from __doc__
    """
    get_window_content_region_max()
    Get maximal current window content boundaries in window coordinates.
    
        It translates roughly to: ``(0, 0) + Size - Scroll``
    
        Returns:
            Vec2: content boundaries two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetWindowContentRegionMin()
    """
    pass

def get_window_content_region_min(): # real signature unknown; restored from __doc__
    """
    get_window_content_region_min()
    Get minimal current window content boundaries in window coordinates.
    
        It translates roughly to: ``(0, 0) - Scroll``
    
        Returns:
            Vec2: content boundaries two-tuple ``(width, height)``
    
        .. wraps::
            ImVec2 GetWindowContentRegionMin()
    """
    pass

def get_window_content_region_width(): # real signature unknown; restored from __doc__
    """
    get_window_content_region_width()
    Get available current window content region width.
    
        Returns:
            float: available content region width.
    
        .. wraps::
            float GetWindowContentRegionWidth()
    """
    pass

def get_window_draw_list(): # real signature unknown; restored from __doc__
    """
    get_window_draw_list()
    Get the draw list associated with the window, to append your own drawing primitives
    
        It may be useful if you want to do your own drawing via the :class:`_DrawList`
        API.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
            :click: 10 10
    
    
            pos_x = 10
            pos_y = 10
            sz = 20
    
            draw_list = imgui.get_window_draw_list()
    
            for i in range(0, imgui.COLOR_COUNT):
                name = imgui.get_style_color_name(i);
                draw_list.add_rect_filled(pos_x, pos_y, pos_x+sz, pos_y+sz, imgui.get_color_u32_idx(i));
                imgui.dummy(sz, sz);
                imgui.same_line();
    
            rgba_color = imgui.get_color_u32_rgba(1, 1, 0, 1);
            draw_list.add_rect_filled(pos_x, pos_y, pos_x+sz, pos_y+sz, rgba_color);
    
    
        Returns:
            ImDrawList*
    
        .. wraps::
            ImDrawList* GetWindowDrawList()
    """
    pass

def get_window_height(): # real signature unknown; restored from __doc__
    """
    get_window_height()
    Get current window height.
    
        Returns:
            float: height of current window.
    
        .. wraps::
            float GetWindowHeight()
    """
    pass

def get_window_position(): # real signature unknown; restored from __doc__
    """
    get_window_position()
    Get current window position.
    
        It may be useful if you want to do your own drawing via the DrawList
        api.
    
        Returns:
            Vec2: two-tuple of window coordinates in screen space.
    
        .. wraps::
            ImVec2 GetWindowPos()
    """
    pass

def get_window_size(): # real signature unknown; restored from __doc__
    """
    get_window_size()
    Get current window size.
    
        Returns:
            Vec2: two-tuple of window dimensions.
    
        .. wraps::
            ImVec2 GetWindowSize()
    """
    pass

def get_window_width(): # real signature unknown; restored from __doc__
    """
    get_window_width()
    Get current window width.
    
        Returns:
            float: width of current window.
    
        .. wraps::
            float GetWindowWidth()
    """
    pass

def image(texture_id, width: float, height: float, tuple_uv0=00, tuple_uv1=11, tuple_tcolor: int=1111, tuple_border_color=0000): # real signature unknown; restored from __doc__
    """
    image(texture_id, float width, float height, tuple uv0=(0, 0), tuple uv1=(1, 1), tuple tcolor: int=(1, 1, 1, 1), tuple border_color=(0, 0, 0, 0))
    Display image.
    
        .. visual-example::
            :auto_layout:
            :width: 550
            :height: 200
    
            texture_id = imgui.get_io().fonts.texture_id
    
            imgui.begin("Example: image display")
            imgui.image(texture_id, 512, 64, border_color=(1, 0, 0, 1))
            imgui.end()
    
        Args:
            texture_id (object): user data defining texture id. Argument type
                is implementation dependent. For OpenGL it is usually an integer.
            size (Vec2): image display size two-tuple.
            uv0 (Vec2): UV coordinates for 1st corner (lower-left for OpenGL).
                Defaults to ``(0, 0)``.
            uv1 (Vec2): UV coordinates for 2nd corner (upper-right for OpenGL).
                Defaults to ``(1, 1)``.
            tcolor(Vec4: int): Image tint color. Defaults to white.
            border_color(Vec4): Image border color. Defaults to transparent.
    
        .. wraps::
            void Image(
                ImTextureID user_texture_id,
                const ImVec2& size,
                const ImVec2& uv0 = ImVec2(0,0),
                const ImVec2& uv1 = ImVec2(1,1),
                const ImVec4& tcol : int= ImVec4(1,1,1,1),
                const ImVec4& border_col = ImVec4(0,0,0,0)
            )
    """
    pass

def image_button(texture_id, width: float, height: float, tuple_uv0=00, tuple_uv1=11, tuple_tcolor: int=1111, tuple_border_color=0000, frame_padding: int=-1): # real signature unknown; restored from __doc__
    """
    image_button(texture_id, float width, float height, tuple uv0=(0, 0), tuple uv1=(1, 1), tuple tcolor: int=(1, 1, 1, 1), tuple border_color=(0, 0, 0, 0), int frame_padding=-1)
    Display image.
    
        .. todo:: add example with some preconfigured image
    
        Args:
            texture_id (object): user data defining texture id. Argument type
                is implementation dependent. For OpenGL it is usually an integer.
            size (Vec2): image display size two-tuple.
            uv0 (Vec2): UV coordinates for 1st corner (lower-left for OpenGL).
                Defaults to ``(0, 0)``.
            uv1 (Vec2): UV coordinates for 2nd corner (upper-right for OpenGL).
                Defaults to ``(1, 1)``.
            tcolor (Vec4: int): Image tint color. Defaults to white.
            border_color (Vec4): Image border color. Defaults to transparent.
            frame_padding (int): Frame padding (``0``: no padding, ``<0`` default
                padding).
    
        Returns:
            bool: True if clicked.
    
        .. wraps::
            bool ImageButton(
                ImTextureID user_texture_id,
                const ImVec2& size,
                const ImVec2& uv0 = ImVec2(0,0),
                const ImVec2& uv1 = ImVec2(1,1),
                int frame_padding = -1,
                const ImVec4& bg_col = ImVec4(0,0,0,0),
                const ImVec4& tcol : int= ImVec4(1,1,1,1)
            )
    """
    pass

def indent(width: float=0.0): # real signature unknown; restored from __doc__
    """
    indent(float width=0.0)
    Move content to right by indent width.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            imgui.begin("Example: item indenting")
    
            imgui.text("Some text with bullets:")
    
            imgui.bullet_text("Bullet A")
            imgui.indent()
            imgui.bullet_text("Bullet B (first indented)")
            imgui.bullet_text("Bullet C (indent continues)")
            imgui.unindent()
            imgui.bullet_text("Bullet D (indent cleared)")
    
            imgui.end()
    
        Args:
            width (float): fixed width of indent. If less or equal 0 it defaults
                to global indent spacing or value set using style value  stack
                (see :any:`push_style_var`).
    
        .. wraps::
            void Indent(float indent_w = 0.0f)
    """
    pass

def input_double(label: str, double_value, double_step=0.0, double_step_fast=0.0, format: str='%.6f', ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_double(str label, double value, double step=0.0, double step_fast=0.0, str format='%.6f', ImGuiInputTextFlags flags=0)
    Display double input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            double_val = 3.14159265358979323846
            imgui.begin("Example: double input")
            changed, double_val = imgui.input_double('Type multiplier:', double_val)
            imgui.text('You wrote: %i' % double_val)
            imgui.end()
    
        Args:
            label (str): widget label.
            value (double): textbox value
            step (double): incremental step
            step_fast (double): fast incremental step
            format = (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current textbox content.
    
        .. wraps::
            bool InputDouble(
                const char* label,
                double* v,
                double step = 0.0,
                double step_fast = 0.0,
                _bytes(format),
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_float(label: str, value: float, step: float=0.0, step_fast: float=0.0, format: str='%.3f', ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_float(str label, float value, float step=0.0, float step_fast=0.0, str format='%.3f', ImGuiInputTextFlags flags=0)
    Display float input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            val : float= 0.4
            imgui.begin("Example: float input")
            changed, val : float= imgui.input_float('Type coefficient:', val: float)
            imgui.text('You wrote: %f' % val: float)
            imgui.end()
    
        Args:
            label (str): widget label.
            value (float): textbox value
            step (float): incremental step
            step_fast (float): fast incremental step
            format = (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current textbox content.
    
        .. wraps::
            bool InputFloat(
                const char* label,
                float* v,
                float step = 0.0f,
                float step_fast = 0.0f,
                const char* format = "%.3f",
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_float2(label: str, value0: float, value1: float, format: str='%.3f', ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_float2(str label, float value0, float value1, str format='%.3f', ImGuiInputTextFlags flags=0)
    Display two-float input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            values = 0.4, 3.2
            imgui.begin("Example: two float inputs")
            changed, values = imgui.input_float2('Type here:', *values)
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (float): input values.
            format = (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            textbox state change and the tuple of current values.
    
        .. wraps::
            bool InputFloat2(
                const char* label,
                float v[2],
                const char* format = "%.3f",
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_float3(label: str, value0: float, value1: float, value2: float, format: str='%.3f', ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_float3(str label, float value0, float value1, float value2, str format='%.3f', ImGuiInputTextFlags flags=0)
    Display three-float input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            values = 0.4, 3.2, 29.3
            imgui.begin("Example: three float inputs")
            changed, values = imgui.input_float3('Type here:', *values)
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2 (float): input values.
            format = (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            textbox state change and the tuple of current values.
    
        .. wraps::
            bool InputFloat3(
                const char* label,
                float v[3],
                const char* format = "%.3f",
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_float4(label: str, value0: float, value1: float, value2: float, value3: float, format: str='%.3f', ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_float4(str label, float value0, float value1, float value2, float value3, str format='%.3f', ImGuiInputTextFlags flags=0)
    Display four-float input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            values = 0.4, 3.2, 29.3, 12.9
            imgui.begin("Example: four float inputs")
            changed, values = imgui.input_float4('Type here:', *values)
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2, value3 (float): input values.
            format = (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            textbox state change and the tuple of current values.
    
        .. wraps::
            bool InputFloat4(
                const char* label,
                float v[4],
                const char* format = "%.3f",
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_int(label: str, value: int, step: int=1, step_fast: int=100, ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_int(str label, int value, int step=1, int step_fast=100, ImGuiInputTextFlags flags=0)
    Display integer input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            val : int= 3
            imgui.begin("Example: integer input")
            changed, val : int= imgui.input_int('Type multiplier:', val: int)
            imgui.text('You wrote: %i' % val: int)
            imgui.end()
    
        Args:
            label (str): widget label.
            value (int): textbox value
            step (int): incremental step
            step_fast (int): fast incremental step
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current textbox content.
    
        .. wraps::
            bool InputInt(
                const char* label,
                int* v,
                int step = 1,
                int step_fast = 100,
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_int2(label: str, value0: int, value1: int, ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_int2(str label, int value0, int value1, ImGuiInputTextFlags flags=0)
    Display two-integer input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            values = 4, 12
            imgui.begin("Example: two int inputs")
            changed, values = imgui.input_int2('Type here:', *values)
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (int): textbox values
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current textbox content.
    
        .. wraps::
            bool InputInt2(
                const char* label,
                int v[2],
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_int3(label: str, value0: int, value1: int, value2: int, ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_int3(str label, int value0, int value1, int value2, ImGuiInputTextFlags flags=0)
    Display three-integer input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            values = 4, 12, 28
            imgui.begin("Example: three int inputs")
            changed, values = imgui.input_int3('Type here:', *values)
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2 (int): textbox values
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current textbox content.
    
        .. wraps::
            bool InputInt3(
                const char* label,
                int v[3],
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_int4(label: str, value0: int, value1: int, value2: int, value3: int, ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_int4(str label, int value0, int value1, int value2, int value3, ImGuiInputTextFlags flags=0)
    Display four-integer input widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            values = 4, 12, 28, 73
            imgui.begin("Example: four int inputs")
            changed, values = imgui.input_int4('Type here:', *values)
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2, value3 (int): textbox values
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current textbox content.
    
        .. wraps::
            bool InputInt4(
                const char* label,
                int v[4],
                ImGuiInputTextFlags extra_flags = 0
            )
    """
    pass

def input_scalar(label: str, ImGuiDataType_data_type, bytes_data, bytes_step=None, bytes_step_fast=None, format: Optional[str]=None, ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_scalar(str label, ImGuiDataType data_type, bytes data, bytes step=None, bytes step_fast=None, str format=None, ImGuiInputTextFlags flags=0)
    Display scalar input widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            step (bytes): incremental step
            step_fast (bytes): fast incremental step
            format (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            input state change and the current input content.
    
        .. wraps::
            bool InputScalar(
                const char* label,
                ImGuiDataType data_type,
                void* p_data,
                const void* p_step = NULL,
                const void* p_step_fast = NULL,
                const char* format = NULL,
                ImGuiInputTextFlags flags = 0
            )
    """
    pass

def input_scalar_N(label: str, ImGuiDataType_data_type, bytes_data, components: int, bytes_step=None, bytes_step_fast=None, format: Optional[str]=None, ImGuiInputTextFlags_flags=0): # real signature unknown; restored from __doc__
    """
    input_scalar_N(str label, ImGuiDataType data_type, bytes data, int components, bytes step=None, bytes step_fast=None, str format=None, ImGuiInputTextFlags flags=0)
    Display multiple scalar input widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            components (int): number of components to display
            step (bytes): incremental step
            step_fast (bytes): fast incremental step
            format (str): format string
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            input state change and the current input content.
    
        .. wraps::
            bool InputScalarN(
                const char* label,
                ImGuiDataType data_type,
                void* p_data,
                int components,
                const void* p_step = NULL,
                const void* p_step_fast = NULL,
                const char* format = NULL,
                ImGuiInputTextFlags flags = 0
            )
    """
    pass

def input_text(label: str, value: str, buffer_length: int=-1, ImGuiInputTextFlags_flags=0, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """
    input_text(str label, str value, int buffer_length=-1, ImGuiInputTextFlags flags=0, callback=None, user_data=None)
    Display text input widget.
    
        The ``buffer_length`` is the maximum allowed length of the content. It is the size in bytes, which may not correspond to the number of characters.
        If set to -1, the internal buffer will have an adaptive size, which is equivalent to using the ``imgui.INPUT_TEXT_CALLBACK_RESIZE`` flag.
        When a callback is provided, it is called after the internal buffer has been resized.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 100
    
            text_val = 'Please, type the coefficient here.'
            imgui.begin("Example: text input")
            changed, text_val = imgui.input_text('Coefficient:', text_val)
            imgui.text('You wrote:')
            imgui.same_line()
            imgui.text(text_val)
            imgui.end()
    
        Args:
            label (str): widget label.
            value (str): textbox value
            buffer_length (int): length of the content buffer
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
            callback (callable): a callable that is called depending on choosen flags.
                Callable takes an imgui._ImGuiInputTextCallbackData object as argument
                Callable should return None or integer
            user_data: Any data that the user want to use in the callback.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current text contents.
    
        .. wraps::
            bool InputText(
                const char* label,
                char* buf,
                size_t buf_size,
                ImGuiInputTextFlags flags = 0,
                ImGuiInputTextCallback callback = NULL,
                void* user_data = NULL
            )
    """
    pass

def input_text_multiline(label: str, value: str, buffer_length: int=-1, width: float=0, height: float=0, ImGuiInputTextFlags_flags=0, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """
    input_text_multiline(str label, str value, int buffer_length=-1, float width=0, float height=0, ImGuiInputTextFlags flags=0, callback=None, user_data=None)
    Display multiline text input widget.
    
        The ``buffer_length`` is the maximum allowed length of the content. It is the size in bytes, which may not correspond to the number of characters.
        If set to -1, the internal buffer will have an adaptive size, which is equivalent to using the ``imgui.INPUT_TEXT_CALLBACK_RESIZE`` flag.
        When a callback is provided, it is called after the internal buffer has been resized.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 200
    
            text_val = 'Type the your message here.'
            imgui.begin("Example: text input")
            changed, text_val = imgui.input_text_multiline(
                'Message:',
                text_val,
                2056
            )
            imgui.text('You wrote:')
            imgui.same_line()
            imgui.text(text_val)
            imgui.end()
    
        Args:
            label (str): widget label.
            value (str): textbox value
            buffer_length (int): length of the content buffer
            width (float): width of the textbox
            height (float): height of the textbox
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
            callback (callable): a callable that is called depending on choosen flags.
                Callable takes an imgui._ImGuiInputTextCallbackData object as argument
                Callable should return None or integer
            user_data: Any data that the user want to use in the callback.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current text contents.
    
        .. wraps::
            bool InputTextMultiline(
                const char* label,
                char* buf,
                size_t buf_size,
                const ImVec2& size = ImVec2(0,0),
                ImGuiInputTextFlags flags = 0,
                ImGuiInputTextCallback callback = NULL,
                void* user_data = NULL
            )
    """
    pass

def input_text_with_hint(label: str, hint: str, value: str, buffer_length: int=-1, ImGuiInputTextFlags_flags=0, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """
    input_text_with_hint(str label, str hint, str value, int buffer_length=-1, ImGuiInputTextFlags flags=0, callback=None, user_data=None)
    Display a text box, if the text is empty a hint on how to fill the box is given.
    
        The ``buffer_length`` is the maximum allowed length of the content. It is the size in bytes, which may not correspond to the number of characters.
        If set to -1, the internal buffer will have an adaptive size, which is equivalent to using the ``imgui.INPUT_TEXT_CALLBACK_RESIZE`` flag.
        When a callback is provided, it is called after the internal buffer has been resized.
    
        Args:
            label (str): Widget label
            hing (str): Hint displayed if text value empty
            value (str): Text value
            buffer_length (int): Length of the content buffer
            flags: InputText flags. See:
                :ref:`list of available flags <inputtext-flag-options>`.
            callback (callable): a callable that is called depending on choosen flags.
                Callable takes an imgui._ImGuiInputTextCallbackData object as argument
                Callable should return None or integer
            user_data: Any data that the user want to use in the callback.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            textbox state change and the current text contents.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 200
    
            text_val = ''
            imgui.begin("Example Text With hing")
            changed, text_val = imgui.input_text_with_hint(
                'Email', 'your@email.com',
                text_val, 255)
            imgui.end()
    
        .. wraps::
            bool InputTextWithHint(
                const char* label,
                const char* hint,
                char* buf,
                size_t buf_size,
                ImGuiInputTextFlags flags = 0,
                ImGuiInputTextCallback callback = NULL,
                void* user_data = NULL
            )
    """
    pass

def invisible_button(identifier: str, width: float, height: float, ImGuiButtonFlags_flags=0): # real signature unknown; restored from __doc__
    """
    invisible_button(str identifier, float width, float height, ImGuiButtonFlags flags=0)
    Create invisible button.
    
        Flexible button behavior without the visuals, frequently useful to build custom behaviors using the public api (along with IsItemActive, IsItemHovered, etc.)
    
        .. visual-example::
            :auto_layout:
            :height: 300
            :width: 300
    
            imgui.begin("Example: invisible button :)")
            imgui.invisible_button("Button 1", 200, 200)
            imgui.small_button("Button 2")
            imgui.end()
    
        Args:
            identifier (str): Button identifier. Like label on :any:`button()`
                but it is not displayed.
            width (float): button width.
            height (float): button height.
            flags: ImGuiButtonFlags
    
        Returns:
            bool: True if button is clicked.
    
        .. wraps::
            bool InvisibleButton(const char* id: str, const ImVec2& size, ImGuiButtonFlags flags = 0)
    """
    pass

def is_any_item_active(): # real signature unknown; restored from __doc__
    """
    is_any_item_active()
    Was any of the items active.
    
        Returns:
            bool: True if any item is active, otherwise False.
    
        .. wraps::
            bool IsAnyItemActive()
    """
    pass

def is_any_item_focused(): # real signature unknown; restored from __doc__
    """
    is_any_item_focused()
    Is any of the items focused.
    
        Returns:
            bool: True if any item is focused, otherwise False.
    
        .. wraps::
            bool IsAnyItemFocused()
    """
    pass

def is_any_item_hovered(): # real signature unknown; restored from __doc__
    """
    is_any_item_hovered()
    Was any of the items hovered.
    
        Returns:
            bool: True if any item is hovered, otherwise False.
    
        .. wraps::
            bool IsAnyItemHovered()
    """
    pass

def is_item_activated(): # real signature unknown; restored from __doc__
    """
    is_item_activated()
    Was the last item just made active (item was previously inactive)?
    
        Returns:
            bool: True if item was just made active
    
        .. wraps::
            bool IsItemActivated()
    """
    pass

def is_item_active(): # real signature unknown; restored from __doc__
    """
    is_item_active()
    Was the last item active? For ex. button being held or text field
        being edited. Items that don't interact will always return false.
    
        Returns:
            bool: True if item is active, otherwise False.
    
        .. wraps::
            bool IsItemActive()
    """
    pass

def is_item_clicked(ImGuiMouseButton_mouse_button=0): # real signature unknown; restored from __doc__
    """
    is_item_clicked(ImGuiMouseButton mouse_button=0)
     Was the last item hovered and mouse clicked on?
        Button or node that was just being clicked on.
    
        Args:
            mouse_button: ImGuiMouseButton
    
        Returns:
            bool: True if item is clicked, otherwise False.
    
        .. wraps::
            bool IsItemClicked(int mouse_button = 0)
    """
    pass

def is_item_deactivated(): # real signature unknown; restored from __doc__
    """
    is_item_deactivated()
    Was the last item just made inactive (item was previously active)?
        Useful for Undo/Redo patterns with widgets that requires continuous editing.
    
        Results:
            bool: True if item just made inactive
    
        .. wraps:
            bool IsItemDeactivated()
    """
    pass

def is_item_deactivated_after_edit(): # real signature unknown; restored from __doc__
    """
    is_item_deactivated_after_edit()
    Was the last item just made inactive and made a value change when it was active? (e.g. Slider/Drag moved).
        Useful for Undo/Redo patterns with widgets that requires continuous editing.
        Note that you may get false positives (some widgets such as Combo()/ListBox()/Selectable() will return true even when clicking an already selected item).
    
        Results:
            bool: True if item just made inactive after an edition
    
        .. wraps::
            bool IsItemDeactivatedAfterEdit()
    """
    pass

def is_item_edited(): # real signature unknown; restored from __doc__
    """
    is_item_edited()
    Did the last item modify its underlying value this frame? or was pressed?
        This is generally the same as the "bool" return value of many widgets.
    
        Returns:
            bool: True if item is edited, otherwise False.
    
        .. wraps::
            bool IsItemEdited()
    """
    pass

def is_item_focused(): # real signature unknown; restored from __doc__
    """
    is_item_focused()
    Check if the last item is focused
    
        Returns:
            bool: True if item is focused, otherwise False.
    
        .. wraps::
            bool IsItemFocused()
    """
    pass

def is_item_hovered(ImGuiHoveredFlags_flags=0): # real signature unknown; restored from __doc__
    """
    is_item_hovered(ImGuiHoveredFlags flags=0)
    Check if the last item is hovered by mouse.
    
        Returns:
            bool: True if item is hovered by mouse, otherwise False.
    
        .. wraps::
            bool IsItemHovered(ImGuiHoveredFlags flags = 0)
    """
    pass

def is_item_toggled_open(): # real signature unknown; restored from __doc__
    """
    is_item_toggled_open()
    Was the last item open state toggled? set by TreeNode().
    
        .. wraps::
            bool IsItemToggledOpen()
    """
    pass

def is_item_visible(): # real signature unknown; restored from __doc__
    """
    is_item_visible()
    Was the last item visible? Aka not out of sight due to
        clipping/scrolling.
    
        Returns:
            bool: True if item is visible, otherwise False.
    
        .. wraps::
            bool IsItemVisible()
    """
    pass

def is_key_down(key_index: int): # real signature unknown; restored from __doc__
    """
    is_key_down(int key_index)
    Returns if key is being held -- io.KeysDown[user_key_index].
           Note that imgui doesn't know the semantic of each entry of
           io.KeysDown[]. Use your own indices/enums according to how
           your backend/engine stored them into io.KeysDown[]!
    
        Returns:
            bool: True if specified key is being held.
    
        .. wraps::
            bool IsKeyDown(int user_key_index)
    """
    pass

def is_key_pressed(key_index: int, bool_repeat=False): # real signature unknown; restored from __doc__
    """
    is_key_pressed(int key_index, bool repeat=False)
    Was key pressed (went from !Down to Down).
           If repeat=true, uses io.KeyRepeatDelay / KeyRepeatRate
    
        Returns:
            bool: True if specified key was pressed this frame
    
        .. wraps::
            bool IsKeyPressed(int user_key_index)
    """
    pass

def is_mouse_clicked(button: int=0, bool_repeat=False): # real signature unknown; restored from __doc__
    """
    is_mouse_clicked(int button=0, bool repeat=False)
    Returns if the mouse was clicked this frame.
    
        Args:
            button (int): mouse button index.
            repeat (float):
    
        Returns:
            bool: if the mouse was clicked this frame.
    
        .. wraps::
            bool IsMouseClicked(int button, bool repeat = false)
    """
    pass

def is_mouse_double_clicked(button: int=0): # real signature unknown; restored from __doc__
    """
    is_mouse_double_clicked(int button=0)
    Return True if mouse was double-clicked.
    
        **Note:** A double-click returns false in IsMouseClicked().
    
        Args:
            button (int): mouse button index.
    
        Returns:
            bool: if mouse is double clicked.
    
        .. wraps::
             bool IsMouseDoubleClicked(int button);
    """
    pass

def is_mouse_down(button: int=0): # real signature unknown; restored from __doc__
    """
    is_mouse_down(int button=0)
    Returns if the mouse is down.
    
        Args:
            button (int): mouse button index.
    
        Returns:
            bool: if the mouse is down.
    
        .. wraps::
            bool IsMouseDown(int button)
    """
    pass

def is_mouse_dragging(button: int, lock_threshold: float=-1.0): # real signature unknown; restored from __doc__
    """
    is_mouse_dragging(int button, float lock_threshold=-1.0)
    Returns if mouse is dragging.
    
        Args:
            button (int): mouse button index.
            lock_threshold (float): if less than -1.0
                uses io.MouseDraggingThreshold.
    
        Returns:
            bool: if mouse is dragging.
    
        .. wraps::
            bool IsMouseDragging(int button = 0, float lock_threshold = -1.0f)
    """
    pass

def is_mouse_hovering_rect(r_min_x: float, r_min_y: float, r_max_x: float, r_max_y: float, bool_clip=True): # real signature unknown; restored from __doc__
    """
    is_mouse_hovering_rect(float r_min_x, float r_min_y, float r_max_x, float r_max_y, bool clip=True)
    Test if mouse is hovering rectangle with given coordinates.
    
        Args:
            r_min_x, r_min_y (float): x,y coordinate of the upper-left corner
            r_max_x, r_max_y (float): x,y coordinate of the lower-right corner
    
        Returns:
            bool: True if mouse is hovering the rectangle.
    
        .. wraps::
            bool IsMouseHoveringRect(
                const ImVec2& r_min,
                const ImVec2& r_max,
                bool clip = true
            )
    """
    pass

def is_mouse_released(button: int=0): # real signature unknown; restored from __doc__
    """
    is_mouse_released(int button=0)
    Returns if the mouse was released this frame.
    
        Args:
            button (int): mouse button index.
    
        Returns:
            bool: if the mouse was released this frame.
    
        .. wraps::
            bool IsMouseReleased(int button)
    """
    pass

def is_popup_open(label: str, ImGuiPopupFlags_flags=0): # real signature unknown; restored from __doc__
    """
    is_popup_open(str label, ImGuiPopupFlags flags=0)
    Popups: test function
    
        * ``is_popup_open()`` with POPUP_ANY_POPUP_ID: return true if any popup is open at the current BeginPopup() level of the popup stack.
        * ``is_popup_open()`` with POPUP_ANY_POPUP_ID + POPUP_ANY_POPUP_LEVEL: return true if any popup is open.
    
        Returns:
            bool: True if the popup is open at the current ``begin_popup()`` level of the popup stack.
    
        .. wraps::
            bool IsPopupOpen(const char* id: str, ImGuiPopupFlags flags = 0)
    """
    pass

def is_rect_visible(size_width: float, size_height: float): # real signature unknown; restored from __doc__
    """
    is_rect_visible(float size_width, float size_height)
    Test if a rectangle of the given size, starting from the cursor
        position is visible (not clipped).
    
        Args:
            size_width (float): width of the rect
            size_height (float): height of the rect
    
        Returns:
            bool: True if rect is visible, otherwise False.
    
        .. wraps::
            bool IsRectVisible(const ImVec2& size)
    """
    pass

def is_window_appearing(): # real signature unknown; restored from __doc__
    """
    is_window_appearing()
    Check if current window is appearing.
    
        Returns:
            bool: True if window is appearing
    """
    pass

def is_window_collapsed(): # real signature unknown; restored from __doc__
    """
    is_window_collapsed()
    Check if current window is collapsed.
    
        Returns:
            bool: True if window is collapsed
    """
    pass

def is_window_focused(ImGuiHoveredFlags_flags=0): # real signature unknown; restored from __doc__
    """
    is_window_focused(ImGuiHoveredFlags flags=0)
    Is current window focused.
    
        Returns:
            bool: True if current window is on focus, otherwise False.
    
        .. wraps::
            bool IsWindowFocused(ImGuiFocusedFlags flags = 0)
    """
    pass

def is_window_hovered(ImGuiHoveredFlags_flags=0): # real signature unknown; restored from __doc__
    """
    is_window_hovered(ImGuiHoveredFlags flags=0)
    Is current window hovered and hoverable (not blocked by a popup).
        Differentiate child windows from each others.
    
        Returns:
            bool: True if current window is hovered, otherwise False.
    
        .. wraps::
            bool IsWindowHovered(ImGuiFocusedFlags flags = 0)
    """
    pass

def label_text(label: str, text: str): # real signature unknown; restored from __doc__
    """
    label_text(str label, str text)
    Display text+label aligned the same way as value+label widgets.
    
        .. visual-example::
            :auto_layout:
            :height: 80
            :width: 300
    
            imgui.begin("Example: text with label")
            imgui.label_text("my label", "my text")
            imgui.end()
    
        Args:
            label (str): label to display.
            text (str): text to display.
    
        .. wraps::
            void LabelText(const char* label, const char* fmt, ...)
    """
    pass

def listbox(label: str, current: int, items: list, height_in_items: int=-1) -> Tuple[bool, int]: # real signature unknown; restored from __doc__
    """
    listbox(str label, int current, list items, int height_in_items=-1)
    Show listbox widget.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
    
            current = 2
            imgui.begin("Example: listbox widget")
    
            clicked, current = imgui.listbox(
                "List", current, ["first", "second", "third"]
            )
    
            imgui.end()
    
        Args:
            label (str): The label.
            current (int): index of selected item.
            items (list): list of string labels for items.
            height_in_items (int): height of dropdown in items. Defaults to -1
                (autosized).
    
        Returns:
            tuple: a ``(changed, current)`` tuple indicating change of selection
            and current index of selected item.
    
        .. wraps::
            bool ListBox(
                const char* label,
                int* current_item,
                const char* items[],
                int items_count,
                int height_in_items = -1
            )
    """
    pass

def listbox_footer(): # real signature unknown; restored from __doc__
    """
    listbox_footer()
    *Obsoleted in imgui v1.81 from February 2021, refer to :func:`end_list_box()`*
    
        Closing the listbox, previously opened by :func:`listbox_header()`.
    
        See :func:`listbox_header()` for usage example.
    
        .. wraps::
            void ListBoxFooter()
    """
    pass

def listbox_header(label: str, width=0, height=0): # real signature unknown; restored from __doc__
    """
    listbox_header(str label, width=0, height=0)
    *Obsoleted in imgui v1.81 from February 2021, refer to :func:`begin_list_box()`*
    
        For use if you want to reimplement :func:`listbox()` with custom data
        or interactions. You need to call :func:`listbox_footer()` at the end.
    
        Args:
            label (str): The label.
            width (float): button width.
            height (float): button height.
    
        Returns:
            opened (bool): If the item is opened or closed.
    
        .. wraps::
            bool ListBoxHeader(
                const char* label,
                const ImVec2& size = ImVec2(0,0)
            )
    """
    pass

def load_ini_settings_from_disk(ini_file_name: str): # real signature unknown; restored from __doc__
    """
    load_ini_settings_from_disk(str ini_file_name)
    Call after ``create_context()`` and before the first call to ``new_frame()``.
        ``new_frame()`` automatically calls ``load_ini_settings_from_disk(io.ini_file_name)``.
    
        Args:
            ini_file_name (str): Filename to load settings from.
    
        .. wraps::
            void LoadIniSettingsFromDisk(const char* ini_filename)
    """
    pass

def load_ini_settings_from_memory(ini_data: str): # real signature unknown; restored from __doc__
    """
    load_ini_settings_from_memory(str ini_data)
    Call after ``create_context()`` and before the first call to ``new_frame()``
        to provide .ini data from your own data source.
    
        .. wraps::
            void LoadIniSettingsFromMemory(const char* ini_data, size_t ini_size=0)
    """
    pass

def menu_item(label: str, shortcut: Optional[str] = None, selected: bool = False, enabled: bool = True): # real signature unknown; restored from __doc__
    """
    menu_item(str label, str shortcut=None, bool selected=False, enabled=True)
    Create a menu item.
    
        Item shortcuts are displayed for convenience but not processed by ImGui at
        the moment. Using ``selected`` argument it is possible to show and trigger
        a check mark next to the menu item label.
    
        For practical example how to use this function, please see documentation
        of :func:`begin_main_menu_bar` or :func:`begin_menu_bar`.
    
        Args:
            label (str): label of the menu item.
            shortcut (str): shortcut text of the menu item.
            selected (bool): define if menu item is selected.
            enabled (bool): define if menu item is enabled or disabled.
    
        Returns:
            tuple: a ``(clicked, state)`` two-tuple indicating if item was
            clicked by the user and the current state of item (visibility of
            the check mark).
    
        .. wraps::
            MenuItem(
                const char* label,
                const char* shortcut,
                bool* p_selected,
                bool enabled = true
            )
    """
    pass

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

def new_frame(): # real signature unknown; restored from __doc__
    """
    new_frame()
    Start a new frame.
    
        After calling this you can submit any command from this point until
        next :any:`new_frame()` or :any:`render()`.
    
        .. wraps::
            void NewFrame()
    """
    pass

def new_line(): # real signature unknown; restored from __doc__
    """
    new_line()
    Undo :any:`same_line()` call.
    
        .. wraps::
            void NewLine()
    """
    pass

def next_column(): # real signature unknown; restored from __doc__
    """
    next_column()
    Move to the next column drawing.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        .. wraps::
            void NextColumn()
    """
    pass

def open_popup(label: str, ImGuiPopupFlags_flags=0): # real signature unknown; restored from __doc__
    """
    open_popup(str label, ImGuiPopupFlags flags=0)
    Open a popup window.
    
        Marks a popup window as open. Popups are closed when user click outside,
        or activate a pressable item, or :func:`close_current_popup()` is
        called within a :func:`begin_popup()`/:func:`end_popup()` block.
        Popup identifiers are relative to the current ID-stack
        (so :func:`open_popup` and :func:`begin_popup` needs to be at
        the same level).
    
        .. visual-example::
            :title: Simple popup window
            :height: 100
            :width: 220
            :auto_layout:
    
            imgui.begin("Example: simple popup")
            if imgui.button('Toggle..'):
                imgui.open_popup("toggle")
            if imgui.begin_popup("toggle"):
                if imgui.begin_menu('Sub-menu'):
                    _, _ = imgui.menu_item('Click me')
                    imgui.end_menu()
                imgui.end_popup()
            imgui.end()
    
        Args:
            label (str): label of the modal window.
    
        .. wraps::
            void OpenPopup(
                const char* id: str,
                ImGuiPopupFlags popup_flags = 0
            )
    """
    pass

def open_popup_on_item_click(label: Optional[str]=None, ImGuiPopupFlags_popup_flags=1): # real signature unknown; restored from __doc__
    """
    open_popup_on_item_click(str label=None, ImGuiPopupFlags popup_flags=1)
    Helper to open popup when clicked on last item.
        (note: actually triggers on the mouse _released_ event to be consistent with popup behaviors)
    
        Args:
            label (str): label of the modal window
            flags: ImGuiWindowFlags
    
        .. wraps::
            void OpenPopupOnItemClick(const char* id : str= NULL, ImGuiPopupFlags popup_flags = 1)
    """
    pass

def plot_histogram(label: str, const_float, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    plot_histogram(str label, const float[:] values, int values_count=-1, int values_offset=0, str overlay_text=None, float scale_min=FLT_MAX, float scale_max=FLT_MAX, graph_size=(0, 0), int stride=<???>)
    
        Plot a histogram of float values.
    
        Args:
            label (str): A plot label that will be displayed on the plot's right
                side. If you want the label to be invisible, add :code:`"##"`
                before the label's text: :code:`"my_label" -> "##my_label"`
    
            values (array of floats): the y-values.
                It must be a type that supports Cython's Memoryviews,
                (See: http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
                for example a numpy array.
    
            overlay_text (str or None, optional): Overlay text.
    
            scale_min (float, optional): y-value at the bottom of the plot.
            scale_max (float, optional): y-value at the top of the plot.
    
            graph_size (tuple of two floats, optional): plot size in pixels.
                **Note:** In ImGui 1.49, (-1,-1) will NOT auto-size the plot.
                To do that, use :func:`get_content_region_available` and pass
                in the right size.
    
        **Note:** These low-level parameters are exposed if needed for
        performance:
    
        * **values_offset** (*int*): Index of first element to display
        * **values_count** (*int*): Number of values to display. -1 will use the
            entire array.
        * **stride** (*int*): Number of bytes to move to read next element.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            from array import array
            from random import random
    
            # NOTE: this example will not work under py27 due do incompatible
            # implementation of array and memoryview().
            histogram_values = array('f', [random() for _ in range(20)])
    
            imgui.begin("Plot example")
            imgui.plot_histogram("histogram(random())", histogram_values)
            imgui.end()
    
        .. wraps::
                void PlotHistogram(
                    const char* label, const float* values, int values_count,
                    # note: optional
                    int values_offset,
                    const char* overlay_text,
                    float scale_min,
                    float scale_max,
                    ImVec2 graph_size,
                    int stride
                )
    """
    pass

def plot_lines(label: str, const_float, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    plot_lines(str label, const float[:] values, int values_count=-1, int values_offset=0, str overlay_text=None, float scale_min=MAX: float, float scale_max=MAX: float, graph_size=(0, 0), int stride=<???>)
    
        Plot a 1D array of float values.
    
        Args:
            label (str): A plot label that will be displayed on the plot's right
                side. If you want the label to be invisible, add :code:`"##"`
                before the label's text: :code:`"my_label" -> "##my_label"`
    
            values (array of floats): the y-values.
                It must be a type that supports Cython's Memoryviews,
                (See: http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
                for example a numpy array.
    
            overlay_text (str or None, optional): Overlay text.
    
            scale_min (float, optional): y-value at the bottom of the plot.
            scale_max (float, optional): y-value at the top of the plot.
    
            graph_size (tuple of two floats, optional): plot size in pixels.
                **Note:** In ImGui 1.49, (-1,-1) will NOT auto-size the plot.
                To do that, use :func:`get_content_region_available` and pass
                in the right size.
    
        **Note:** These low-level parameters are exposed if needed for
        performance:
    
        * **values_offset** (*int*): Index of first element to display
        * **values_count** (*int*): Number of values to display. -1 will use the
            entire array.
        * **stride** (*int*): Number of bytes to move to read next element.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            from array import array
            from math import sin
            # NOTE: this example will not work under py27 due do incompatible
            # implementation of array and memoryview().
            plot_values = array('f', [sin(x * 0.1) for x in range(100)])
    
            imgui.begin("Plot example")
            imgui.plot_lines("Sin(t)", plot_values)
            imgui.end()
    
        .. wraps::
                void PlotLines(
                    const char* label, const float* values, int values_count,
    
                    int values_offset = 0,
                    const char* overlay_text = NULL,
                    float scale_min = FLT_MAX,
                    float scale_max = FLT_MAX,
                    ImVec2 graph_size = ImVec2(0,0),
                    int stride = sizeof(float)
                )
    """
    pass

def pop_allow_keyboard_focus(): # real signature unknown; restored from __doc__
    """ pop_allow_keyboard_focus() """
    pass

def pop_button_repeat(): # real signature unknown; restored from __doc__
    """ pop_button_repeat() """
    pass

def pop_clip_rect(): # real signature unknown; restored from __doc__
    """
    pop_clip_rect()
    Pop the last clip region from the stack. See: :func:`push_clip_rect()`.
        
        .. wraps::
            void PopClipRect()
    """
    pass

def pop_font(): # real signature unknown; restored from __doc__
    """
    pop_font()
    Pop font on a stack.
    
        For example usage see :func:`push_font()`.
    
        Args:
            font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.
    
        .. wraps::
            void PopFont()
    """
    pass

def pop_id(): # real signature unknown; restored from __doc__
    """
    pop_id()
    Pop from the ID stack
    
          wraps::
            PopID()
    """
    pass

def pop_item_width(): # real signature unknown; restored from __doc__
    """
    pop_item_width()
    Reset width back to the default width.
    
        **Note:** This implementation guards you from segfaults caused by
        redundant stack pops (raises exception if this happens) but generally
        it is safer and easier to use :func:`styled` or :func:`istyled` context
        managers. See: :any:`push_item_width()`.
    
        .. wraps::
            void PopItemWidth()
    """
    pass

def pop_style_color(unsigned_count: int=1): # real signature unknown; restored from __doc__
    """
    pop_style_color(unsigned int count=1)
    Pop style color from stack.
    
        **Note:** This implementation guards you from segfaults caused by
        redundant stack pops (raises exception if this happens) but generally
        it is safer and easier to use :func:`styled` or :func:`istyled` context
        managers. See: :any:`push_style_color()`.
    
        Args:
            count (int): number of variables to pop from style color stack.
    
        .. wraps::
            void PopStyleColor(int count = 1)
    """
    pass

def pop_style_var(unsigned_count: int=1): # real signature unknown; restored from __doc__
    """
    pop_style_var(unsigned int count=1)
    Pop style variables from stack.
    
        **Note:** This implementation guards you from segfaults caused by
        redundant stack pops (raises exception if this happens) but generally
        it is safer and easier to use :func:`styled` or :func:`istyled` context
        managers. See: :any:`push_style_var()`.
    
        Args:
            count (int): number of variables to pop from style variable stack.
    
        .. wraps::
            void PopStyleVar(int count = 1)
    """
    pass

def pop_text_wrap_pos(): # real signature unknown; restored from __doc__
    """
    pop_text_wrap_pos()
    Pop the text wrapping position from the stack.
    
        **Note:** This implementation guards you from segfaults caused by
        redundant stack pops (raises exception if this happens) but generally
        it is safer and easier to use :func:`styled` or :func:`istyled` context
        managers. See: :func:`push_text_wrap_pos()`.
    
        .. wraps::
            void PopTextWrapPos()
    """
    pass

def pop_text_wrap_position(*args, **kwargs): # real signature unknown
    """
    pop_text_wrap_pos()
    Pop the text wrapping position from the stack.
    
        **Note:** This implementation guards you from segfaults caused by
        redundant stack pops (raises exception if this happens) but generally
        it is safer and easier to use :func:`styled` or :func:`istyled` context
        managers. See: :func:`push_text_wrap_pos()`.
    
        .. wraps::
            void PopTextWrapPos()
    """
    pass

def progress_bar(fraction: float, size, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    progress_bar(float fraction, size=(-MIN: float, 0), str overlay='')
     Show a progress bar
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 200
    
            imgui.begin("Progress bar example")
            imgui.progress_bar(0.7, (100,20), "Overlay text")
            imgui.end()
    
        Args:
            fraction (float): A floating point number between 0.0 and 1.0
                0.0 means no progress and 1.0 means progress is completed
            size : a tuple (width, height) that sets the width and height
                of the progress bar
            overlay (str): Optional text that will be shown in the progress bar
    
        .. wraps::
            void ProgressBar(
                float fraction,
                const ImVec2& size_arg = ImVec2(-FLT_MIN, 0),
                const char* overlay = NULL
            )
    """
    pass

def push_allow_keyboard_focus(bool_allow_focus): # real signature unknown; restored from __doc__
    """ push_allow_keyboard_focus(bool allow_focus) """
    pass

def push_button_repeat(bool_repeat): # real signature unknown; restored from __doc__
    """ push_button_repeat(bool repeat) """
    pass

def push_clip_rect(clip_rect_min_x: float, clip_rect_min_y: float, clip_rect_max_x: float, clip_rect_max_y: float, bool_intersect_with_current_clip_rect=False): # real signature unknown; restored from __doc__
    """
    push_clip_rect(float clip_rect_min_x, float clip_rect_min_y, float clip_rect_max_x, float clip_rect_max_y, bool intersect_with_current_clip_rect=False)
    Push the clip region, i.e. the area of the screen to be rendered,on the stack. 
        If ``intersect_with_current_clip_rect`` is ``True``, the intersection between pushed 
        clip region and previous one is added on the stack. 
        See: :func:`pop_clip_rect()`
        
        Args:
            clip_rect_min_x, clip_rect_min_y (float): Position of the minimum point of the rectangle
            clip_rect_max_x, clip_rect_max_y (float): Position of the maximum point of the rectangle
            intersect_with_current_clip_rect (bool): If True, intersection with current clip region is pushed on stack.
        
        .. visual-example::
            :auto_layout:
            :width: 150
            :height: 150
    
            imgui.begin("Example Cliprect")
            
            winpos = imgui.get_window_position()
            imgui.push_clip_rect(0+winpos.x,0+winpos.y,100+winpos.x,100+winpos.y)
            imgui.push_clip_rect(50+winpos.x,50+winpos.y,100+winpos.x,100+winpos.y, True)
            
            imgui.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
            imgui.text('Vivamus mattis velit ac ex auctor gravida.')
            imgui.text('Quisque varius erat finibus porta interdum.')
            imgui.text('Nam neque magna, dapibus placerat urna eget, facilisis malesuada ipsum.')
            
            imgui.pop_clip_rect()
            imgui.pop_clip_rect()
            
            imgui.end()
        
        .. wraps::
            void PushClipRect(
                const ImVec2& clip_rect_min, 
                const ImVec2& clip_rect_max, 
                bool intersect_with_current_clip_rect
            )
    """
    pass

def push_font(_Font_font): # real signature unknown; restored from __doc__
    """
    push_font(_Font font)
    Push font on a stack.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 320
    
            io = imgui.get_io()
    
            new_font = io.fonts.add_font_from_file_ttf(
                "DroidSans.ttf", 20,
            )
            impl.refresh_font_texture()
    
            # later in frame code
    
            imgui.begin("Default Window")
    
            imgui.text("Text displayed using default font")
    
            imgui.push_font(new_font)
            imgui.text("Text displayed using custom font")
            imgui.pop_font()
    
            imgui.end()
    
        **Note:** Pushed fonts should be poped with :func:`pop_font()` within the
        same frame. In order to avoid manual push/pop functions you can use the
        :func:`font()` context manager.
    
        Args:
            font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.
    
        .. wraps::
            void PushFont(ImFont*)
    """
    pass

def push_id(str_id: str): # real signature unknown; restored from __doc__
    """
    push_id(str id: str)
    Push an ID into the ID stack
    
        Args:
            id (str: str): ID to push
    
          wraps::
            PushID(const char* id: str)
    """
    pass

def push_item_width(item_width: float): # real signature unknown; restored from __doc__
    """
    push_item_width(float item_width)
    Push item width in the stack.
    
        **Note:** sizing of child region allows for three modes:
    
        * ``0.0`` - default to ~2/3 of windows width
        * ``>0.0`` - width in pixels
        * ``<0.0`` - align xx pixels to the right of window
          (so -MIN always align width to the right side: float)
    
        **Note:** width pushed on stack need to be poped using
        :func:`pop_item_width()` or it will be applied to all subsequent
        children components.
    
        .. visual-example::
            :auto_layout:
            :width: 200
            :height: 200
    
            imgui.begin("Example: item width")
    
            # custom width
            imgui.push_item_width(imgui.get_window_width() * 0.33)
            imgui.text('Lorem Ipsum ...')
            imgui.slider_float('float slider', 10.2, 0.0, 20.0, '%.2f', 1.0)
            imgui.pop_item_width()
    
            # default width
            imgui.text('Lorem Ipsum ...')
            imgui.slider_float('float slider', 10.2, 0.0, 20.0, '%.2f', 1.0)
    
            imgui.end()
    
        Args:
            item_width (float): width of the component
    
        .. wraps::
            void PushItemWidth(float item_width)
    """
    pass

def push_style_color(ImGuiCol_variable, r: float, g: float, b: float, a: float=1.): # real signature unknown; restored from __doc__
    """
    push_style_color(ImGuiCol variable, float r, float g, float b, float a=1.)
    Push style color on stack.
    
        **Note:** variables pushed on stack need to be popped using
        :func:`pop_style_color()` until the end of current frame. This
        implementation guards you from segfaults caused by redundant stack pops
        (raises exception if this happens) but generally it is safer and easier to
        use :func:`styled` or :func:`istyled` context managers.
    
        .. visual-example::
            :auto_layout:
            :width: 200
            :height: 80
    
            imgui.begin("Example: Color variables")
            imgui.push_style_color(imgui.COLOR_TEXT, 1.0, 0.0, 0.0)
            imgui.text("Colored text")
            imgui.pop_style_color(1)
            imgui.end()
    
        Args:
            variable: imgui style color constant
            r (float): red color intensity.
            g (float): green color intensity.
            b (float): blue color instensity.
            a (float): alpha intensity.
    
        .. wraps::
            PushStyleColor(ImGuiCol idx, const ImVec4& col)
    """
    pass

def push_style_var(ImGuiStyleVar_variable, value): # real signature unknown; restored from __doc__
    """
    push_style_var(ImGuiStyleVar variable, value)
    Push style variable on stack.
    
        This function accepts both float and float two-tuples as ``value``
        argument. ImGui core implementation will verify if passed value has
        type compatibile with given style variable. If not, it will raise
        exception.
    
        **Note:** variables pushed on stack need to be poped using
        :func:`pop_style_var()` until the end of current frame. This
        implementation guards you from segfaults caused by redundant stack pops
        (raises exception if this happens) but generally it is safer and easier to
        use :func:`styled` or :func:`istyled` context managers.
    
        .. visual-example::
            :auto_layout:
            :width: 200
            :height: 80
    
            imgui.begin("Example: style variables")
            imgui.push_style_var(imgui.STYLE_ALPHA, 0.2)
            imgui.text("Alpha text")
            imgui.pop_style_var(1)
            imgui.end()
    
        Args:
            variable: imgui style variable constant
            value (float or two-tuple): style variable value
    
    
        .. wraps::
            PushStyleVar(ImGuiStyleVar idx, float val)
    """
    pass

def push_text_wrap_pos(wrap_pos_x: float=0.0): # real signature unknown; restored from __doc__
    """
    push_text_wrap_pos(float wrap_pos_x=0.0)
    Word-wrapping function for text*() commands.
    
        **Note:** wrapping position allows these modes:
        * ``0.0`` - wrap to end of window (or column)
        * ``>0.0`` - wrap at 'wrap_pos_x' position in window local space
        * ``<0.0`` - no wrapping
    
        Args:
            wrap_pos_x (float): calculated item width.
    
        .. wraps::
            float PushTextWrapPos(float wrap_pos_x = 0.0f)
    """
    pass

def push_text_wrap_position(*args, **kwargs): # real signature unknown
    """
    push_text_wrap_pos(float wrap_pos_x=0.0)
    Word-wrapping function for text*() commands.
    
        **Note:** wrapping position allows these modes:
        * ``0.0`` - wrap to end of window (or column)
        * ``>0.0`` - wrap at 'wrap_pos_x' position in window local space
        * ``<0.0`` - no wrapping
    
        Args:
            wrap_pos_x (float): calculated item width.
    
        .. wraps::
            float PushTextWrapPos(float wrap_pos_x = 0.0f)
    """
    pass

def radio_button(label: str, bool_active): # real signature unknown; restored from __doc__
    """
    radio_button(str label, bool active)
    Display radio button widget
    
        .. visual-example::
            :auto_layout:
            :height: 100
    
            # note: the variable that contains the state of the radio_button, should be initialized
            #       outside of the main interaction loop
            radio_active = True
    
            imgui.begin("Example: radio buttons")
    
            if imgui.radio_button("Radio button", radio_active):
                radio_active = not radio_active
    
            imgui.end()
    
        Args:
            label (str): button label.
            active (bool): state of the radio button.
    
        Returns:
            bool: True if clicked.
    
        .. wraps::
            bool RadioButton(const char* label, bool active)
    """
    pass

def render(): # real signature unknown; restored from __doc__
    """
    render()
    Finalize frame, set rendering data, and run render callback (if set).
    
        .. wraps::
            void Render()
    """
    pass

def reset_mouse_drag_delta(button: int=0): # real signature unknown; restored from __doc__
    """
    reset_mouse_drag_delta(int button=0)
    Reset the mouse dragging delta.
    
        Args:
            button (int): mouse button index.
    
        .. wraps::
            void ResetMouseDragDelta(int button = 0)
    """
    pass

def same_line(position: float=0.0, spacing: float=-1.0): # real signature unknown; restored from __doc__
    """
    same_line(float position=0.0, float spacing=-1.0)
    Call between widgets or groups to layout them horizontally.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            imgui.begin("Example: same line widgets")
    
            imgui.text("same_line() with defaults:")
            imgui.button("yes"); imgui.same_line()
            imgui.button("no")
    
            imgui.text("same_line() with fixed position:")
            imgui.button("yes"); imgui.same_line(position=50)
            imgui.button("no")
    
            imgui.text("same_line() with spacing:")
            imgui.button("yes"); imgui.same_line(spacing=50)
            imgui.button("no")
    
            imgui.end()
    
        Args:
            position (float): fixed horizontal position position.
            spacing (float): spacing between elements.
    
        .. wraps::
            void SameLine(float pos_x = 0.0f, float spacing_w = -1.0f)
    """
    pass

def save_ini_settings_to_disk(ini_file_name: str): # real signature unknown; restored from __doc__
    """
    save_ini_settings_to_disk(str ini_file_name)
    This is automatically called (if ``io.ini_file_name`` is not empty)
        a few seconds after any modification that should be reflected in the .ini file
        (and also by ``destroy_context``).
    
        Args:
            ini_file_name (str): Filename to save settings to.
    
        .. wraps::
            void SaveIniSettingsToDisk(const char* ini_filename)
    """
    pass

def save_ini_settings_to_memory(): # real signature unknown; restored from __doc__
    """
    save_ini_settings_to_memory()
    Return a string with the .ini data which you can save by your own mean.
        Call when ``io.want_save_ini_settings`` is set, then save data by your own mean
        and clear ``io.want_save_ini_settings``.
    
        Returns:
            str: Settings data
    
        .. wraps::
           const char* SaveIniSettingsToMemory(size_t* out_ini_size = NULL)
    """
    pass

def selectable(label: str, selected=False, ImGuiTreeNodeFlags_flags=0, width=0, height=0): # real signature unknown; restored from __doc__
    """
    selectable(str label, selected=False, ImGuiTreeNodeFlags flags=0, width=0, height=0)
    Selectable text. Returns 'true' if the item is pressed.
    
        Width of 0.0 will use the available width in the parent container.
        Height of 0.0 will use the available height in the parent container.
    
        .. visual-example::
            :auto_layout:
            :height: 200
            :width: 200
            :click: 80 40
    
            selected = [False, False]
            imgui.begin("Example: selectable")
            _, selected[0] = imgui.selectable(
                "1. I am selectable", selected[0]
            )
            _, selected[1] = imgui.selectable(
                "2. I am selectable too", selected[1]
            )
            imgui.text("3. I am not selectable")
            imgui.end()
    
        Args:
            label (str): The label.
            selected (bool): defines if item is selected or not.
            flags: Selectable flags. See:
                :ref:`list of available flags <selectable-flag-options>`.
            width (float): button width.
            height (float): button height.
    
        Returns:
            tuple: a ``(opened, selected)`` two-tuple indicating if item was
            clicked by the user and the current state of item.
    
        .. wraps::
            bool Selectable(
                const char* label,
                bool selected = false,
                ImGuiSelectableFlags flags = 0,
                const ImVec2& size = ImVec2(0,0)
            )
    
            bool Selectable(
                const char* label,
                bool* selected,
                ImGuiSelectableFlags flags = 0,
                const ImVec2& size = ImVec2(0,0)
            )
    """
    pass

def separator(): # real signature unknown; restored from __doc__
    """
    separator()
    Add vertical line as a separator beween elements.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            imgui.begin("Example: separators")
    
            imgui.text("Some text with bullets")
            imgui.bullet_text("Bullet A")
            imgui.bullet_text("Bullet A")
    
            imgui.separator()
    
            imgui.text("Another text with bullets")
            imgui.bullet_text("Bullet A")
            imgui.bullet_text("Bullet A")
    
            imgui.end()
    
        .. wraps::
            void Separator()
    """
    pass

def set_clipboard_text(text: str): # real signature unknown; restored from __doc__
    """
    set_clipboard_text(str text)
    Set the clipboard content
    
        Args:
            text (str): Text to copy in clipboard
    
        .. wraps:
            void SetClipboardText(const char* text)
    """
    pass

def set_column_offset(column_index: int, offset_x: float): # real signature unknown; restored from __doc__
    """
    set_column_offset(int column_index, float offset_x)
    Set the position of column line (in pixels, from the left side of the
        contents region). Pass -1 to use current column.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        Args:
            column_index (int): index of the column to get the offset for.
            offset_x (float): offset in pixels.
    
        .. wraps::
            void SetColumnOffset(int column_index, float offset_x)
    """
    pass

def set_column_width(column_index: int, width: float): # real signature unknown; restored from __doc__
    """
    set_column_width(int column_index, float width)
    Set the position of column line (in pixels, from the left side of the
        contents region). Pass -1 to use current column.
    
        For a complete example see :func:`columns()`.
    
        Legacy Columns API (2020: prefer using Tables!)
    
        Args:
            column_index (int): index of the column to set the width for.
            width (float): width in pixels.
    
        .. wraps::
            void SetColumnWidth(int column_index, float width)
    """
    pass

def set_current_context(_ImGuiContext_ctx): # real signature unknown; restored from __doc__
    """
    set_current_context(_ImGuiContext ctx)
    SetCurrentContext
    
        .. wraps::
            SetCurrentContext(
                    ImGuiContext *ctx);
    """
    pass

def set_cursor_pos(local_pos): # real signature unknown; restored from __doc__
    """
    set_cursor_pos(local_pos)
    Set the cursor position in local coordinates [0..<window size>] (useful to work with ImDrawList API)
    
        .. wraps::
            ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    """
    pass

def set_cursor_position(*args, **kwargs): # real signature unknown
    """
    set_cursor_pos(local_pos)
    Set the cursor position in local coordinates [0..<window size>] (useful to work with ImDrawList API)
    
        .. wraps::
            ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    """
    pass

def set_cursor_pos_x(x: float): # real signature unknown; restored from __doc__
    """ set_cursor_pos_x(float x) """
    pass

def set_cursor_pos_y(y: float): # real signature unknown; restored from __doc__
    """ set_cursor_pos_y(float y) """
    pass

def set_cursor_screen_pos(screen_pos): # real signature unknown; restored from __doc__
    """
    set_cursor_screen_pos(screen_pos)
    Set the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)
    
        .. wraps::
            ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    """
    pass

def set_cursor_screen_position(*args, **kwargs): # real signature unknown
    """
    set_cursor_screen_pos(screen_pos)
    Set the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)
    
        .. wraps::
            ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    """
    pass

def set_drag_drop_payload(type: str, bytes_data, ImGuiCond_condition=0): # real signature unknown; restored from __doc__
    """
    set_drag_drop_payload(str type, bytes data, ImGuiCond condition=0)
    Set the payload for a drag and drop source. Only call after
        :func:`begin_drag_drop_source` returns True.
    
        **Note:** this is a beta API.
    
        For a complete example see :func:`begin_drag_drop_source`.
    
        Args:
            type (str): user defined type with maximum 32 bytes.
            data (bytes): the data for the payload; will be copied and stored internally.
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
    
        .. wraps::
            bool SetDragDropPayload(const char* type, const void* data, size_t size, ImGuiCond cond = 0)
    """
    pass

def set_item_allow_overlap(): # real signature unknown; restored from __doc__
    """
    set_item_allow_overlap()
    Allow last item to be overlapped by a subsequent item.
        Sometimes useful with invisible buttons, selectables, etc.
        to catch unused area.
    
        .. wraps::
            void SetItemAllowOverlap()
    """
    pass

def set_item_default_focus(): # real signature unknown; restored from __doc__
    """
    set_item_default_focus()
    Make last item the default focused item of a window.
        Please use instead of "if (is_window_appearing()) set_scroll_here()" to signify "default item".
    
        .. wraps::
            void SetItemDefaultFocus()
    """
    pass

def set_keyboard_focus_here(offset: int=0): # real signature unknown; restored from __doc__
    """
    set_keyboard_focus_here(int offset=0)
    Focus keyboard on the next widget.
        Use positive 'offset' to access sub components of a multiple component widget. Use -1 to access previous widget.
    
        .. wraps::
            void SetKeyboardFocusHere(int offset = 0)
    """
    pass

def set_mouse_cursor(ImGuiMouseCursor_mouse_cursor_type): # real signature unknown; restored from __doc__
    """
    set_mouse_cursor(ImGuiMouseCursor mouse_cursor_type)
    Set the mouse cursor id.
    
        Args:
            mouse_cursor_type (ImGuiMouseCursor): mouse cursor type.
    
        .. wraps::
            void SetMouseCursor(ImGuiMouseCursor type)
    """
    pass

def set_next_item_open(bool_is_open, ImGuiCond_condition=0): # real signature unknown; restored from __doc__
    """
    set_next_item_open(bool is_open, ImGuiCond condition=0)
    Set next TreeNode/CollapsingHeader open state.
    
        Args:
            is_open (bool):
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.NONE`.
    
        .. wraps::
            void SetNextItemOpen(bool is_open, ImGuiCond cond = 0)
    """
    pass

def set_next_item_width(item_width: float): # real signature unknown; restored from __doc__
    """
    set_next_item_width(float item_width)
    Set width of the _next_ common large "item+label" widget. 
        * ``>0.0`` - width in pixels
        * ``<0.0`` - align xx pixels to the right of window
        (so -MIN always align width to the right side: float)
        
        Helper to avoid using ``push_item_width()``/``pop_item_width()`` for single items.
        
        Args:
            item_width (float): width of the component
        
        .. visual-example::
            :auto_layout:
            :width: 200
            :height: 200
            
            imgui.begin("Exemple: Next item width")
            imgui.set_next_item_width(imgui.get_window_width() * 0.33)
            imgui.slider_float('Slider 1', 10.2, 0.0, 20.0, '%.2f', 1.0)
            imgui.slider_float('Slider 2', 10.2, 0.0, 20.0, '%.2f', 1.0)
            imgui.end()
        
        .. wraps::
            void SetNextItemWidth(float item_width)
    """
    pass

def set_next_window_bg_alpha(alpha: float): # real signature unknown; restored from __doc__
    """
    set_next_window_bg_alpha(float alpha)
    set next window background color alpha. helper to easily modify ImGuiCol_WindowBg/ChildBg/PopupBg.
    
        .. wraps::
            void SetNextWindowBgAlpha(float)
    """
    pass

def set_next_window_collapsed(bool_collapsed, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_next_window_collapsed(bool collapsed, ImGuiCond condition=ALWAYS)
    Set next window collapsed state.
    
        .. visual-example::
            :auto_layout:
            :height: 60
            :width: 400
    
            imgui.set_next_window_collapsed(True)
            imgui.begin("Example: collapsed window")
            imgui.end()
    
    
        Args:
            collapsed (bool): set to True if window has to be collapsed.
            condition (:ref:`condition flag <condition-options>`): defines on
                which condition value should be set. Defaults to
                :any:`imgui.ALWAYS`.
    
        .. wraps::
             void SetNextWindowCollapsed(
                 bool collapsed, ImGuiCond cond = 0
             )
    """
    pass

def set_next_window_content_size(width: float, height: float): # real signature unknown; restored from __doc__
    """
    set_next_window_content_size(float width, float height)
    Set content size of the next window. Show scrollbars
           if content doesn't fit in the window
    
        Call before :func:`begin()`.
    
        Args:
            width(float): width of the content area
            height(float): height of the content area
    
        .. visual-example::
            :title: Content Size Demo
            :height: 30
    
            imgui.set_window_size(20,20)
            imgui.set_next_window_content_size(100,100)
    
            imgui.begin("Window", True)
            imgui.text("Some example text")
            imgui.end()
    
        .. wraps::
            void SetNextWindowContentSize(
                const ImVec2& size
            )
    """
    pass

def set_next_window_focus(): # real signature unknown; restored from __doc__
    """
    set_next_window_focus()
    Set next window to be focused (most front).
    
        .. wraps::
            void SetNextWindowFocus()
    """
    pass

def set_next_window_position(x: float, y: float, ImGuiCond_condition=None, pivot_x: float=0, pivot_y: float=0): # real signature unknown; restored from __doc__
    """
    set_next_window_position(float x, float y, ImGuiCond condition=ALWAYS, float pivot_x=0, float pivot_y=0)
    Set next window position.
    
        Call before :func:`begin()`.
    
        Args:
            x (float): x window coordinate
            y (float): y window coordinate
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
            pivot_x (float): pivot x window coordinate
            pivot_y (float): pivot y window coordinate
    
        .. visual-example::
            :title: window positioning
            :height: 50
    
            imgui.set_next_window_size(20, 20)
    
            for index in range(5):
                imgui.set_next_window_position(index * 40, 5)
                imgui.begin(str(index))
                imgui.end()
    
        .. wraps::
            void SetNextWindowPos(
                const ImVec2& pos,
                ImGuiCond cond = 0,
                const ImVec2& pivot = ImVec2(0,0)
            )
    """
    pass

def set_next_window_size(width: float, height: float, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_next_window_size(float width, float height, ImGuiCond condition=ALWAYS)
    Set next window size.
    
        Call before :func:`begin()`.
    
        Args:
            width (float): window width. Value 0.0 enables autofit.
            height (float): window height. Value 0.0 enables autofit.
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
    
        .. visual-example::
            :title: window sizing
            :height: 200
    
            imgui.set_next_window_position(io.display_size.x * 0.5, io.display_size.y * 0.5, 1, pivot_x = 0.5, pivot_y = 0.5)
    
            imgui.set_next_window_size(80, 180)
            imgui.begin("High")
            imgui.end()
    
    
        .. wraps::
            void SetNextWindowSize(
                const ImVec2& size, ImGuiCond cond = 0
            )
    """
    pass

def set_next_window_size_constraints(tuple_size_min, tuple_size_max, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """
    set_next_window_size_constraints(tuple size_min, tuple size_max, callback=None, user_data=None)
    Set next window size limits. use -1,-1 on either X/Y axis to preserve the current size.
        Sizes will be rounded down.
    
        Call before :func:`begin()`.
    
        Args:
            size_min (tuple): Minimum window size, use -1 to conserve current size
            size_max (tuple): Maximum window size, use -1 to conserve current size
            callback (callable): a callable.
                Callable takes an imgui._ImGuiSizeCallbackData object as argument
                Callable should return None
            user_data: Any data that the user want to use in the callback.
    
        .. visual-example::
            :title: Window size constraints
            :height: 200
    
            imgui.set_next_window_size_constraints((175,50), (200, 100))
            imgui.begin("Constrained Window")
            imgui.text("...")
            imgui.end()
    
        .. wraps::
            void SetNextWindowSizeConstraints(
                const ImVec2& size_min,
                const ImVec2& size_max,
                ImGuiSizeCallback custom_callback = NULL,
                void* custom_callback_user_data = NULL
            )
    """
    pass

def set_scroll_from_pos_x(local_x: float, center_x_ratio: float=0.5): # real signature unknown; restored from __doc__
    """
    set_scroll_from_pos_x(float local_x, float center_x_ratio=0.5)
    Set scroll from position X
    
        Adjust scrolling amount to make given position visible.
        Generally GetCursorStartPos() + offset to compute a valid position.
    
        Args:
            float local_x
            float center_x_ratio = 0.5f
    
        .. wraps::
            void SetScrollFromPosX(float local_x, float center_x_ratio = 0.5f)
    """
    pass

def set_scroll_from_pos_y(local_y: float, center_y_ratio: float=0.5): # real signature unknown; restored from __doc__
    """
    set_scroll_from_pos_y(float local_y, float center_y_ratio=0.5)
    Set scroll from position Y
    
        Adjust scrolling amount to make given position visible.
        Generally GetCursorStartPos() + offset to compute a valid position.
    
        Args:
            float local_y
            float center_y_ratio = 0.5f
    
        .. wraps::
            void SetScrollFromPosY(float local_y, float center_y_ratio = 0.5f)
    """
    pass

def set_scroll_here_x(center_x_ratio: float=0.5): # real signature unknown; restored from __doc__
    """
    set_scroll_here_x(float center_x_ratio=0.5)
    Set scroll here X.
    
        Adjust scrolling amount to make current cursor position visible.
        center_x_ratio =
        0.0: left,
        0.5: center,
        1.0: right.
    
        When using to make a "default/current item" visible, consider using SetItemDefaultFocus() instead.
    
        Args:
            float center_x_ratio = 0.5f
    
        .. wraps::
            void SetScrollHereX(float center_x_ratio = 0.5f)
    """
    pass

def set_scroll_here_y(center_y_ratio: float=0.5): # real signature unknown; restored from __doc__
    """
    set_scroll_here_y(float center_y_ratio=0.5)
    Set scroll here Y.
    
        Adjust scrolling amount to make current cursor position visible.
        center_y_ratio =
        0.0: top,
        0.5: center,
        1.0: bottom.
    
        When using to make a "default/current item" visible, consider using SetItemDefaultFocus() instead.
    
        Args:
            float center_y_ratio = 0.5f
    
        .. wraps::
            void SetScrollHereY(float center_y_ratio = 0.5f)
    """
    pass

def set_scroll_x(scroll_x: float): # real signature unknown; restored from __doc__
    """
    set_scroll_x(float scroll_x)
    set scrolling amount [0..SetScrollMaxX()]
    
        .. wraps::
            int SetScrollX(float)
    """
    pass

def set_scroll_y(scroll_y: float): # real signature unknown; restored from __doc__
    """
    set_scroll_y(float scroll_y)
    set scrolling amount [0..SetScrollMaxY()]
    
        .. wraps::
            int SetScrollY(flot)
    """
    pass

def set_tab_item_closed(tab_or_docked_window_label: str): # real signature unknown; restored from __doc__
    """
    set_tab_item_closed(str tab_or_docked_window_label)
    Notify TabBar or Docking system of a closed tab/window ahead (useful to reduce visual flicker on reorderable tab bars).
        For tab-bar: call after BeginTabBar() and before Tab submissions.
        Otherwise call with a window name.
    
        Args:
            tab_or_docked_window_label (str): Label of the targeted tab or docked window
    
        .. visual-example:
            :auto_layout:
            :width: 300
    
            imgui.begin("Example Tab Bar")
            if imgui.begin_tab_bar("MyTabBar"):
    
                if imgui.begin_tab_item("Item 1")[0]:
                    imgui.text("Here is the tab content!")
                    imgui.end_tab_item()
    
                if imgui.begin_tab_item("Item 2")[0]:
                    imgui.text("This item won't whow !")
                    imgui.end_tab_item()
    
                imgui.set_tab_item_closed("Item 2")
    
                imgui.end_tab_bar()
            imgui.end()
    
        .. wraps:
            void SetTabItemClosed(const char* tab_or_docked_window_label)
    """
    pass

def set_tooltip(text: str): # real signature unknown; restored from __doc__
    """
    set_tooltip(str text)
    Set tooltip under mouse-cursor.
    
        Usually used with :func:`is_item_hovered()`.
        For a complex tooltip window see :func:`begin_tooltip()`.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
            :click: 80 40
    
            imgui.begin("Example: tooltip")
            imgui.button("Hover me!")
            if imgui.is_item_hovered():
                imgui.set_tooltip("Please?")
            imgui.end()
    
        .. wraps::
            void SetTooltip(const char* fmt, ...)
    """
    pass

def set_window_collapsed(bool_collapsed, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_window_collapsed(bool collapsed, ImGuiCond condition=ALWAYS)
    Set the current window to be collapsed
    
        Call inside: func: 'begin()'
    
        Args:
            collapsed(bool): set boolean for collapsing the window. Set True for closed
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
    
        .. visual-example::
            :title: Window Collapsed Demo
            :height: 200
    
            imgui.begin("Window 1")
            imgui.set_window_collapsed(True)
            imgui.end()
    
        .. wraps::
            void SetWindowCollapsed(
                bool collapsed,
                ImGuiCond cond
            )
    """
    pass

def set_window_collapsed_labeled(label: str, bool_collapsed, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_window_collapsed_labeled(str label, bool collapsed, ImGuiCond condition=ALWAYS)
    Set window with label to collapse
    
        Args:
            label(string): name of the window
            collapsed(bool): set boolean for collapsing the window. Set True for closed
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
    
        .. visual-example::
            :title: Window Collapsed Demo
            :height: 200
    
            imgui.set_window_collapsed_labeled("Window 1", True)
            imgui.begin("Window 1")
            imgui.end()
    
        .. wraps::
            void SetWindowCollapsed(
                const char* name,
                bool collapsed,
                ImGuiCond cond
            )
    """
    pass

def set_window_focus(): # real signature unknown; restored from __doc__
    """
    set_window_focus()
    Set window to be focused
    
        Call inside :func:`begin()`.
    
        .. visual-example::
            :title: Window focus
            :height: 100
    
            imgui.begin("Window 1")
            imgui.end()
    
            imgui.begin("Window 2")
            imgui.set_window_focus()
            imgui.end()
    
        .. wraps::
            void SetWindowFocus()
    """
    pass

def set_window_focus_labeled(label: str): # real signature unknown; restored from __doc__
    """
    set_window_focus_labeled(str label)
    Set focus to the window named label
    
        Args:
            label(string): the name of the window that will be focused
    
        .. visual-example::
            :title: Window focus
            :height: 100
    
            imgui.set_window_focus_labeled("Window 2")
    
            imgui.begin("Window 1", True)
            imgui.text("Apples")
            imgui.end()
    
            imgui.begin("Window 2", True)
            imgui.text("Orange")
            imgui.end()
    
            imgui.begin("Window 3", True)
            imgui.text("Mango")
            imgui.end()
    
        .. wraps::
            void SetWindowFocus(
                const char* name
            )
    """
    pass

def set_window_font_scale(scale: float): # real signature unknown; restored from __doc__
    """
    set_window_font_scale(float scale)
    Adjust per-window font scale for current window.
    
        Function should be called inside window context so after calling
        :any:`begin()`.
    
        Note: use ``get_io().font_global_scale`` if you want to scale all windows.
    
        .. visual-example::
            :auto_layout:
            :height: 100
    
            imgui.begin("Example: font scale")
            imgui.set_window_font_scale(2.0)
            imgui.text("Bigger font")
            imgui.end()
    
        Args:
            scale (float): font scale
    
        .. wraps::
            void SetWindowFontScale(float scale)
    """
    pass

def set_window_position(x: float, y: float, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_window_position(float x, float y, ImGuiCond condition=ALWAYS)
    Set the size of the current window
    
        Call inside: func: 'begin()'
    
        Args:
            x(float): position on the x axis
            y(float): position on the y axis
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
    
        .. visual-example::
            :title: Window Size Demo
            :height: 200
    
            imgui.begin("Window 1")
            imgui.set_window_position(20,20)
            imgui.end()
    
            imgui.begin("Window 2")
            imgui.set_window_position(20,50)
            imgui.end()
    
        .. wraps::
            void SetWindowPos(
                const ImVec2& pos,
                ImGuiCond cond
            )
    """
    pass

def set_window_position_labeled(label: str, x: float, y: float, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_window_position_labeled(str label, float x, float y, ImGuiCond condition=ALWAYS)
    Set the size of the window with label
    
        Args:
            label(str): name of the window to be resized
            x(float): position on the x axis
            y(float): position on the y axis
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ALWAYS`.
    
        .. visual-example::
            :title: Window Size Demo
            :height: 200
    
            imgui.set_window_position_labeled("Window 1", 20, 50)
            imgui.set_window_position_labeled("Window 2", 20, 100)
    
            imgui.begin("Window 1")
            imgui.end()
    
            imgui.begin("Window 2")
            imgui.end()
    
        .. wraps::
            void SetWindowPos(
                const char* name,
                const ImVec2& pos,
                ImGuiCond cond
            )
    """
    pass

def set_window_size(width: float, height: float, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_window_size(float width, float height, ImGuiCond condition=ONCE)
    Set window size
    
        Call inside :func:`begin()`.
    
        **Note:** usage of this function is not recommended. prefer using
        :func:`set_next_window_size()` as this may incur tearing and minor
        side-effects.
    
        Args:
            width (float): window width. Value 0.0 enables autofit.
            height (float): window height. Value 0.0 enables autofit.
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ONCE`.
    
        .. visual-example::
            :title: window sizing
            :height: 200
    
            imgui.begin("Window size")
            imgui.set_window_size(80, 180)
            imgui.end()
    
        .. wraps::
            void SetWindowSize(
                const ImVec2& size,
                ImGuiCond cond = 0,
            )
    """
    pass

def set_window_size_named(label: str, width: float, height: float, ImGuiCond_condition=None): # real signature unknown; restored from __doc__
    """
    set_window_size_named(str label, float width, float height, ImGuiCond condition=ONCE)
    Set the window with label to some size
    
        Args:
            label(string): name of the window
            width(float): new width of the window
            height(float): new height of the window
            condition (:ref:`condition flag <condition-options>`): defines on which
                condition value should be set. Defaults to :any:`imgui.ONCE`.
    
        .. visual-example::
            :title: Window size
            :height: 200
    
            imgui.set_window_size_named("Window 1",100,100)
            imgui.set_window_size_named("Window 2",100,200)
    
            imgui.begin("Window 1")
            imgui.end()
    
            imgui.begin("Window 2")
            imgui.end()
    
        .. wraps::
            void SetWindowSize(
                const char* name,
                const ImVec2& size,
                 ImGuiCond cond
            )
    """
    pass

def show_about_window(closable=False): # real signature unknown; restored from __doc__
    """
    show_about_window(closable=False)
     Create About window. 
        Display Dear ImGui version, credits and build/system information.
        
        Args:
            closable (bool): define if window is closable
        
        Return:
            bool: True if window is not closed (False trigerred by close button).
        
        .. wraps::
            void ShowAboutWindow(bool* p_open = NULL)
    """
    pass

def show_demo_window(closable=False): # real signature unknown; restored from __doc__
    """
    show_demo_window(closable=False)
    Show ImGui demo window.
    
        .. visual-example::
            :width: 700
            :height: 600
            :auto_layout:
    
            imgui.show_demo_window()
    
        Args:
            closable (bool): define if window is closable.
    
        Returns:
            bool: True if window is not closed (False trigerred by close button).
    
        .. wraps::
            void ShowDemoWindow(bool* p_open = NULL)
    """
    pass

def show_font_selector(label: str): # real signature unknown; restored from __doc__
    """ show_font_selector(str label) """
    pass

def show_metrics_window(closable=False): # real signature unknown; restored from __doc__
    """
    show_metrics_window(closable=False)
    Show ImGui metrics window.
    
        .. visual-example::
            :width: 700
            :height: 200
            :auto_layout:
    
            imgui.show_metrics_window()
    
        Args:
            closable (bool): define if window is closable.
    
        Returns:
            bool: True if window is not closed (False trigerred by close button).
    
        .. wraps::
            void ShowMetricsWindow(bool* p_open = NULL)
    """
    pass

def show_style_editor(GuiStyle_style=None): # real signature unknown; restored from __doc__
    """
    show_style_editor(GuiStyle style=None)
    Show ImGui style editor.
    
        .. visual-example::
            :width: 300
            :height: 300
            :auto_layout:
    
            imgui.begin("Example: my style editor")
            imgui.show_style_editor()
            imgui.end()
    
        Args:
            style (GuiStyle): style editor state container.
    
        .. wraps::
            void ShowStyleEditor(ImGuiStyle* ref = NULL)
    """
    pass

def show_style_selector(label: str): # real signature unknown; restored from __doc__
    """ show_style_selector(str label) """
    pass

def show_test_window(): # real signature unknown; restored from __doc__
    """
    show_test_window()
    Show ImGui demo window.
    
        .. visual-example::
            :width: 700
            :height: 600
            :auto_layout:
    
            imgui.show_test_window()
    
        .. wraps::
            void ShowDemoWindow()
    """
    pass

def show_user_guide(): # real signature unknown; restored from __doc__
    """
    show_user_guide()
    Show ImGui user guide editor.
    
        .. visual-example::
            :width: 700
            :height: 500
            :auto_layout:
    
            imgui.begin("Example: user guide")
            imgui.show_user_guide()
            imgui.end()
    
    
        .. wraps::
            void ShowUserGuide()
    """
    pass

def slider_angle(label: str, rad_value: float, value_degrees_min: float=-360.0, value_degrees_max: float=360, format: str='%.0f deg', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_angle(str label, float rad_value, float value_degrees_min=-360.0, float value_degrees_max=360, str format='%.0f deg', ImGuiSliderFlags flags=0)
    Display angle slider widget.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            radian = 3.1415/4
    
            imgui.begin("Example: slider angle")
            changed, radian = imgui.slider_angle(
                "slider angle", radian,
                value_degrees_min=0.0, value_degrees_max=180.0)
            imgui.text("Changed: %s, Value: %s" % (changed, radian))
            imgui.end()
    
        Args:
            labal (str): widget label
            rad_value (float): slider value in radian
            value_degrees_min (float): min value allowed in degrees
            value_degrees_max (float): max value allowed in degrees
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, rad_value)`` tuple that contains indicator of
            widget state change and the current slider value in radian.
    
    
        .. wraps::
            bool SliderAngle(
                const char* label,
                float* v_rad, float
                v_degrees_min = -360.0f,
                float v_degrees_max = +360.0f,
                const char* format = "%.0f deg",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_float(label: str, value: float, min_value: float, max_value: float, format: str = '%.3f', flags=0, power: float = 1.0) -> Tuple[bool, float]: # real signature unknown; restored from __doc__
    """
    slider_float(str label, float value, float min_value, float max_value, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.0)
    Display float slider widget.
        Manually input values aren't clamped and can go off-bounds.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            value = 88.2
    
            imgui.begin("Example: slider float")
            changed, value = imgui.slider_float(
                "slide floats", value,
                min_value=0.0, max_value=100.0,
                format="%.0f"
            )
            imgui.text("Changed: %s, Value: %s" % (changed, value))
            imgui.end()
    
        Args:
            label (str): widget label.
            value (float): slider values.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the current slider value.
    
        .. wraps::
            bool SliderFloat(
                const char* label,
                float v,
                float v_min,
                float v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_float2(label: str, value0: float, value1: float, min_value: float, max_value: float, format: str='%.3f', ImGuiSliderFlags_flags=0, power: float=1.0): # real signature unknown; restored from __doc__
    """
    slider_float2(str label, float value0, float value1, float min_value, float max_value, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.0)
    Display float slider widget with 2 values.
        Manually input values aren't clamped and can go off-bounds.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88.2, 42.6
    
            imgui.begin("Example: slider float2")
            changed, values = imgui.slider_float2(
                "slide floats", *values,
                min_value=0.0, max_value=100.0,
                format="%.0f"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
        
        Args:
            label (str): widget label.
            value0, value1 (float): slider values.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current slider values.
    
        .. wraps::
            bool SliderFloat2(
                const char* label,
                float v[2],
                float v_min,
                float v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_float3(label: str, value0: float, value1: float, value2: float, min_value: float, max_value: float, format: str='%.3f', ImGuiSliderFlags_flags=0, power: float=1.0): # real signature unknown; restored from __doc__
    """
    slider_float3(str label, float value0, float value1, float value2, float min_value, float max_value, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.0)
    Display float slider widget with 3 values.
        Manually input values aren't clamped and can go off-bounds.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88.2, 42.6, 69.1
    
            imgui.begin("Example: slider float3")
            changed, values = imgui.slider_float3(
                "slide floats", *values,
                min_value=0.0, max_value=100.0,
                format="%.0f"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2 (float): slider values.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current slider values.
    
        .. wraps::
            bool SliderFloat3(
                const char* label,
                float v[3],
                float v_min,
                float v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_float4(label: str, value0: float, value1: float, value2: float, value3: float, min_value: float, max_value: float, format: str='%.3f', ImGuiSliderFlags_flags=0, power: float=1.0): # real signature unknown; restored from __doc__
    """
    slider_float4(str label, float value0, float value1, float value2, float value3, float min_value, float max_value, str format='%.3f', ImGuiSliderFlags flags=0, float power=1.0)
    Display float slider widget with 4 values.
        Manually input values aren't clamped and can go off-bounds.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88.2, 42.6, 69.1, 0.3
    
            imgui.begin("Example: slider float4")
            changed, values = imgui.slider_float4(
                "slide floats", *values,
                min_value=0.0, max_value=100.0,
                format="%.0f"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2, value3 (float): slider values.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
            power (float): OBSOLETED in ImGui 1.78 (from June 2020)
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current slider values.
    
        .. wraps::
            bool SliderFloat4(
                const char* label,
                float v[4],
                float v_min,
                float v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_int(label: str, value: int, min_value: int, max_value: int, format: str='%.f', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_int(str label, int value, int min_value, int max_value, str format='%.f', ImGuiSliderFlags flags=0)
    Display int slider widget
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            value = 88
    
            imgui.begin("Example: slider int")
            changed, values = imgui.slider_int(
                "slide ints", value,
                min_value=0, max_value=100,
                format="%d"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, value))
            imgui.end()
    
        Args:
            label (str): widget label.
            value (int): slider value.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            widget state change and the slider value.
    
        .. wraps::
            bool SliderInt(
                const char* label,
                int v,
                int v_min,
                int v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_int2(label: str, value0: int, value1: int, min_value: int, max_value: int, format: str='%.f', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_int2(str label, int value0, int value1, int min_value, int max_value, str format='%.f', ImGuiSliderFlags flags=0)
    Display int slider widget with 2 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88, 27
    
            imgui.begin("Example: slider int2")
            changed, values = imgui.slider_int2(
                "slide ints2", *values,
                min_value=0, max_value=100,
                format="%d"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1 (int): slider values.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current slider values.
    
        .. wraps::
            bool SliderInt2(
                const char* label,
                int v[2],
                int v_min,
                int v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_int3(label: str, value0: int, value1: int, value2: int, min_value: int, max_value: int, format: str='%.f', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_int3(str label, int value0, int value1, int value2, int min_value, int max_value, str format='%.f', ImGuiSliderFlags flags=0)
    Display int slider widget with 3 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88, 27, 3
    
            imgui.begin("Example: slider int3")
            changed, values = imgui.slider_int3(
                "slide ints3", *values,
                min_value=0, max_value=100,
                format="%d"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2 (int): slider values.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current slider values.
    
        .. wraps::
            bool SliderInt3(
                const char* label,
                int v[3],
                int v_min,
                int v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_int4(label: str, value0: int, value1: int, value2: int, value3: int, min_value: int, max_value: int, format: str='%.f', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_int4(str label, int value0, int value1, int value2, int value3, int min_value, int max_value, str format='%.f', ImGuiSliderFlags flags=0)
    Display int slider widget with 4 values.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            values = 88, 42, 69, 0
    
            imgui.begin("Example: slider int4")
            changed, values = imgui.slider_int4(
                "slide ints", *values,
                min_value=0, max_value=100, format="%d"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value0, value1, value2, value3 (int): slider values.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, values)`` tuple that contains indicator of
            widget state change and the tuple of current slider values.
    
        .. wraps::
            bool SliderInt4(
                const char* label,
                int v[4],
                int v_min,
                int v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_scalar(label: str, ImGuiDataType_data_type, bytes_data, bytes_min_value, bytes_max_value, format: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_scalar(str label, ImGuiDataType data_type, bytes data, bytes min_value, bytes max_value, str format=None, ImGuiSliderFlags flags=0)
    Display scalar slider widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            min_value (bytes): min value allowed by widget
            max_value (bytes): max value allowed by widget
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: ImGuiSlider flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            slider state change and the current slider content.
    
        .. wraps::
            bool SliderScalar(
                const char* label,
                ImGuiDataType data_type,
                void* p_data,
                const void* p_min,
                const void* p_max,
                const char* format = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def slider_scalar_N(label: str, ImGuiDataType_data_type, bytes_data, components: int, bytes_min_value, bytes_max_value, format: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    slider_scalar_N(str label, ImGuiDataType data_type, bytes data, int components, bytes min_value, bytes max_value, str format=None, ImGuiSliderFlags flags=0)
    Display multiple scalar slider widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            components (int): number of widgets
            min_value (bytes): min value allowed by widget
            max_value (bytes): max value allowed by widget
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: ImGuiSlider flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            slider state change and the current slider content.
    
        .. wraps::
            bool SliderScalarN(
                const char* label,
                ImGuiDataType data_type,
                void* p_data,
                int components,
                const void* p_min,
                const void* p_max,
                const char* format = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def small_button(label: str): # real signature unknown; restored from __doc__
    """
    small_button(str label)
    Display small button (with 0 frame padding).
    
        .. visual-example::
            :auto_layout:
            :height: 100
    
            imgui.begin("Example: button")
            imgui.small_button("Button 1")
            imgui.small_button("Button 2")
            imgui.end()
    
        Args:
            label (str): button label.
    
        Returns:
            bool: True if clicked.
    
        .. wraps::
            bool SmallButton(const char* label)
    """
    pass

def spacing(): # real signature unknown; restored from __doc__
    """
    spacing()
    Add vertical spacing beween elements.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            imgui.begin("Example: vertical spacing")
    
            imgui.text("Some text with bullets:")
            imgui.bullet_text("Bullet A")
            imgui.bullet_text("Bullet A")
    
            imgui.spacing(); imgui.spacing()
    
            imgui.text("Another text with bullets:")
            imgui.bullet_text("Bullet A")
            imgui.bullet_text("Bullet A")
    
            imgui.end()
    
        .. wraps::
            void Spacing()
    """
    pass

def style_colors_classic(GuiStyle_dst=None): # real signature unknown; restored from __doc__
    """
    style_colors_classic(GuiStyle dst=None)
    Set the style to Classic.
    
           classic imgui style.
    
        .. wraps::
            void StyleColorsClassic(ImGuiStyle* dst = NULL)
    """
    pass

def style_colors_dark(GuiStyle_dst=None): # real signature unknown; restored from __doc__
    """
    style_colors_dark(GuiStyle dst=None)
    Set the style to Dark.
    
           new, recommended style (default)
    
        .. wraps::
            void StyleColorsDark(ImGuiStyle* dst = NULL)
    """
    pass

def style_colors_light(GuiStyle_dst=None): # real signature unknown; restored from __doc__
    """
    style_colors_light(GuiStyle dst=None)
    Set the style to Light.
    
           best used with borders and a custom, thicker font
    
        .. wraps::
            void StyleColorsLight(ImGuiStyle* dst = NULL)
    """
    pass

def table_get_column_count(): # real signature unknown; restored from __doc__
    """
    table_get_column_count()
    
    
        .. wraps::
            int TableGetColumnCount()
    """
    pass

def table_get_column_flags(column_n: int=-1): # real signature unknown; restored from __doc__
    """
    table_get_column_flags(int column_n=-1)
    
    
        .. wraps::
            ImGuiTableColumnFlags TableGetColumnFlags(
                int column_n = -1
            )
    """
    pass

def table_get_column_index(): # real signature unknown; restored from __doc__
    """
    table_get_column_index()
    
    
        .. wraps::
            int TableGetColumnIndex()
    """
    pass

def table_get_column_name(column_n: int=-1): # real signature unknown; restored from __doc__
    """
    table_get_column_name(int column_n=-1)
    
    
        .. wraps::
            const char* TableGetColumnName(
                int column_n  = -1
            )
    """
    pass

def table_get_row_index(): # real signature unknown; restored from __doc__
    """
    table_get_row_index()
    
    
        .. wraps::
            int TableGetRowIndex()
    """
    pass

def table_get_sort_specs(): # real signature unknown; restored from __doc__
    """
    table_get_sort_specs()
    
    
        .. wraps::
            ImGuiTableSortSpecs* TableGetSortSpecs()
    """
    pass

def table_header(label: str): # real signature unknown; restored from __doc__
    """
    table_header(str label)
    
    
        .. wraps::
            void TableHeader(const char* label)
    """
    pass

def table_headers_row(): # real signature unknown; restored from __doc__
    """
    table_headers_row()
    
    
        .. wraps::
            void TableHeadersRow()
    """
    pass

def table_next_column(): # real signature unknown; restored from __doc__
    """
    table_next_column()
    
    
        .. wraps::
            bool TableNextColumn()
    """
    pass

def table_next_row(ImGuiTableRowFlags_row_flags=0, min_row_height: float=0.0): # real signature unknown; restored from __doc__
    """
    table_next_row(ImGuiTableRowFlags row_flags=0, float min_row_height=0.0)
    
    
        .. wraps::
            void TableNextRow(
                ImGuiTableRowFlags row_flags = 0,
                float min_row_height = 0.0f
            )
    """
    pass

def table_setup_column(label: str, ImGuiTableColumnFlags_flags=0, init_width_or_weight: float=0.0, ImU32_user_id=0): # real signature unknown; restored from __doc__
    """
    table_setup_column(str label, ImGuiTableColumnFlags flags=0, float init_width_or_weight=0.0, ImU32 user_id=0)
    
    
        .. wraps::
            void TableSetupColumn(
                const char* label,
                ImGuiTableColumnFlags flags = 0,
                float init_width_or_weight = 0.0f,
                ImU32 user_id  = 0
            )
    """
    pass

def table_setup_scroll_freeze(cols: int, rows: int): # real signature unknown; restored from __doc__
    """
    table_setup_scroll_freeze(int cols, int rows)
    
    
        .. wraps::
            void TableSetupScrollFreeze(int cols, int rows)
    """
    pass

def table_set_background_color(ImGuiTableBgTarget_target, ImU32_color, column_n: int=-1): # real signature unknown; restored from __doc__
    """
    table_set_background_color(ImGuiTableBgTarget target, ImU32 color, int column_n=-1)
    
    
        .. wraps::
            void TableSetBgColor(
                ImGuiTableBgTarget target,
                ImU32 color,
                int column_n  = -1
            )
    """
    pass

def table_set_column_index(column_n: int): # real signature unknown; restored from __doc__
    """
    table_set_column_index(int column_n)
    
    
        .. wraps::
            bool TableSetColumnIndex(int column_n)
    """
    pass

def tab_item_button(label: str, ImGuiTabItemFlags_flags=0): # real signature unknown; restored from __doc__
    """
    tab_item_button(str label, ImGuiTabItemFlags flags=0)
    Create a Tab behaving like a button.
        Cannot be selected in the tab bar.
    
        Args:
            label (str): Label of the button
            flags: ImGuiTabItemFlags flags. See:
                :ref:`list of available flags <tabitem-flag-options>`.
    
        Returns:
            (bool): Return true when clicked.
    
        .. visual-example:
            :auto_layout:
            :width: 300
    
            imgui.begin("Example Tab Bar")
            if imgui.begin_tab_bar("MyTabBar"):
    
                if imgui.begin_tab_item("Item 1")[0]:
                    imgui.text("Here is the tab content!")
                    imgui.end_tab_item()
    
                if imgui.tab_item_button("Click me!"):
                    print('Clicked!')
    
                imgui.end_tab_bar()
            imgui.end()
    
        .. wraps::
            bool TabItemButton(const char* label, ImGuiTabItemFlags flags = 0)
    """
    pass

def text(text: str): # real signature unknown; restored from __doc__
    """
    text(str text)
    Add text to current widget stack.
    
        .. visual-example::
            :title: simple text widget
            :height: 80
            :auto_layout:
    
            imgui.begin("Example: simple text")
            imgui.text("Simple text")
            imgui.end()
    
        Args:
            text (str): text to display.
    
        .. wraps::
            Text(const char* fmt, ...)
    """
    pass

def text_colored(text: str, r: float, g: float, b: float, a: float=1.): # real signature unknown; restored from __doc__
    """
    text_colored(str text, float r, float g, float b, float a=1.)
    Add colored text to current widget stack.
    
        It is a shortcut for:
    
        .. code-block:: python
    
            imgui.push_style_color(imgui.COLOR_TEXT, r, g, b, a)
            imgui.text(text)
            imgui.pop_style_color()
    
    
        .. visual-example::
            :title: colored text widget
            :height: 100
            :auto_layout:
    
            imgui.begin("Example: colored text")
            imgui.text_colored("Colored text", 1, 0, 0)
            imgui.end()
    
        Args:
            text (str): text to display.
            r (float): red color intensity.
            g (float): green color intensity.
            b (float): blue color instensity.
            a (float): alpha intensity.
    
        .. wraps::
            TextColored(const ImVec4& col, const char* fmt, ...)
    """
    pass

def text_disabled(text: str): # real signature unknown; restored from __doc__
    """
    text_disabled(str text)
    Add disabled(grayed out) text to current widget stack.
    
        .. visual-example::
            :title: disabled text widget
            :height: 80
            :auto_layout:
    
            imgui.begin("Example: disabled text")
            imgui.text_disabled("Disabled text")
            imgui.end()
    
        Args:
            text (str): text to display.
    
        .. wraps::
            TextDisabled(const char*, ...)
    """
    pass

def text_unformatted(text: str): # real signature unknown; restored from __doc__
    """
    text_unformatted(str text)
    Big area text display - the size is defined by it's container.
        Recommended for long chunks of text.
    
        .. visual-example::
            :title: simple text widget
            :height: 100
            :width: 200
            :auto_layout:
    
            imgui.begin("Example: unformatted text")
            imgui.text_unformatted("Really ... long ... text")
            imgui.end()
    
        Args:
            text (str): text to display.
    
        .. wraps::
            TextUnformatted(const char* text, const char* text_end = NULL)
    """
    pass

def text_wrapped(text: str): # real signature unknown; restored from __doc__
    """
    text_wrapped(str text)
    Add wrappable text to current widget stack.
    
        .. visual-example::
            :title: Wrappable Text
            :height: 80
            :width: 40
            :auto_layout:
    
            imgui.begin("Text wrap")
            # Resize the window to see text wrapping
            imgui.text_wrapped("This text will wrap around.")
            imgui.end()
    
        Args:
            text (str): text to display
    
        .. wraps::
            TextWrapped(const char* fmt, ...)
    """
    pass

def tree_node(text: str, ImGuiTreeNodeFlags_flags=0): # real signature unknown; restored from __doc__
    """
    tree_node(str text, ImGuiTreeNodeFlags flags=0)
    Draw a tree node.
    
        Returns 'true' if the node is drawn, call :func:`tree_pop()` to finish.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 200
            :click: 80 40
    
            imgui.begin("Example: tree node")
            if imgui.tree_node("Expand me!", imgui.TREE_NODE_DEFAULT_OPEN):
                imgui.text("Lorem Ipsum")
                imgui.tree_pop()
            imgui.end()
    
        Args:
            text (str): Tree node label
            flags: TreeNode flags. See:
                :ref:`list of available flags <treenode-flag-options>`.
    
        Returns:
            bool: True if tree node is displayed (opened).
    
        .. wraps::
            bool TreeNode(const char* label)
            bool TreeNodeEx(const char* label, ImGuiTreeNodeFlags flags = 0)
    """
    pass

def tree_pop(): # real signature unknown; restored from __doc__
    """
    tree_pop()
    Called to clear the tree nodes stack and return back the identation.
    
        For a tree example see :func:`tree_node()`.
        Same as calls to :func:`unindent()` and :func:`pop_id()`.
    
        .. wraps::
            void TreePop()
    """
    pass

def unindent(width: float=0.0): # real signature unknown; restored from __doc__
    """
    unindent(float width=0.0)
    Move content to left by indent width.
    
        .. visual-example::
            :auto_layout:
            :width: 300
    
            imgui.begin("Example: item unindenting")
    
            imgui.text("Some text with bullets:")
    
            imgui.bullet_text("Bullet A")
            imgui.unindent(10)
            imgui.bullet_text("Bullet B (first unindented)")
            imgui.bullet_text("Bullet C (unindent continues)")
            imgui.indent(10)
            imgui.bullet_text("Bullet C (unindent cleared)")
    
            imgui.end()
    
        Args:
            width (float): fixed width of indent. If less or equal 0 it defaults
                to global indent spacing or value set using style value stack
                (see :any:`push_style_var`).
    
        .. wraps::
            void Unindent(float indent_w = 0.0f)
    """
    pass

def v_slider_float(label: str, width: float, height: float, value: float, min_value: float, max_value: float, format: str='%.f', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    v_slider_float(str label, float width, float height, float value, float min_value, float max_value, str format='%.f', ImGuiSliderFlags flags=0)
    Display vertical float slider widget with the specified width and
        height.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            width = 20
            height = 100
            value = 88
    
            imgui.begin("Example: vertical slider float")
            changed, values = imgui.v_slider_float(
                "vertical slider float",
                width, height, value,
                min_value=0, max_value=100,
                format="%0.3f", flags=imgui.SLIDER_FLAGS_NONE
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value (float): slider value.
            min_value (float): min value allowed by widget.
            max_value (float): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_float()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            widget state change and the slider value.
    
        .. wraps::
            bool VSliderFloat(
                const char* label,
                const ImVec2& size,
                float v,
                float v_min,
                floatint v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def v_slider_int(label: str, width: float, height: float, value: int, min_value: int, max_value: int, format: str='%d', ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    v_slider_int(str label, float width, float height, int value, int min_value, int max_value, str format='%d', ImGuiSliderFlags flags=0)
    Display vertical int slider widget with the specified width and height.
    
        .. visual-example::
            :auto_layout:
            :width: 400
            :height: 130
    
            width = 20
            height = 100
            value = 88
    
            imgui.begin("Example: vertical slider int")
            changed, values = imgui.v_slider_int(
                "vertical slider int",
                width, height, value,
                min_value=0, max_value=100,
                format="%d"
            )
            imgui.text("Changed: %s, Values: %s" % (changed, values))
            imgui.end()
    
        Args:
            label (str): widget label.
            value (int): slider value.
            min_value (int): min value allowed by widget.
            max_value (int): max value allowed by widget.
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe.
                See :any:`slider_int()`.
            flags: SliderFlags flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            widget state change and the slider value.
    
        .. wraps::
            bool VSliderInt(
                const char* label,
                const ImVec2& size,
                int v,
                int v_min,
                int v_max,
                const char* format = "%.3f",
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def v_slider_scalar(label: str, width: float, height: float, ImGuiDataType_data_type, bytes_data, bytes_min_value, bytes_max_value, format: Optional[str]=None, ImGuiSliderFlags_flags=0): # real signature unknown; restored from __doc__
    """
    v_slider_scalar(str label, float width, float height, ImGuiDataType data_type, bytes data, bytes min_value, bytes max_value, str format=None, ImGuiSliderFlags flags=0)
    Display vertical scalar slider widget.
        Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
        This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
        like when interfacing with Numpy.
    
        Args:
            label (str): widget label
            width (float): width of the slider
            height (float): height of the slider
            data_type: ImGuiDataType enum, type of the given data
            data (bytes): data value as a bytes array
            min_value (bytes): min value allowed by widget
            max_value (bytes): max value allowed by widget
            format (str): display format string as C-style ``printf``
                format string. **Warning:** highly unsafe. See :any:`drag_int()`.
            flags: ImGuiSlider flags. See:
                :ref:`list of available flags <slider-flag-options>`.
    
        Returns:
            tuple: a ``(changed, value)`` tuple that contains indicator of
            slider state change and the current slider content.
    
        .. wraps::
            bool VSliderScalar(
                const char* label,
                const ImVec2& size,
                ImGuiDataType data_type,
                void* p_data,
                const void* p_min,
                const void* p_max,
                const char* format = NULL,
                ImGuiSliderFlags flags = 0
            )
    """
    pass

def _ansifeed_text_ansi(text: str): # real signature unknown; restored from __doc__
    """
    _ansifeed_text_ansi(str text)
    Add ANSI-escape-formatted text to current widget stack.
    
        Similar to imgui.text, but with ANSI parsing.
        imgui.text documentation below:
    
        .. visual-example::
            :title: simple text widget
            :height: 80
            :auto_layout:
    
            imgui.begin("Example: simple text")
            imgui.extra.text_ansi("Default [31m colored [m default")
            imgui.end()
    
        Args:
            text (str): text to display.
    
        .. wraps::
            Text(const char* fmt, ...)
    """
    pass

def _ansifeed_text_ansi_colored(text: str, r: float, g: float, b: float, a: float=1.): # real signature unknown; restored from __doc__
    """
    _ansifeed_text_ansi_colored(str text, float r, float g, float b, float a=1.)
    Add pre-colored ANSI-escape-formatted text to current widget stack.
    
        Similar to imgui.text_colored, but with ANSI parsing.
        imgui.text_colored documentation below:
    
        It is a shortcut for:
    
        .. code-block:: python
    
            imgui.push_style_color(imgui.COLOR_TEXT, r, g, b, a)
            imgui.extra.text_ansi(text)
            imgui.pop_style_color()
    
    
        .. visual-example::
            :title: colored text widget
            :height: 100
            :auto_layout:
    
            imgui.begin("Example: colored text")
            imgui.text_ansi_colored("Default [31m colored [m default", 1, 0, 0)
            imgui.end()
    
        Args:
            text (str): text to display.
            r (float): red color intensity.
            g (float): green color intensity.
            b (float): blue color instensity.
            a (float): alpha intensity.
    
        .. wraps::
            TextColored(const ImVec4& col, const char* fmt, ...)
    """
    pass

def _py_colored(*args, **kwds): # reliably restored by inspect
    """ _py_colored(ImGuiCol variable, float r, float g, float b, float a=1.) """
    pass

def _py_font(*args, **kwds): # reliably restored by inspect
    """
    _py_font(_Font font)
    Use specified font in given context.
    
        .. visual-example::
            :auto_layout:
            :height: 100
            :width: 320
    
            io = imgui.get_io()
    
            new_font = io.fonts.add_font_from_file_ttf("DroidSans.ttf", 20)
            impl.refresh_font_texture()
    
            # later in frame code
    
            imgui.begin("Default Window")
    
            imgui.text("Text displayed using default font")
            with imgui.font(new_font):
                imgui.text("Text displayed using custom font")
    
            imgui.end()
    
        Args:
            font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.
    """
    pass

def _py_index_buffer_index_size(): # real signature unknown; restored from __doc__
    """ _py_index_buffer_index_size() """
    pass

def _py_istyled(*args, **kwds): # reliably restored by inspect
    """ _py_istyled(*variables_and_values) """
    pass

def _py_scoped(*args, **kwds): # reliably restored by inspect
    """
    _py_scoped(str id: str)
    Use scoped ID within a block of code.
    
        This context manager can be used to distinguish widgets sharing
        same implicit identifiers without manual calling of :func:`push_id`
        :func:`pop_id` functions.
    
        Example:
    
        Args:
            id (str: str): ID to push and pop within marked scope
    """
    pass

def _py_styled(*args, **kwds): # reliably restored by inspect
    """ _py_styled(ImGuiStyleVar variable, value) """
    pass

def _py_vertex_buffer_vertex_col_offset(): # real signature unknown; restored from __doc__
    """ _py_vertex_buffer_vertex_col_offset() """
    pass

def _py_vertex_buffer_vertex_pos_offset(): # real signature unknown; restored from __doc__
    """ _py_vertex_buffer_vertex_pos_offset() """
    pass

def _py_vertex_buffer_vertex_size(): # real signature unknown; restored from __doc__
    """ _py_vertex_buffer_vertex_size() """
    pass

def _py_vertex_buffer_vertex_uv_offset(): # real signature unknown; restored from __doc__
    """ _py_vertex_buffer_vertex_uv_offset() """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__BeginEndGroup(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__BeginEndGroup(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle__BeginEndTooltip(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__BeginEndTooltip(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

from .FontConfig import FontConfig
from .GlyphRanges import GlyphRanges
from .GuiStyle import GuiStyle
from .ImGuiError import ImGuiError
from .Vec2 import Vec2
from .Vec4 import Vec4
from ._BeginEnd import _BeginEnd
from ._BeginEndChild import _BeginEndChild
from ._BeginEndCombo import _BeginEndCombo
from ._BeginEndDragDropSource import _BeginEndDragDropSource
from ._BeginEndDragDropTarget import _BeginEndDragDropTarget
from ._BeginEndGroup import _BeginEndGroup
from ._BeginEndListBox import _BeginEndListBox
from ._BeginEndMainMenuBar import _BeginEndMainMenuBar
from ._BeginEndMenu import _BeginEndMenu
from ._BeginEndMenuBar import _BeginEndMenuBar
from ._BeginEndPopup import _BeginEndPopup
from ._BeginEndPopupModal import _BeginEndPopupModal
from ._BeginEndTabBar import _BeginEndTabBar
from ._BeginEndTabItem import _BeginEndTabItem
from ._BeginEndTable import _BeginEndTable
from ._BeginEndTooltip import _BeginEndTooltip
from ._callback_user_info import _callback_user_info
from ._Colors import _Colors
from ._DrawCmd import _DrawCmd
from ._DrawData import _DrawData
from ._DrawList import _DrawList
from ._Font import _Font
from ._FontAtlas import _FontAtlas
from ._ImGuiContext import _ImGuiContext
from ._ImGuiInputTextCallbackData import _ImGuiInputTextCallbackData
from ._ImGuiSizeCallbackData import _ImGuiSizeCallbackData
from ._ImGuiTableColumnSortSpecs import _ImGuiTableColumnSortSpecs
from ._ImGuiTableColumnSortSpecs_array import _ImGuiTableColumnSortSpecs_array
from ._ImGuiTableSortSpecs import _ImGuiTableSortSpecs
from ._ImGuiViewport import _ImGuiViewport
from ._InputTextSharedBuffer import _InputTextSharedBuffer
from ._IO import _IO
from ._StaticGlyphRanges import _StaticGlyphRanges
# variables with complex values

_contexts = {}

_io_clipboard = {}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x03CEE270>'

__spec__ = None # (!) real value is "ModuleSpec(name='imgui.core', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x03CEE270>, origin='C:\\\\Users\\\\justi\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python37-32\\\\lib\\\\site-packages\\\\imgui\\\\core.cp37-win32.pyd')"

__test__ = {}

