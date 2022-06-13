import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb


class Bloom:
    WeightSmall = Options.Slider(
        Caption="BloomWeightSmall",
        Description="Bloom weight for small objects. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=-1000,
        MaxValue=1000,
        Increment=1
    )
    WeightMedium = Options.Slider(
        Caption="BloomWeightMedium",
        Description="Bloom weight for medium objects. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=-1000,
        MaxValue=1000,
        Increment=1
    )
    WeightLarge = Options.Slider(
        Caption="BloomWeightLarge",
        Description="Bloom weight for large objects. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=-1000,
        MaxValue=1000,
        Increment=1
    )
    SizeScaleSmall = Options.Slider(
        Caption="BloomSizeScaleSmall",
        Description="Bloom size scale for small objects. Divide value by 100 to get the actual value.",
        StartingValue=25,
        MinValue=-1000,
        MaxValue=1000,
        Increment=1
    )
    SizeScaleMedium = Options.Slider(
        Caption="BloomSizeScaleMedium",
        Description="Bloom size scale for medium objects. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=-1000,
        MaxValue=1000,
        Increment=1
    )
    SizeScaleLarge = Options.Slider(
        Caption="BloomSizeScaleLarge",
        Description="Bloom size scale for large objects. Divide value by 100 to get the actual value.",
        StartingValue=300,
        MinValue=-1000,
        MaxValue=1000,
        Increment=1
    )
    BloomScale = Options.Slider(
        Caption="BloomScale",
        Description="The scale of the bloom. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )

    BloomThreshold = Options.Slider(
        Caption="BloomThreshold",
        Description="The threshold of the bloom. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )

    BloomTintR = Options.Slider(
        Caption="BloomTintR",
        Description="The red component of the bloom tint.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    BloomTintG = Options.Slider(
        Caption="BloomTintG",
        Description="The green component of the bloom tint.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    BloomTintB = Options.Slider(
        Caption="BloomTintB",
        Description="The blue component of the bloom tint.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    BloomTintA = Options.Slider(
        Caption="BloomTintA",
        Description="The alpha component of the bloom tint.",
        StartingValue=0,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )

    BloomScreenBlendThreshold = Options.Slider(
        Caption="BloomScreenBlendThreshold",
        Description="The threshold for the screen blend. Divide by 100 for the real value.",
        StartingValue=1000,
        MinValue=0,
        MaxValue=100000,
        Increment=10,
    )

    children = [WeightSmall, WeightMedium, WeightLarge, SizeScaleSmall, SizeScaleMedium, SizeScaleLarge,
                BloomScale, BloomThreshold, BloomTintR, BloomTintG, BloomTintB, BloomTintA, BloomScreenBlendThreshold,]
    Nested = Options.Nested(Caption="Bloom", Description="Bloom settings.", Children=children)


def _attach_callback():
    Bloom.WeightSmall.Callback = callback_slider
    Bloom.WeightMedium.Callback = callback_slider
    Bloom.WeightLarge.Callback = callback_slider
    Bloom.SizeScaleSmall.Callback = callback_slider
    Bloom.SizeScaleMedium.Callback = callback_slider
    Bloom.SizeScaleLarge.Callback = callback_slider
    Bloom.BloomScale.Callback = callback_slider
    Bloom.BloomThreshold.Callback = callback_slider
    Bloom.BloomTintR.Callback = callback_rgb
    Bloom.BloomTintG.Callback = callback_rgb
    Bloom.BloomTintB.Callback = callback_rgb
    Bloom.BloomTintA.Callback = callback_rgb
    Bloom.BloomScreenBlendThreshold.Callback = callback_slider


BloomOptions = Bloom.Nested

_attach_callback()
