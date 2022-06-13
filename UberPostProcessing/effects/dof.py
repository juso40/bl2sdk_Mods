import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb


class DOF:
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
        Caption="FalloffExponent",
        Description="The falloff exponent. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=1,
    )
    BlurKernelSize = Options.Slider(
        Caption="BlurKernelSize",
        Description="The size of the kernel for the blur. Divide by 100 for the real value.",
        StartingValue=3200,
        MinValue=0,
        MaxValue=10000,
        Increment=10,
    )
    MaxNearBlurAmount = Options.Slider(
        Caption="MaxNearBlurAmount",
        Description="The maximum near blur amount. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )
    MinBlurAmount = Options.Slider(
        Caption="MinBlurAmount",
        Description="The minimum blur amount. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )
    MaxFarBlurAmount = Options.Slider(
        Caption="MaxFarBlurAmount",
        Description="The maximum far blur amount. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=0,
        MaxValue=1000,
        Increment=5,
    )
    FocusType = Options.Spinner(
        Caption="FocusType",
        Description="The type of focus.",
        StartingValue="FOCUS_Distance",
        Choices=["FOCUS_Distance", "FOCUS_Position"]
    )
    FocusInnerRadius = Options.Slider(
        Caption="FocusInnerRadius",
        Description="The inner radius of the focus. Divide by 100 for the real value.",
        StartingValue=40000,
        MinValue=0,
        MaxValue=100000,
        Increment=100,
    )
    FocusDistance = Options.Slider(
        Caption="FocusDistance",
        Description="The distance of the focus. Divide by 100 for the real value.",
        StartingValue=80000,
        MinValue=0,
        MaxValue=1000000,
        Increment=100,
    )

    FocusPositionX = Options.Slider(
        Caption="FocusPositionX",
        Description="The X position of the focus. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=-100,
        MaxValue=100,
        Increment=1
    )
    FocusPositionY = Options.Slider(
        Caption="FocusPositionY",
        Description="The Y position of the focus. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=-100,
        MaxValue=100,
        Increment=1
    )
    FocusPositionZ = Options.Slider(
        Caption="FocusPositionZ",
        Description="The Z position of the focus. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=-100,
        MaxValue=100,
        Increment=1
    )

    TunnelVisionScale = Options.Slider(
        Caption="TunnelVisionScale",
        Description="The scale of the tunnel vision. Divide by 100 for the real value.",
        StartingValue=200,
        MinValue=-500,
        MaxValue=500,
        Increment=5
    )

    TunnelVisionYOffset = Options.Slider(
        Caption="TunnelVisionYOffset",
        Description="The Y offset of the tunnel vision. Divide by 100 for the real value.",
        StartingValue=10,
        MinValue=-100,
        MaxValue=100,
        Increment=1
    )

    bOverrideDOFSettings = Options.Boolean(
        Caption="bOverrideDOFSettings", Description="Override DOF settings.",
        StartingValue=False
    )
    FalloffExponentOverride = Options.Slider(
        Caption="FalloffExponentOverride",
        Description="The falloff exponent override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )
    BlurKernelSizeOverride = Options.Slider(
        Caption="BlurKernelSizeOverride",
        Description="The size of the kernel for the blur override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=10000,
        Increment=10
    )
    MaxNearBlurAmountOverride = Options.Slider(
        Caption="MaxNearBlurAmountOverride",
        Description="The maximum near blur amount override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )
    MaxFarBlurAmountOverride = Options.Slider(
        Caption="MaxFarBlurAmountOverride",
        Description="The maximum far blur amount override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )
    MinBlurAmountOverride = Options.Slider(
        Caption="MinBlurAmountOverride",
        Description="The minimum blur amount override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=5
    )
    FocusInnerRadiusOverride = Options.Slider(
        Caption="FocusInnerRadiusOverride",
        Description="The inner radius of the focus override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )
    FocusDistanceOverride = Options.Slider(
        Caption="FocusDistanceOverride",
        Description="The distance of the focus override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )
    TunnelVisionScaleOverride = Options.Slider(
        Caption="TunnelVisionScaleOverride",
        Description="The scale of the tunnel vision override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )
    TunnelVisionYOffsetOverride = Options.Slider(
        Caption="TunnelVisionYOffsetOverride",
        Description="The Y offset of the tunnel vision override. Divide by 100 for the real value.",
        StartingValue=0,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )

    children = [
        bEnableReferenceDOF,
        DepthOfFieldType,
        DepthOfFieldQuality,
        bOverrideDOFSettings,
        FalloffExponent,
        BlurKernelSize,
        MaxNearBlurAmount,
        MinBlurAmount,
        MaxFarBlurAmount,
        FocusType,
        FocusInnerRadius,
        FocusDistance,
        FocusPositionX,
        FocusPositionY,
        FocusPositionZ,
        TunnelVisionScale,
        TunnelVisionYOffset,
        FalloffExponentOverride,
        BlurKernelSizeOverride,
        MaxNearBlurAmountOverride,
        MinBlurAmountOverride,
        MaxFarBlurAmountOverride,
        FocusInnerRadiusOverride,
        FocusDistanceOverride,
        TunnelVisionScaleOverride,
        TunnelVisionYOffsetOverride,
    ]

    Nested = Options.Nested(Caption="Depth of Field", Description="DOF options.", Children=children)


def _attach_callbacks():
    DOF.bEnableReferenceDOF.Callback = callback_normal
    DOF.DepthOfFieldType.Callback = callback_normal
    DOF.DepthOfFieldQuality.Callback = callback_normal
    DOF.bOverrideDOFSettings.Callback = callback_normal
    DOF.FalloffExponent.Callback = callback_slider
    DOF.BlurKernelSize.Callback = callback_slider
    DOF.MaxNearBlurAmount.Callback = callback_slider
    DOF.MinBlurAmount.Callback = callback_slider
    DOF.MaxFarBlurAmount.Callback = callback_slider
    DOF.FocusType.Callback = callback_normal
    DOF.FocusInnerRadius.Callback = callback_slider
    DOF.FocusDistance.Callback = callback_slider
    DOF.FocusPositionX.Callback = callback_xyz
    DOF.FocusPositionY.Callback = callback_xyz
    DOF.FocusPositionZ.Callback = callback_xyz
    DOF.TunnelVisionScale.Callback = callback_slider
    DOF.TunnelVisionYOffset.Callback = callback_slider
    DOF.FalloffExponentOverride.Callback = callback_slider
    DOF.BlurKernelSizeOverride.Callback = callback_slider
    DOF.MaxNearBlurAmountOverride.Callback = callback_slider
    DOF.MinBlurAmountOverride.Callback = callback_slider
    DOF.MaxFarBlurAmountOverride.Callback = callback_slider
    DOF.FocusInnerRadiusOverride.Callback = callback_slider
    DOF.FocusDistanceOverride.Callback = callback_slider
    DOF.TunnelVisionScaleOverride.Callback = callback_slider
    DOF.TunnelVisionYOffsetOverride.Callback = callback_slider





DOFOptions = DOF.Nested

_attach_callbacks()
