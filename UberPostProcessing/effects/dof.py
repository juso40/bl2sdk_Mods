import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb, callback_normal_worldInfo, rcon, \
    callback_slider_worldInfo, callback_xyz_worldInfo


class DOF:
    EnableDynamic = Options.Boolean(
        Caption="Dynamic DoF", Description="Enable dynamic depth of field.", StartingValue=False
    )

    Enable = Options.Boolean(Caption="bEnableDOF", Description="Enable depth of field.", StartingValue=False)

    bEnableReferenceDOF = Options.Boolean(
        Caption="bEnableReferenceDOF",
        Description="Enable reference DOF.",
        StartingValue=False,
    )

    DepthOfFieldType = Options.Spinner(
        Caption="DepthOfFieldType",
        Description="The type of depth of field.",
        StartingValue="DOFType_SimpleDOF",
        Choices=["DOFType_SimpleDOF", "DOFType_ReferenceDOF", "DOFType_BokehDOF"],
    )

    DepthOfFieldQuality = Options.Spinner(
        Caption="DepthOfFieldQuality",
        Description="The quality of the depth of field.",
        StartingValue="DOFQuality_Medium",
        Choices=["DOFQuality_Low", "DOFQuality_Medium", "DOFQuality_High"],
    )
    FalloffExponent = Options.Slider(
        Caption="DOF_FalloffExponent",
        Description="The falloff exponent. Divide by 100 for the real value.",
        StartingValue=400,
        MinValue=0,
        MaxValue=1000,
        Increment=10,
    )
    BlurKernelSize = Options.Slider(
        Caption="DOF_BlurKernelSize",
        Description="The size of the kernel for the blur. Divide by 100 for the real value.",
        StartingValue=1600,
        MinValue=0,
        MaxValue=12800,
        Increment=200,
    )
    MaxNearBlurAmount = Options.Slider(
        Caption="DOF_MaxNearBlurAmount",
        Description="The maximum near blur amount. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )
    MinBlurAmount = Options.Slider(
        Caption="DOF_MinBlurAmount",
        Description="The minimum blur amount. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )
    MaxFarBlurAmount = Options.Slider(
        Caption="DOF_MaxFarBlurAmount",
        Description="The maximum far blur amount. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )
    FocusType = Options.Spinner(
        Caption="DOF_FocusType",
        Description="The type of focus.",
        StartingValue="FOCUS_Distance",
        Choices=["FOCUS_Distance", "FOCUS_Position"]
    )
    FocusInnerRadius = Options.Slider(
        Caption="DOF_FocusInnerRadius",
        Description="The inner radius of the focus. Divide by 100 for the real value.",
        StartingValue=200000,
        MinValue=0,
        MaxValue=1000000,
        Increment=100,
    )
    FocusDistance = Options.Slider(
        Caption="DOF_FocusDistance",
        Description="The distance of the focus. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=10000,
        Increment=100,
    )

    children = [
        EnableDynamic,
        Enable,
        bEnableReferenceDOF,
        DepthOfFieldType,
        DepthOfFieldQuality,
        FalloffExponent,
        BlurKernelSize,
        MaxNearBlurAmount,
        MinBlurAmount,
        MaxFarBlurAmount,
        FocusType,
        FocusInnerRadius,
        FocusDistance,

    ]

    Nested = Options.Nested(Caption="Depth of Field", Description="DOF options.", Children=children)


def callback_dof_dynamic(option: Options.Boolean, val: bool) -> None:
    def dynamic_dof(caller, function, params) -> bool:
        if not caller.IsLocalPlayerController() or not caller.Pawn:
            return True
        pawn = caller.Pawn
        if not pawn.Weapon:
            return True
        dist = pawn.Weapon.GetTargetDistance()
        dist = dist if dist > 0 else 1000
        DOF.FocusDistance.CurrentValue = int(dist*100)
        DOF.FocusDistance.Callback(DOF.FocusDistance, int(dist*100))
        return True
    if val:
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.PlayerTick",
            "DanymicDOF",
            dynamic_dof
        )
    else:
        unrealsdk.RemoveHook(
            "WillowGame.WillowPlayerController.PlayerTick",
            "DanymicDOF"
        )



def _attach_callbacks():
    DOF.EnableDynamic.Callback = callback_dof_dynamic

    DOF.Enable.Callback = lambda o, v: (
        rcon("", "", cmd=f"SCALE set DepthOfField True"), callback_normal_worldInfo(o, v)
    )
    DOF.bEnableReferenceDOF.Callback = callback_normal
    DOF.DepthOfFieldType.Callback = callback_normal
    DOF.DepthOfFieldQuality.Callback = callback_normal
    DOF.FalloffExponent.Callback = callback_slider_worldInfo
    DOF.BlurKernelSize.Callback = callback_slider_worldInfo
    DOF.MaxNearBlurAmount.Callback = callback_slider_worldInfo
    DOF.MinBlurAmount.Callback = callback_slider_worldInfo
    DOF.MaxFarBlurAmount.Callback = callback_slider_worldInfo
    DOF.FocusType.Callback = callback_normal_worldInfo
    DOF.FocusInnerRadius.Callback = callback_slider_worldInfo
    DOF.FocusDistance.Callback = callback_slider_worldInfo


DOFOptions = DOF.Nested

_attach_callbacks()
