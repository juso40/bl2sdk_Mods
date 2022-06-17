import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb, callback_xyz_worldInfo, \
    callback_slider_worldInfo, callback_rgb_worldInfo, callback_normal_worldInfo, rcon


class Bloom:
    Enable = Options.Boolean(Caption="bEnableBloom", Description="Enable bloom.", StartingValue=False)
    WeightSmall = Options.Slider(
        Caption="BloomWeightSmall",
        Description="Bloom weight for small objects. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )
    WeightMedium = Options.Slider(
        Caption="BloomWeightMedium",
        Description="Bloom weight for medium objects. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )
    WeightLarge = Options.Slider(
        Caption="BloomWeightLarge",
        Description="Bloom weight for large objects. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )
    SizeScaleSmall = Options.Slider(
        Caption="BloomSizeScaleSmall",
        Description="Bloom size scale for small objects. Divide value by 100 to get the actual value.",
        StartingValue=25,
        MinValue=-1000,
        MaxValue=1000,
        Increment=5
    )
    SizeScaleMedium = Options.Slider(
        Caption="BloomSizeScaleMedium",
        Description="Bloom size scale for medium objects. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=-1000,
        MaxValue=1000,
        Increment=5
    )
    SizeScaleLarge = Options.Slider(
        Caption="BloomSizeScaleLarge",
        Description="Bloom size scale for large objects. Divide value by 100 to get the actual value.",
        StartingValue=300,
        MinValue=-1000,
        MaxValue=1000,
        Increment=5
    )
    BloomScale = Options.Slider(
        Caption="Bloom_Scale",
        Description="The scale of the bloom. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )

    BloomThreshold = Options.Slider(
        Caption="Bloom_Threshold",
        Description="The threshold of the bloom. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )

    BloomTintR = Options.Slider(
        Caption="Bloom_TintR",
        Description="The red component of the bloom tint.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    BloomTintG = Options.Slider(
        Caption="Bloom_TintG",
        Description="The green component of the bloom tint.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    BloomTintB = Options.Slider(
        Caption="Bloom_TintB",
        Description="The blue component of the bloom tint.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )
    BloomTintA = Options.Slider(
        Caption="Bloom_TintA",
        Description="The alpha component of the bloom tint.",
        StartingValue=0,
        MinValue=0,
        MaxValue=255,
        Increment=1
    )

    BloomScreenBlendThreshold = Options.Slider(
        Caption="Bloom_ScreenBlendThreshold",
        Description="The threshold for the screen blend. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )

    children = [Enable, WeightSmall, WeightMedium, WeightLarge, SizeScaleSmall, SizeScaleMedium, SizeScaleLarge,
                BloomScale, BloomThreshold, BloomTintR, BloomTintG, BloomTintB, BloomTintA, BloomScreenBlendThreshold, ]
    Nested = Options.Nested(Caption="Bloom", Description="Bloom settings.", Children=children)


def _attach_callback():
    Bloom.Enable.Callback = lambda o, v: (rcon("", "", cmd=f"SCALE set Bloom {v}"), callback_normal_worldInfo(o, v))
    Bloom.WeightSmall.Callback = callback_slider
    Bloom.WeightMedium.Callback = callback_slider
    Bloom.WeightLarge.Callback = callback_slider
    Bloom.SizeScaleSmall.Callback = callback_slider
    Bloom.SizeScaleMedium.Callback = callback_slider
    Bloom.SizeScaleLarge.Callback = callback_slider
    Bloom.BloomScale.Callback = callback_slider_worldInfo
    Bloom.BloomThreshold.Callback = callback_slider_worldInfo
    Bloom.BloomTintR.Callback = callback_rgb_worldInfo
    Bloom.BloomTintG.Callback = callback_rgb_worldInfo
    Bloom.BloomTintB.Callback = callback_rgb_worldInfo
    Bloom.BloomTintA.Callback = callback_rgb_worldInfo
    Bloom.BloomScreenBlendThreshold.Callback = callback_slider_worldInfo


BloomOptions = Bloom.Nested

_attach_callback()
