from ...ModMenu import Options

from . import callback_slider, callback_xyz, callback_xyz_worldInfo, callback_slider_worldInfo


class Scene:
    _min_value = -200
    _max_value = 500
    ShadowsX = Options.Slider(
        Caption="Scene_ShadowsX",
        Description="Scene shadows X. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    ShadowsY = Options.Slider(
        Caption="Scene_ShadowsY",
        Description="Scene shadows Y. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    ShadowsZ = Options.Slider(
        Caption="Scene_ShadowsZ",
        Description="Scene shadows Z. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    HighLightsX = Options.Slider(
        Caption="Scene_HighLightsX",
        Description="Scene highlights X. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    HighLightsY = Options.Slider(
        Caption="Scene_HighLightsY",
        Description="Scene highlights Y. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    HighLightsZ = Options.Slider(
        Caption="Scene_HighLightsZ",
        Description="Scene highlights Z. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    MidTonesX = Options.Slider(
        Caption="Scene_MidTonesX",
        Description="Scene midtones X. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    MidTonesY = Options.Slider(
        Caption="Scene_MidTonesY",
        Description="Scene midtones Y. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )
    MidTonesZ = Options.Slider(
        Caption="Scene_MidTonesZ",
        Description="Scene midtones Z. Divide value by 100 to get the actual value.",
        StartingValue=90,
        MinValue=_min_value,
        MaxValue=_max_value,
        Increment=5
    )

    Desaturation = Options.Slider(
        Caption="Scene_Desaturation",
        Description="Scene desaturation. Divide value by 100 to get the actual value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=100,
        Increment=1
    )

    ColorizeX = Options.Slider(
        Caption="SceneColorizeX",
        Description="Scene colorize X. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=_max_value,
        Increment=1
    )
    ColorizeY = Options.Slider(
        Caption="SceneColorizeY",
        Description="Scene colorize Y. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=_max_value,
        Increment=1
    )
    ColorizeZ = Options.Slider(
        Caption="SceneColorizeZ",
        Description="Scene colorize Z. Divide value by 100 to get the actual value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=_max_value,
        Increment=1
    )
    SceneMultiplier = Options.Slider(
        Caption="SceneMultiplier",
        Description="The multiplier for the scene. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=_max_value,
        Increment=1,
    )

    children = [ShadowsX,
                ShadowsY,
                ShadowsZ,
                HighLightsX,
                HighLightsY,
                HighLightsZ,
                MidTonesX,
                MidTonesY,
                MidTonesZ,
                Desaturation,
                ColorizeX,
                ColorizeY,
                ColorizeZ,
                SceneMultiplier]
    Nested = Options.Nested(Caption="Scene", Description="Scene settings.", Children=children)


def _attach_callback():
    Scene.ColorizeX.Callback = callback_xyz
    Scene.ColorizeY.Callback = callback_xyz
    Scene.ColorizeZ.Callback = callback_xyz
    Scene.ShadowsX.Callback = callback_xyz_worldInfo
    Scene.ShadowsY.Callback = callback_xyz_worldInfo
    Scene.ShadowsZ.Callback = callback_xyz_worldInfo
    Scene.HighLightsX.Callback = callback_xyz_worldInfo
    Scene.HighLightsY.Callback = callback_xyz_worldInfo
    Scene.HighLightsZ.Callback = callback_xyz_worldInfo
    Scene.MidTonesX.Callback = callback_xyz_worldInfo
    Scene.MidTonesY.Callback = callback_xyz_worldInfo
    Scene.MidTonesZ.Callback = callback_xyz_worldInfo
    Scene.Desaturation.Callback = callback_slider_worldInfo
    Scene.SceneMultiplier.Callback = callback_slider


SceneOptions = Scene.Nested

_attach_callback()
