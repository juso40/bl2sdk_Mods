import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb


class ImageGrain:
    Enable = Options.Boolean(Caption="bEnableImageGrain", Description="Enable image grain.", StartingValue=False)
    GrainScale = Options.Slider(
        Caption="SceneImageGrainScale",
        Description="Image grain scale. Divide value by 100 to get the actual value.",
        StartingValue=2,
        MinValue=0,
        MaxValue=200,
        Increment=1
    )
    children = [Enable, GrainScale]
    Nested = Options.Nested(Caption="ImageGrain", Description="Image grain settings.", Children=children)


def _attach_callback():
    ImageGrain.Enable.Callback = callback_normal
    ImageGrain.GrainScale.Callback = callback_slider


ImageGrainOptions = ImageGrain.Nested

_attach_callback()
