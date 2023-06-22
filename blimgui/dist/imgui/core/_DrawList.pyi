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

class _DrawList(object):
    """
    Low level drawing API.
    
        _DrawList instance can be acquired by calling :func:`get_window_draw_list`.
    """
    def add_bezier_cubic(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_point3_x, float_point3_y, float_point4_x, float_point4_y, ImU32_col, float_thickness, int_num_segments=0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_bezier_cubic(self, float point1_x, float point1_y, float point2_x, float point2_y, float point3_x, float point3_y, float point4_x, float point4_y, ImU32 col, float thickness, int num_segments=0)
        Add a cubic bezier curve to the list.
        
                    .. visual-example::
                        :auto_layout:
                        :width: 200
                        :height: 100
        
                        imgui.begin("Cubic bezier example")
                        draw_list = imgui.get_window_draw_list()
                        draw_list.add_bezier_cubic(20, 35, 90, 80, 110, 180, 145, 35, imgui.get_color_u32_rgba(1,1,0,1), 2)
                        imgui.end()
        
                    Args:
                        point1_x (float): X coordinate of first point
                        point1_y (float): Y coordinate of first point
                        point2_x (float): X coordinate of second point
                        point2_y (float): Y coordinate of second point
                        point3_x (float): X coordinate of third point
                        point3_y (float): Y coordinate of third point
                        point4_x (float): X coordinate of fourth point
                        point4_y (float): Y coordinate of fourth point
                        col (ImU32): RGBA color specification
                        thickness (float): Line thickness
                        num_segments (ImU32): Number of segments, defaults to 0 meaning auto-tesselation
        
                    .. wraps::
                        void ImDrawList::AddBezierCubic(
                            const ImVec2& p1,
                            const ImVec2& p2,
                            const ImVec2& p3,
                            const ImVec2& p4,
                            ImU32 col,
                            float thickness,
                            int num_segments = 0
                        )
        """
        pass

    def add_bezier_quadratic(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_point3_x, float_point3_y, ImU32_col, float_thickness, int_num_segments=0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_bezier_quadratic(self, float point1_x, float point1_y, float point2_x, float point2_y, float point3_x, float point3_y, ImU32 col, float thickness, int num_segments=0)
        Add a quadratic bezier curve to the list.
        
                    .. visual-example::
                        :auto_layout:
                        :width: 200
                        :height: 100
        
                        imgui.begin("Quadratic bezier example")
                        draw_list = imgui.get_window_draw_list()
                        draw_list.add_bezier_quadratic(20, 35, 90, 80, 145, 35, imgui.get_color_u32_rgba(1,1,0,1), 2)
                        imgui.end()
        
                    Args:
                        point1_x (float): X coordinate of first point
                        point1_y (float): Y coordinate of first point
                        point2_x (float): X coordinate of second point
                        point2_y (float): Y coordinate of second point
                        point3_x (float): X coordinate of third point
                        point3_y (float): Y coordinate of third point
                        col (ImU32): RGBA color specification
                        thickness (float): Line thickness
                        num_segments (ImU32): Number of segments, defaults to 0 meaning auto-tesselation
        
                    .. wraps::
                        void ImDrawList::AddBezierCubic(
                            const ImVec2& p1,
                            const ImVec2& p2,
                            const ImVec2& p3,
                            ImU32 col,
                            float thickness,
                            int num_segments = 0
                        )
        """
        pass

    def add_circle(self, float_centre_x, float_centre_y, float_radius, ImU32_col, int_num_segments=0, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_circle(self, float centre_x, float centre_y, float radius, ImU32 col, int num_segments=0, float thickness=1.0)
        Add a circle to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Circle example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_circle(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
                    imgui.end()
        
                Args:
                    centre_x (float): circle centre coordinates
                    centre_y (float): circle centre coordinates
                    radius (float): circle radius
                    col (ImU32): RGBA color specification
                    num_segments (ImU32): Number of segments, defaults to 0 meaning auto-tesselation
                    thickness (float): Line thickness
        
                .. wraps::
                    void ImDrawList::AddCircle(
                        const ImVec2& centre,
                        float radius,
                        ImU32 col,
                        int num_segments = 0,
                        float thickness = 1.0
                    )
        """
        pass

    def add_circle_filled(self, float_centre_x, float_centre_y, float_radius, ImU32_col, ImU32_num_segments=0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_circle_filled(self, float centre_x, float centre_y, float radius, ImU32 col, ImU32 num_segments=0)
        Add a filled circle to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Filled circle example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_circle_filled(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1))
                    imgui.end()
        
                Args:
                    centre_x (float): circle centre coordinates
                    centre_y (float): circle centre coordinates
                    radius (float): circle radius
                    col (ImU32): RGBA color specification
                    num_segments (ImU32): Number of segments, defaults to 0 meaning auto-tesselation
        
                .. wraps::
                    void ImDrawList::AddCircleFilled(
                        const ImVec2& centre,
                        float radius,
                        ImU32 col,
                        int num_segments = 0
                    )
        """
        pass

    def add_image(self, texture_id, tuple_a, tuple_b, tuple_uv_a=00, tuple_uv_b=11, ImU32_col=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.add_image(self, texture_id, tuple a, tuple b, tuple uv_a=(0, 0), tuple uv_b=(1, 1), ImU32 col=0xffffffff)
        Add image to the draw list. Aspect ratio is not preserved.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Image example")
                    texture_id = imgui.get_io().fonts.texture_id
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_image(texture_id, (20, 35), (180, 80), col=imgui.get_color_u32_rgba(0.5,0.5,1,1))
                    imgui.end()
        
                Args:
                    texture_id (object): ID of the texture to draw
                    a (tuple): top-left image corner coordinates,
                    b (tuple): bottom-right image corner coordinates,
                    uv_a (tuple): UV coordinates of the top-left corner, defaults to (0, 0)
                    uv_b (tuple): UV coordinates of the bottom-right corner, defaults to (1, 1)
                    col (ImU32): tint color, defaults to 0xffffffff (no tint)
        
                .. wraps::
                    void ImDrawList::AddImage(
                        ImTextureID user_texture_id,
                        const ImVec2& a,
                        const ImVec2& b,
                        const ImVec2& uv_a = ImVec2(0,0),
                        const ImVec2& uv_b = ImVec2(1,1),
                        ImU32 col = 0xFFFFFFFF
                    )
        """
        pass

    def add_image_rounded(self, texture_id, tuple_a, tuple_b, tuple_uv_a=00, tuple_uv_b=11, ImU32_col=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.add_image_rounded(self, texture_id, tuple a, tuple b, tuple uv_a=(0, 0), tuple uv_b=(1, 1), ImU32 col=0xffffffff, float rounding=0.0, ImDrawFlags flags=0)
        Add rounded image to the draw list. Aspect ratio is not preserved.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Image example")
                    texture_id = imgui.get_io().fonts.texture_id
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_image_rounded(texture_id, (20, 35), (180, 80), col=imgui.get_color_u32_rgba(0.5,0.5,1,1), rounding=10)
                    imgui.end()
        
                Args:
                    texture_id (object): ID of the texture to draw
                    a (tuple): top-left image corner coordinates,
                    b (tuple): bottom-right image corner coordinates,
                    uv_a (tuple): UV coordinates of the top-left corner, defaults to (0, 0)
                    uv_b (tuple): UV coordinates of the bottom-right corner, defaults to (1, 1)
                    col (ImU32): tint color, defaults to 0xffffffff (no tint)
                    rounding (float): degree of rounding, defaults to 0.0
                    flags (ImDrawFlags): draw flags, defaults to 0. See:
                        :ref:`list of available flags <draw-flag-options>`.
        
                .. wraps::
                    void ImDrawList::AddImageRounded(
                        ImTextureID user_texture_id,
                        const ImVec2& a,
                        const ImVec2& b,
                        const ImVec2& uv_a = ImVec2(0,0),
                        const ImVec2& uv_b = ImVec2(1,1),
                        ImU32 col = 0xFFFFFFFF,
                        float rounding = 0.0f,
                        ImDrawFlags flags = 0
                    )
        """
        pass

    def add_line(self, float_start_x, float_start_y, float_end_x, float_end_y, ImU32_col, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_line(self, float start_x, float start_y, float end_x, float end_y, ImU32 col, float thickness=1.0)
        Add a straight line to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Line example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_line(20, 35, 180, 80, imgui.get_color_u32_rgba(1,1,0,1), 3)
                    draw_list.add_line(180, 35, 20, 80, imgui.get_color_u32_rgba(1,0,0,1), 3)
                    imgui.end()
        
                Args:
                    start_x (float): X coordinate of first point
                    start_y (float): Y coordinate of first point
                    end_x (float): X coordinate of second point
                    end_y (float): Y coordinate of second point
                    col (ImU32): RGBA color specification
                    thickness (float): Line thickness in pixels
        
                .. wraps::
                    void ImDrawList::AddLine(
                        const ImVec2& a,
                        const ImVec2& b,
                        ImU32 col,
                        float thickness = 1.0f
                    )
        """
        pass

    def add_ngon(self, float_centre_x, float_centre_y, float_radius, ImU32_col, int_num_segments, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_ngon(self, float centre_x, float centre_y, float radius, ImU32 col, int num_segments, float thickness=1.0)
        Draw a regular Ngon
                
                Args:
                    centre_x (float): circle centre coordinates
                    centre_y (float): circle centre coordinates
                    radius (float): Distance of points to center
                    col (ImU32): RGBA color specification
                    num_segments (int): Number of segments
                    thickness (float): Line thickness
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Ngon Example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_ngon(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1), 5)
                    imgui.end()
                
                .. wraps::
                    void  AddNgon(
                        const ImVec2& center, 
                        float radius, 
                        ImU32 col, 
                        int num_segments, 
                        float thickness = 1.0f
                    )
        """
        pass

    def add_ngon_filled(self, float_centre_x, float_centre_y, float_radius, ImU32_col, int_num_segments): # real signature unknown; restored from __doc__
        """
        _DrawList.add_ngon_filled(self, float centre_x, float centre_y, float radius, ImU32 col, int num_segments)
        Draw a regular Ngon
                
                Args:
                    centre_x (float): circle centre coordinates
                    centre_y (float): circle centre coordinates
                    radius (float): Distance of points to center
                    col (ImU32): RGBA color specification
                    num_segments (int): Number of segments
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Filled Ngon Example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_ngon_filled(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1), 5)
                    imgui.end()
                
                .. wraps::
                    void  AddNgonFilled(
                        const ImVec2& center, 
                        float radius, 
                        ImU32 col, 
                        int num_segments
                    )
        """
        pass

    def add_polyline(self, list_points, ImU32_col, ImDrawFlags_flags=0, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_polyline(self, list points, ImU32 col, ImDrawFlags flags=0, float thickness=1.0)
        Add a optionally closed polyline to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Polyline example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_polyline([(20, 35), (90, 35), (55, 80)], imgui.get_color_u32_rgba(1,1,0,1), flags=imgui.DRAW_NONE, thickness=3)
                    draw_list.add_polyline([(110, 35), (180, 35), (145, 80)], imgui.get_color_u32_rgba(1,0,0,1), flags=imgui.DRAW_CLOSED, thickness=3)
                    imgui.end()
        
                Args:
                    points (list): list of points
                    col (float): RGBA color specification
                    flags (ImDrawFlags): Drawing flags. See:
                        :ref:`list of available flags <draw-flag-options>`.
                    thickness (float): line thickness
        
                .. wraps::
                    void ImDrawList::AddPolyline(
                        const ImVec2* points,
                        int num_points,
                        ImU32 col,
                        flags flags,
                        float thickness
                    )
        """
        pass

    def add_quad(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_point3_x, float_point3_y, float_point4_x, float_point4_y, ImU32_col, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_quad(self, float point1_x, float point1_y, float point2_x, float point2_y, float point3_x, float point3_y, float point4_x, float point4_y, ImU32 col, float thickness=1.0)
        Add a quad to the list.
        
                    .. visual-example::
                        :auto_layout:
                        :width: 200
                        :height: 100
        
                        imgui.begin("Quad example")
                        draw_list = imgui.get_window_draw_list()
                        draw_list.add_quad(20, 35, 85, 30, 90, 80, 17, 76, imgui.get_color_u32_rgba(1,1,0,1))
                        draw_list.add_quad(110, 35, 177, 33, 180, 80, 112, 79, imgui.get_color_u32_rgba(1,0,0,1), 5)
                        imgui.end()
        
                    Args:
                        point1_x (float): X coordinate of first corner
                        point1_y (float): Y coordinate of first corner
                        point2_x (float): X coordinate of second corner
                        point2_y (float): Y coordinate of second corner
                        point3_x (float): X coordinate of third corner
                        point3_y (float): Y coordinate of third corner
                        point4_x (float): X coordinate of fourth corner
                        point4_y (float): Y coordinate of fourth corner
                        col (ImU32): RGBA color specification
                        thickness (float): Line thickness
        
                    .. wraps::
                        void ImDrawList::AddQuad(
                            const ImVec2& p1,
                            const ImVec2& p2,
                            const ImVec2& p3,
                            const ImVec2& p4,
                            ImU32 col,
                            float thickness = 1.0
                        )
        """
        pass

    def add_quad_filled(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_point3_x, float_point3_y, float_point4_x, float_point4_y, ImU32_col): # real signature unknown; restored from __doc__
        """
        _DrawList.add_quad_filled(self, float point1_x, float point1_y, float point2_x, float point2_y, float point3_x, float point3_y, float point4_x, float point4_y, ImU32 col)
        Add a filled quad to the list.
        
                    .. visual-example::
                        :auto_layout:
                        :width: 200
                        :height: 100
        
                        imgui.begin("Filled Quad example")
                        draw_list = imgui.get_window_draw_list()
                        draw_list.add_quad_filled(20, 35, 85, 30, 90, 80, 17, 76, imgui.get_color_u32_rgba(1,1,0,1))
                        draw_list.add_quad_filled(110, 35, 177, 33, 180, 80, 112, 79, imgui.get_color_u32_rgba(1,0,0,1))
                        imgui.end()
        
                    Args:
                        point1_x (float): X coordinate of first corner
                        point1_y (float): Y coordinate of first corner
                        point2_x (float): X coordinate of second corner
                        point2_y (float): Y coordinate of second corner
                        point3_x (float): X coordinate of third corner
                        point3_y (float): Y coordinate of third corner
                        point4_x (float): X coordinate of fourth corner
                        point4_y (float): Y coordinate of fourth corner
                        col (ImU32): RGBA color specification
        
                    .. wraps::
                        void ImDrawList::AddQuadFilled(
                            const ImVec2& p1,
                            const ImVec2& p2,
                            const ImVec2& p3,
                            const ImVec2& p4,
                            ImU32 col
                        )
        """
        pass

    def add_rect(self, float_upper_left_x, float_upper_left_y, float_lower_right_x, float_lower_right_y, ImU32_col, float_rounding=0.0, ImDrawFlags_flags=0, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_rect(self, float upper_left_x, float upper_left_y, float lower_right_x, float lower_right_y, ImU32 col, float rounding=0.0, ImDrawFlags flags=0, float thickness=1.0)
        Add a rectangle outline to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Rect example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_rect(20, 35, 90, 80, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
                    draw_list.add_rect(110, 35, 180, 80, imgui.get_color_u32_rgba(1,0,0,1), rounding=5, thickness=3)
                    imgui.end()
        
                Args:
                    upper_left_x (float): X coordinate of top-left corner
                    upper_left_y (float): Y coordinate of top-left corner
                    lower_right_x (float): X coordinate of lower-right corner
                    lower_right_y (float): Y coordinate of lower-right corner
                    col (ImU32): RGBA color specification
                    rounding (float): Degree of rounding, defaults to 0.0
                    flags (ImDrawFlags): Draw flags, defaults to 0. See:
                        :ref:`list of available flags <draw-flag-options>`.
                    thickness (float): Line thickness, defaults to 1.0
        
                .. wraps::
                    void ImDrawList::AddRect(
                        const ImVec2& a,
                        const ImVec2& b,
                        ImU32 col,
                        float rounding = 0.0f,
                        ImDrawFlags flags = 0,
                        float thickness = 1.0f
                    )
        """
        pass

    def add_rect_filled(self, float_upper_left_x, float_upper_left_y, float_lower_right_x, float_lower_right_y, ImU32_col, float_rounding=0.0, ImDrawFlags_flags=0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_rect_filled(self, float upper_left_x, float upper_left_y, float lower_right_x, float lower_right_y, ImU32 col, float rounding=0.0, ImDrawFlags flags=0)
        Add a filled rectangle to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Filled rect example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_rect_filled(20, 35, 90, 80, imgui.get_color_u32_rgba(1,1,0,1))
                    draw_list.add_rect_filled(110, 35, 180, 80, imgui.get_color_u32_rgba(1,0,0,1), 5)
                    imgui.end()
        
                Args:
                    upper_left_x (float): X coordinate of top-left corner
                    upper_left_y (float): Y coordinate of top-left corner
                    lower_right_x (float): X coordinate of lower-right corner
                    lower_right_y (float): Y coordinate of lower-right corner
                    col (ImU32): RGBA color specification
                    rounding (float): Degree of rounding, defaults to 0.0
                    flags (ImDrawFlags): Draw flags, defaults to 0. See:
                        :ref:`list of available flags <draw-flag-options>`.
        
                .. wraps::
                    void ImDrawList::AddRectFilled(
                        const ImVec2& a,
                        const ImVec2& b,
                        ImU32 col,
                        float rounding = 0.0f,
                        ImDrawFlags flags = 0
                    )
        """
        pass

    def add_rect_filled_multicolor(self, float_upper_left_x, float_upper_left_y, float_lower_right_x, float_lower_right_y, ImU32_col_upr_left, ImU32_col_upr_right, ImU32_col_bot_right, ImU32_col_bot_left): # real signature unknown; restored from __doc__
        """
        _DrawList.add_rect_filled_multicolor(self, float upper_left_x, float upper_left_y, float lower_right_x, float lower_right_y, ImU32 col_upr_left, ImU32 col_upr_right, ImU32 col_bot_right, ImU32 col_bot_left)
        Add a multicolor filled rectangle to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Multicolored filled rect example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_rect_filled_multicolor(20, 35, 190, 80, imgui.get_color_u32_rgba(1,0,0,1),
                        imgui.get_color_u32_rgba(0,1,0,1), imgui.get_color_u32_rgba(0,0,1,1),
                        imgui.get_color_u32_rgba(1,1,1,1))
                    imgui.end()
        
                Args:
                    upper_left_x (float): X coordinate of top-left corner
                    upper_left_y (float): Y coordinate of top-left corner
                    lower_right_x (float): X coordinate of lower-right corner
                    lower_right_y (float): Y coordinate of lower-right corner
                    col_upr_left (ImU32): RGBA color for the top left corner
                    col_upr_right (ImU32): RGBA color for the top right corner
                    col_bot_right (ImU32): RGBA color for the bottom right corner
                    col_bot_left (ImU32): RGBA color for the bottom left corner
        
                .. wraps::
                    void ImDrawList::AddRectFilledMultiColor(
                        const ImVec2& a,
                        const ImVec2& b,
                        ImU32 col_upr_left,
                        ImU32 col_upr_right,
                        ImU32 col_bot_right,
                        ImU32 col_bot_left
                    )
        """
        pass

    def add_text(self, float_pos_x, float_pos_y, ImU32_col, str_text): # real signature unknown; restored from __doc__
        """
        _DrawList.add_text(self, float pos_x, float pos_y, ImU32 col, str text)
        Add text to the draw list.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Text example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.add_text(20, 35, imgui.get_color_u32_rgba(1,1,0,1), "Hello!")
                    imgui.end()
        
                Args:
                    pos_x (float): X coordinate of the text's upper-left corner
                    pos_y (float): Y coordinate of the text's upper-left corner
                    col (ImU32): RGBA color specification
                    text (str): text
        
                .. wraps::
                    void ImDrawList::AddText(
                        const ImVec2& pos,
                        ImU32 col,
                        const char* text_begin,
                        const char* text_end = NULL
                    )
        """
        pass

    def add_triangle(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_point3_x, float_point3_y, ImU32_col, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.add_triangle(self, float point1_x, float point1_y, float point2_x, float point2_y, float point3_x, float point3_y, ImU32 col, float thickness=1.0)
        Add a triangle to the list.
        
                    .. visual-example::
                        :auto_layout:
                        :width: 200
                        :height: 100
        
                        imgui.begin("Triangle example")
                        draw_list = imgui.get_window_draw_list()
                        draw_list.add_triangle(20, 35, 90, 35, 55, 80, imgui.get_color_u32_rgba(1,1,0,1))
                        draw_list.add_triangle(110, 35, 180, 35, 145, 80, imgui.get_color_u32_rgba(1,0,0,1), 5)
                        imgui.end()
        
                    Args:
                        point1_x (float): X coordinate of first corner
                        point1_y (float): Y coordinate of first corner
                        point2_x (float): X coordinate of second corner
                        point2_y (float): Y coordinate of second corner
                        point3_x (float): X coordinate of third corner
                        point3_y (float): Y coordinate of third corner
                        col (ImU32): RGBA color specification
                        thickness (float): Line thickness
        
                    .. wraps::
                        void ImDrawList::AddTriangle(
                            const ImVec2& p1,
                            const ImVec2& p2,
                            const ImVec2& p3,
                            ImU32 col,
                            float thickness = 1.0
                        )
        """
        pass

    def add_triangle_filled(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_point3_x, float_point3_y, ImU32_col): # real signature unknown; restored from __doc__
        """
        _DrawList.add_triangle_filled(self, float point1_x, float point1_y, float point2_x, float point2_y, float point3_x, float point3_y, ImU32 col)
        Add a filled triangle to the list.
        
                    .. visual-example::
                        :auto_layout:
                        :width: 200
                        :height: 100
        
                        imgui.begin("Filled triangle example")
                        draw_list = imgui.get_window_draw_list()
                        draw_list.add_triangle_filled(20, 35, 90, 35, 55, 80, imgui.get_color_u32_rgba(1,1,0,1))
                        draw_list.add_triangle_filled(110, 35, 180, 35, 145, 80, imgui.get_color_u32_rgba(1,0,0,1))
                        imgui.end()
        
                    Args:
                        point1_x (float): X coordinate of first corner
                        point1_y (float): Y coordinate of first corner
                        point2_x (float): X coordinate of second corner
                        point2_y (float): Y coordinate of second corner
                        point3_x (float): X coordinate of third corner
                        point3_y (float): Y coordinate of third corner
                        col (ImU32): RGBA color specification
        
                    .. wraps::
                        void ImDrawList::AddTriangleFilled(
                            const ImVec2& p1,
                            const ImVec2& p2,
                            const ImVec2& p3,
                            ImU32 col
                        )
        """
        pass

    def channels_merge(self): # real signature unknown; restored from __doc__
        """ _DrawList.channels_merge(self) """
        pass

    def channels_set_current(self, int_idx): # real signature unknown; restored from __doc__
        """ _DrawList.channels_set_current(self, int idx) """
        pass

    def channels_split(self, int_channels_count): # real signature unknown; restored from __doc__
        """
        _DrawList.channels_split(self, int channels_count)
        Use to split render into layers. 
                By switching channels to can render out-of-order (e.g. submit FG primitives before BG primitives)
                Use to minimize draw calls (e.g. if going back-and-forth between multiple clipping rectangles, prefer to append into separate channels then merge at the end)
                
                Prefer using your own persistent instance of ImDrawListSplitter as you can stack them.
                Using the ImDrawList::ChannelsXXXX you cannot stack a split over another.
                
                Warning - be careful with using channels as "layers".
                Child windows are always drawn after their parent, so they will
                paint over its channels.
                To paint over child windows, use `OverlayDrawList`.
        """
        pass

    def get_clip_rect_max(self): # real signature unknown; restored from __doc__
        """
        _DrawList.get_clip_rect_max(self)
        
                .. wraps::
                    ImVec2 GetClipRectMax()
        """
        pass

    def get_clip_rect_min(self): # real signature unknown; restored from __doc__
        """
        _DrawList.get_clip_rect_min(self)
        
                .. wraps::
                    ImVec2 GetClipRectMin()
        """
        pass

    def path_arc_to(self, float_center_x, float_center_y, float_radius, float_a_min, float_a_max, ImU32_num_segments=0): # real signature unknown; restored from __doc__
        """
        _DrawList.path_arc_to(self, float center_x, float center_y, float radius, float a_min, float a_max, ImU32 num_segments=0)
        
                Add an arc to the path list
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Path arc to example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.path_clear()
                    draw_list.path_arc_to(55, 60, 30, 1, 5)
                    draw_list.path_stroke(imgui.get_color_u32_rgba(1,1,0,1), flags=0, thickness=3)
                    draw_list.path_clear()
                    draw_list.path_arc_to(155, 60, 30, -2, 2)
                    draw_list.path_fill_convex(imgui.get_color_u32_rgba(1,0,0,1))
                    imgui.end()
        
                Args:
                    center_x (float): arc center x coordinate
                    center_y (float): arc center y coordinate
                    radius (flaot): radius of the arc
                    a_min (float): minimum angle of the arc (in radian)
                    a_max (float): maximum angle of the arc (in radian)
                    num_segments (ImU32): Number of segments, defaults to 0 meaning auto-tesselation
        
                .. wraps::
                    void ImDrawList::PathArcTo(
                        const ImVec2& center,
                        float radius,
                        float a_min,
                        float a_max,
                        int num_segments = 0
                    )
        """
        pass

    def path_arc_to_fast(self, float_center_x, float_center_y, float_radius, ImU32_a_min_of_12, ImU32_a_max_of_12): # real signature unknown; restored from __doc__
        """
        _DrawList.path_arc_to_fast(self, float center_x, float center_y, float radius, ImU32 a_min_of_12, ImU32 a_max_of_12)
        
                Add an arc to the path list
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Path arc to fast example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.path_clear()
                    draw_list.path_arc_to_fast(55, 60, 30, 0, 6)
                    draw_list.path_stroke(imgui.get_color_u32_rgba(1,1,0,1), flags=0, thickness=3)
                    draw_list.path_clear()
                    draw_list.path_arc_to_fast(155, 60, 30, 3, 9)
                    draw_list.path_fill_convex(imgui.get_color_u32_rgba(1,0,0,1))
                    imgui.end()
        
                Args:
                    center_x (float): arc center x coordinate
                    center_y (float): arc center y coordinate
                    radius (flaot): radius of the arc
                    a_min_of_12 (ImU32): minimum angle of the arc
                    a_max_of_12 (ImU32): maximum angle of the arc
        
                .. wraps::
                    void ImDrawList::PathArcToFast(
                        const ImVec2& center,
                        float radius,
                        int a_min_of_12,
                        int a_max_of_12
                    )
        """
        pass

    def path_clear(self): # real signature unknown; restored from __doc__
        """
        _DrawList.path_clear(self)
        
                Clear the current list of path point
        
                .. wraps::
                    void ImDrawList::PathClear()
        """
        pass

    def path_fill_convex(self, ImU32_col): # real signature unknown; restored from __doc__
        """
        _DrawList.path_fill_convex(self, ImU32 col)
        
        
                Note: Filled shapes must always use clockwise winding order.
                The anti-aliasing fringe depends on it. Counter-clockwise shapes
                will have "inward" anti-aliasing.
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Path fill convex example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.path_clear()
                    draw_list.path_line_to(100, 60)
                    draw_list.path_arc_to(100, 60, 30, 0.5, 5.5)
                    draw_list.path_fill_convex(imgui.get_color_u32_rgba(1,1,0,1))
                    imgui.end()
        
                Args:
                    col (ImU32): color to fill the path shape with
        
                .. wraps::
                    void ImDrawList::PathFillConvex(
                        ImU32   col
                    );
        """
        pass

    def path_line_to(self, float_x, float_y): # real signature unknown; restored from __doc__
        """
        _DrawList.path_line_to(self, float x, float y)
        
                Add a point to the path list
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Path line to example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.path_clear()
                    draw_list.path_line_to(20, 35)
                    draw_list.path_line_to(180, 80)
                    draw_list.path_stroke(imgui.get_color_u32_rgba(1,1,0,1), flags=0, thickness=3)
                    draw_list.path_clear()
                    draw_list.path_line_to(180, 35)
                    draw_list.path_line_to(20, 80)
                    draw_list.path_stroke(imgui.get_color_u32_rgba(1,0,0,1), flags=0, thickness=3)
                    imgui.end()
        
                Args:
                    x (float): path point x coordinate
                    y (float): path point y coordinate
        
                .. wraps::
                    void ImDrawList::PathLineTo(
                        const ImVec2& pos,
                    )
        """
        pass

    def path_rect(self, float_point1_x, float_point1_y, float_point2_x, float_point2_y, float_rounding=0.0, ImDrawFlags_flags=0): # real signature unknown; restored from __doc__
        """
        _DrawList.path_rect(self, float point1_x, float point1_y, float point2_x, float point2_y, float rounding=0.0, ImDrawFlags flags=0)
        
                Add a rect to the path list
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Path arc to fast example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.path_clear()
                    draw_list.path_rect(20, 35, 90, 80)
                    draw_list.path_stroke(imgui.get_color_u32_rgba(1,1,0,1), flags=0, thickness=3)
                    draw_list.path_clear()
                    draw_list.path_rect(110, 35, 180, 80, 5)
                    draw_list.path_fill_convex(imgui.get_color_u32_rgba(1,0,0,1))
                    imgui.end()
        
                Args:
                    point1_x (float): point1 x coordinate
                    point1_y (float): point1 y coordinate
                    point2_x (float): point2 x coordinate
                    point2_y (float): point2 y coordinate
                    rounding (flaot): Degree of rounding, defaults to 0.0
                    flags (ImDrawFlags):Draw flags, defaults to 0. See:
                        :ref:`list of available flags <draw-flag-options>`.
        
                .. wraps::
                    void ImDrawList::PathRect(
                        const ImVec2& p1,
                        const ImVec2& p2,
                        float rounding = 0.0,
                        ImDrawFlags flags = 0
                    )
        """
        pass

    def path_stroke(self, ImU32_col, ImDrawFlags_flags=0, float_thickness=1.0): # real signature unknown; restored from __doc__
        """
        _DrawList.path_stroke(self, ImU32 col, ImDrawFlags flags=0, float thickness=1.0)
        
                Args:
                    col (ImU32): color to fill the path shape with
                    flags (ImDrawFlags): draw flags, defaults to 0. See:
                        :ref:`list of available flags <draw-flag-options>`.
                    thickness (float): Line thickness in pixels
        
                .. visual-example::
                    :auto_layout:
                    :width: 200
                    :height: 100
        
                    imgui.begin("Path stroke example")
                    draw_list = imgui.get_window_draw_list()
                    draw_list.path_clear()
                    draw_list.path_line_to(100, 60)
                    draw_list.path_arc_to(100, 60, 30, 0.5, 5.5)
                    draw_list.path_stroke(imgui.get_color_u32_rgba(1,1,0,1), flags=imgui.DRAW_CLOSED, thickness=3)
                    imgui.end()
        
        
                .. wraps::
                    void ImDrawList::PathStroke(
                        ImU32 col,
                        ImDrawFlags flags = 0,
                        float thickness = 1.0
                    );
        """
        pass

    def pop_clip_rect(self): # real signature unknown; restored from __doc__
        """
        _DrawList.pop_clip_rect(self)
        Render-level scisoring. 
                
                .. wraps::
                    void PopClipRect()
        """
        pass

    def pop_texture_id(self): # real signature unknown; restored from __doc__
        """
        _DrawList.pop_texture_id(self)
        
                .. wraps::
                    void PopTextureID()
        """
        pass

    def prim_quad_UV(self, float_a_x, float_a_y, float_b_x, float_b_y, float_c_x, float_c_y, float_d_x, float_d_y, float_uv_a_u, float_uv_a_v, float_uv_b_u, float_uv_b_v, float_uv_c_u, float_uv_c_v, float_uv_d_u, float_uv_d_v, ImU32_color=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.prim_quad_UV(self, float a_x, float a_y, float b_x, float b_y, float c_x, float c_y, float d_x, float d_y, float uv_a_u, float uv_a_v, float uv_b_u, float uv_b_v, float uv_c_u, float uv_c_v, float uv_d_u, float uv_d_v, ImU32 color=0xFFFFFFFF)
        Custom quad (2 triangles) with custom UV coordinates.
                Reserve primitive space with `prim_reserve()` before calling `prim_quad_UV()`.
                Each call to `prim_quad_UV()` is 6 idx and 4 vtx.
                Set the texture ID using `push_texture_id()`.
                
                Args:
                    a_x, a_y (float): Point 1 coordinates
                    b_x, b_y (float): Point 2 coordinates
                    c_x, c_y (float): Point 3 coordinates
                    d_x, d_y (float): Point 4 coordinates
                    uv_a_u, uv_a_v (float): Point 1 UV coordinates
                    uv_b_u, uv_b_v (float): Point 2 UV coordinates
                    uv_c_u, uv_c_v (float): Point 3 UV coordinates
                    uv_d_u, uv_d_v (float): Point 4 UV coordinates
                    color (ImU32): Color
                
                .. wraps::
                    void PrimQuadUV(const ImVec2& a, const ImVec2& b, const ImVec2& c, const ImVec2& d, const ImVec2& uv_a, const ImVec2& uv_b, const ImVec2& uv_c, const ImVec2& uv_d, ImU32 col)
        """
        pass

    def prim_rect(self, float_a_x, float_a_y, float_b_x, float_b_y, ImU32_color=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.prim_rect(self, float a_x, float a_y, float b_x, float b_y, ImU32 color=0xFFFFFFFF)
        Axis aligned rectangle (2 triangles)
                Reserve primitive space with `prim_rect()` before calling `prim_quad_UV()`.
                Each call to `prim_rect()` is 6 idx and 4 vtx.
                
                Args:
                    a_x, a_y (float): First rectangle point coordinates
                    b_x, b_y (float): Opposite rectangle point coordinates
                    color (ImU32): Color
                
                .. wraps::
                    void PrimRect(const ImVec2& a, const ImVec2& b, ImU32 col)
        """
        pass

    def prim_rect_UV(self, float_a_x, float_a_y, float_b_x, float_b_y, float_uv_a_u, float_uv_a_v, float_uv_b_u, float_uv_b_v, ImU32_color=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.prim_rect_UV(self, float a_x, float a_y, float b_x, float b_y, float uv_a_u, float uv_a_v, float uv_b_u, float uv_b_v, ImU32 color=0xFFFFFFFF)
        Axis aligned rectangle (2 triangles) with custom UV coordinates.
                Reserve primitive space with `prim_reserve()` before calling `prim_rect_UV()`.
                Each call to `prim_rect_UV()` is 6 idx and 4 vtx.
                Set the texture ID using `push_texture_id()`.
                
                Args:
                    a_x, a_y (float): First rectangle point coordinates
                    b_x, b_y (float): Opposite rectangle point coordinates
                    uv_a_u, uv_a_v (float): First rectangle point UV coordinates
                    uv_b_u, uv_b_v (float): Opposite rectangle point UV coordinates
                    color (ImU32): Color
                
                .. wraps::
                    void PrimRectUV(const ImVec2& a, const ImVec2& b, const ImVec2& uv_a, const ImVec2& uv_b, ImU32 col)
        """
        pass

    def prim_reserve(self, int_idx_count, int_vtx_count): # real signature unknown; restored from __doc__
        """
        _DrawList.prim_reserve(self, int idx_count, int vtx_count)
        Reserve space for a number of vertices and indices.
                You must finish filling your reserved data before calling `prim_reserve()` again, as it may 
                reallocate or submit the intermediate results. `prim_unreserve()` can be used to release 
                unused allocations.
                
                Drawing a quad is 6 idx (2 triangles) with 2 sharing vertices for a total of 4 vertices.
                
                Args:
                    idx_count (int): Number of indices to add to IdxBuffer
                    vtx_count (int): Number of verticies to add to VtxBuffer
                
                .. wraps::
                    void PrimReserve(int idx_count, int vtx_count)
        """
        pass

    def prim_unreserve(self, int_idx_count, int_vtx_count): # real signature unknown; restored from __doc__
        """
        _DrawList.prim_unreserve(self, int idx_count, int vtx_count)
        Release the a number of reserved vertices/indices from the end of the 
                last reservation made with `prim_reserve()`.
                
                Args:
                    idx_count (int): Number of indices to remove from IdxBuffer
                    vtx_count (int): Number of verticies to remove from VtxBuffer
                
                .. wraps::
                    void PrimUnreserve(int idx_count, int vtx_count)
        """
        pass

    def prim_vtx(self, float_pos_x, float_pos_y, float_u, float_v, ImU32_color=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.prim_vtx(self, float pos_x, float pos_y, float u, float v, ImU32 color=0xFFFFFFFF)
        Write vertex with unique index
                
                Args:
                    pos_x, pos_y (float): Point coordinates
                    u, v (float): Point UV coordinates
                    color (ImU32): Color
                
                .. wraps::
                    void PrimVtx(const ImVec2& pos, const ImVec2& uv, ImU32 col)
        """
        pass

    def prim_write_idx(self, ImDrawIdx_idx): # real signature unknown; restored from __doc__
        """
        _DrawList.prim_write_idx(self, ImDrawIdx idx)
        Write index
                
                Args:
                    idx (ImDrawIdx): index to write
                
                .. wraps::
                    void  PrimWriteIdx(ImDrawIdx idx)
        """
        pass

    def prim_write_vtx(self, float_pos_x, float_pos_y, float_u, float_v, ImU32_color=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _DrawList.prim_write_vtx(self, float pos_x, float pos_y, float u, float v, ImU32 color=0xFFFFFFFF)
        Write a vertex
                
                Args:
                    pos_x, pos_y (float): Point coordinates
                    u, v (float): Point UV coordinates
                    color (ImU32): Color
                
                .. wraps::
                    void  PrimWriteVtx(const ImVec2& pos, const ImVec2& uv, ImU32 col)
        """
        pass

    def push_clip_rect(self, float_clip_rect_min_x, float_clip_rect_min_y, float_clip_rect_max_x, float_clip_rect_max_y, bool_intersect_with_current_clip_rect=False): # real signature unknown; restored from __doc__
        """
        _DrawList.push_clip_rect(self, float clip_rect_min_x, float clip_rect_min_y, float clip_rect_max_x, float clip_rect_max_y, bool intersect_with_current_clip_rect=False)
        Render-level scissoring. This is passed down to your render function 
                but not used for CPU-side coarse clipping. Prefer using higher-level :func:`push_clip_rect()` 
                to affect logic (hit-testing and widget culling)
                
                .. wraps::
                    void PushClipRect(ImVec2 clip_rect_min, ImVec2 clip_rect_max, bool intersect_with_current_clip_rect = false)
        """
        pass

    def push_clip_rect_full_screen(self): # real signature unknown; restored from __doc__
        """
        _DrawList.push_clip_rect_full_screen(self)
        
                .. wraps::
                    void PushClipRectFullScreen()
        """
        pass

    def push_texture_id(self, texture_id): # real signature unknown; restored from __doc__
        """
        _DrawList.push_texture_id(self, texture_id)
        
                .. wraps::
                    void PushTextureID(ImTextureID texture_id)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _DrawList.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _DrawList.__setstate_cython__(self, __pyx_state) """
        pass

    cmd_buffer_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cmd_buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    commands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    idx_buffer_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    idx_buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vtx_buffer_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vtx_buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x03CCE8C0>'


