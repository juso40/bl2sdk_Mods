from functools import lru_cache
from typing import Tuple

import unrealsdk

RGBA = Tuple[float, float, float, float]
Vec2 = Tuple[float, float]


class _Fonts:

    @property
    @lru_cache()
    def Default__Font(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "Engine.Default__Font")

    @property
    @lru_cache()
    def Default__MultiFont(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "Engine.Default__MultiFont")

    @property
    @lru_cache()
    def SmallFont(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "EngineFonts.SmallFont")

    @property
    @lru_cache()
    def TinyFont(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "EngineFonts.TinyFont")

    @property
    @lru_cache()
    def Font_Hud_Medium(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.Font_Hud_Medium")

    @property
    @lru_cache()
    def Font_Willowbody_18pt(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.Font_Willowbody_18pt")

    @property
    @lru_cache()
    def Font_Willowbody_18pt_JPN(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.Font_Willowbody_18pt_JPN")

    @property
    @lru_cache()
    def Font_Willowbody_18pt_KOR(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.Font_Willowbody_18pt_KOR")

    @property
    @lru_cache()
    def Font_Willowbody_18pt_TWN(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.Font_Willowbody_18pt_TWN")

    @property
    @lru_cache()
    def Font_Willowhead_8pt(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.Font_Willowhead_8pt")

    @property
    @lru_cache()
    def font_ps3(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.font_ps3")

    @property
    @lru_cache()
    def font_xbox18(self) -> unrealsdk.UObject:
        return unrealsdk.FindObject("Font", "UI_Fonts.font_xbox18")


Fonts = _Fonts()


class DepthFieldGlowInfo:
    def __init__(
            self,
            enable_glow: bool = False,
            glow_color: RGBA = (0, 0, 0, 0),
            glow_outer_radius: Vec2 = (0, 0),
            glow_inner_radius: Vec2 = (0, 0)
    ) -> None:
        self._enable_glow = enable_glow
        self._glow_color = glow_color
        self._glow_outer_radius = glow_outer_radius
        self._glow_inner_radius = glow_inner_radius

    @lru_cache()
    def as_tuple(self) -> Tuple[bool, RGBA, Vec2, Vec2]:
        return self._enable_glow, self._glow_color, self._glow_outer_radius, self._glow_inner_radius

    @property
    def enable_glow(self) -> bool:
        return self._enable_glow

    @enable_glow.setter
    def enable_glow(self, value: bool) -> None:
        self._enable_glow = value
        self.as_tuple.cache_clear()

    @property
    def glow_color(self) -> RGBA:
        return self._glow_color

    @glow_color.setter
    def glow_color(self, value: RGBA) -> None:
        self._glow_color = value
        self.as_tuple.cache_clear()

    @property
    def glow_outer_radius(self) -> Vec2:
        return self._glow_outer_radius

    @glow_outer_radius.setter
    def glow_outer_radius(self, value: Vec2) -> None:
        self._glow_outer_radius = value
        self.as_tuple.cache_clear()


class FontRenderInfo:
    def __init__(
            self,
            clip_text: bool = False,
            enable_shadow: bool = False,
            shadow_info: DepthFieldGlowInfo = DepthFieldGlowInfo()
    ) -> None:
        self._clip_text = clip_text
        self._enable_shadow = enable_shadow
        self._shadow_info = shadow_info

    @lru_cache(maxsize=1)
    def as_tuple(self) -> Tuple[bool, bool, Tuple[bool, RGBA, Vec2, Vec2]]:
        return self._clip_text, self._enable_shadow, self._shadow_info.as_tuple()

    @property
    def clip_text(self) -> bool:
        return self._clip_text

    @clip_text.setter
    def clip_text(self, value: bool) -> None:
        self._clip_text = value
        self.as_tuple.cache_clear()

    @property
    def enable_shadow(self) -> bool:
        return self._enable_shadow

    @enable_shadow.setter
    def enable_shadow(self, value: bool) -> None:
        self._enable_shadow = value
        self.as_tuple.cache_clear()

    @property
    def shadow_info(self) -> DepthFieldGlowInfo:
        return self._shadow_info

    @shadow_info.setter
    def shadow_info(self, value: DepthFieldGlowInfo) -> None:
        self._shadow_info = value
        self.as_tuple.cache_clear()
