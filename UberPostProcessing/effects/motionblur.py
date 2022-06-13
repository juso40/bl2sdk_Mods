import unrealsdk

from ...ModMenu import Options

from . import callback_normal, callback_slider, callback_xyz, callback_rgb


class MotionBlur:
    MaxVelocity = Options.Slider(
        Caption="MaxVelocity",
        Description="The velocity of the motion blur. Divide by 100 for the real value.",
        StartingValue=100,
        MinValue=-1000,
        MaxValue=1000,
        Increment=10
    )

    BlurAmount = Options.Slider(
        Caption="MotionBlurAmount",
        Description="The amount of motion blur. Divide by 100 for the real value.",
        StartingValue=50,
        MinValue=0,
        MaxValue=1000,
        Increment=1
    )

    FullMotionBlur = Options.Boolean(
        Caption="FullMotionBlur",
        Description="Enable full motion blur.",
        StartingValue=True,
    )

    CameraRotationThreshold = Options.Slider(
        Caption="CameraRotationThreshold",
        Description="The threshold for the camera rotation. Divide by 100 for the real value.",
        StartingValue=9000,
        MinValue=0,
        MaxValue=100000,
        Increment=100,
    )
    CameraTranslationThreshold = Options.Slider(
        Caption="CameraTranslationThreshold",
        Description="The threshold for the camera translation. Divide by 100 for the real value.",
        StartingValue=1000000,
        MinValue=0,
        MaxValue=10000000,
        Increment=100
    )

    children = [MaxVelocity, BlurAmount, FullMotionBlur, CameraRotationThreshold, CameraTranslationThreshold]
    Nested = Options.Nested(Caption="MotionBlur", Description="Motion blur options.", Children=children)


def _attach_callback():
    MotionBlur.MaxVelocity.Callback = callback_slider
    MotionBlur.BlurAmount.Callback = callback_slider
    MotionBlur.FullMotionBlur.Callback = callback_normal
    MotionBlur.CameraRotationThreshold.Callback = callback_slider
    MotionBlur.CameraTranslationThreshold.Callback = callback_slider


MotionBlurOptions = MotionBlur.Nested

_attach_callback()
