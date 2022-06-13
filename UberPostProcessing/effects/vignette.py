import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb


class Vignette:
    Enabled = Options.Boolean(Caption="VignetteEnabled", Description="Enable vignette effect.", StartingValue=False)
    Brightness = Options.Slider(
        Caption="VignetteBrightness",
        Description="Brightness of the vignette. Divide value by 100 to get the actual value.",
        StartingValue=20,
        MinValue=-500,
        MaxValue=500,
        Increment=1
    )
    ColorR = Options.Slider(
        Caption="VignetteColorR",
        Description="Red color of the vignette.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    ColorG = Options.Slider(
        Caption="VignetteColorG",
        Description="Green color of the vignette.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    ColorB = Options.Slider(
        Caption="VignetteColorB",
        Description="Blue color of the vignette.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    ColorA = Options.Slider(
        Caption="VignetteColorA",
        Description="Opacity of the vignette.",
        StartingValue=1,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )

    children = [Enabled, Brightness, ColorR, ColorG, ColorB, ColorA]
    Nested = Options.Nested(Caption="Vignette", Description="Vignette settings.", Children=children)


def _attach_callback():
    Vignette.Enabled.Callback = callback_normal
    Vignette.Brightness.Callback = callback_slider
    Vignette.ColorR.Callback = callback_rgb
    Vignette.ColorG.Callback = callback_rgb
    Vignette.ColorB.Callback = callback_rgb
    Vignette.ColorA.Callback = callback_rgb


VignetteOptions = Vignette.Nested

_attach_callback()
