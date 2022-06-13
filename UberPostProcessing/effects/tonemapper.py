import unrealsdk

from ...ModMenu import Options

from . import rcon, callback_normal, callback_slider

class Tonemapper:
    Type = Options.Spinner(
        Caption="TonemapperType",
        Description="Tonemapper type.",
        StartingValue="Tonemapper_Off",
        Choices=["Tonemapper_Off", "Tonemapper_Filmic", "Tonemapper_Customizable"]
    )
    Range = Options.Slider(
        Caption="TonemapperRange",
        Description="Tonemapper range. Divide value by 100 to get the actual value.",
        StartingValue=800,
        MinValue=0,
        MaxValue=200,
        Increment=10
    )
    ToeFactor = Options.Slider(
        Caption="TonemapperToeFactor",
        Description="Tonemapper toe factor. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=500,
        Increment=1
    )
    Scale = Options.Slider(
        Caption="TonemapperScale",
        Description="Tonemapper scale. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=100,
        Increment=1
    )

    children = [Type, Range, ToeFactor, Scale]
    Nested = Options.Nested(Caption="Tonemapper", Description="Tonemapper settings.", Children=children)


def _attach_callback():
    Tonemapper.Type.Callback = callback_normal
    Tonemapper.Range.Callback = callback_slider
    Tonemapper.ToeFactor.Callback = callback_slider
    Tonemapper.Scale.Callback = callback_slider


TonemapperOptions = Tonemapper.Nested

_attach_callback()
