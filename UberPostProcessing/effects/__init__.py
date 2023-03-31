import unrealsdk  # type: ignore

from Mods.ModMenu import Options

from .bloom import BloomOptions
from .dof import DOFOptions
from .grain import ImageGrainOptions
from .motionblur import MotionBlurOptions
from .scene import SceneOptions
from .tonemapper import TonemapperOptions
from .vignette import VignetteOptions

all_options = [
    TonemapperOptions,
    SceneOptions,
    VignetteOptions,
    MotionBlurOptions,
    ImageGrainOptions,
    BloomOptions,
    DOFOptions,
]


def rcon(
    atrr: str, value: str, *, obje: str = "UberPostProcessEffect", cmd: str = ""
) -> None:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor

    if cmd:
        return pc.RCon(cmd)
    pc.RCon(f"set {obje} {atrr} {value}")


def callback_normal(option: Options.Value, new_value):
    rcon(option.Caption, new_value)


def callback_slider(option: Options.Slider, new_value):
    rcon(option.Caption, f"{new_value / 100}")


def callback_xyz(option: Options.Value, new_value):
    val_attr = option.Caption[-1]
    attr = option.Caption[:-1]
    rcon(attr, f"({val_attr}={new_value / 100})")


def callback_rgb(option: Options.Value, new_value):
    val_attr = option.Caption[-1]
    attr = option.Caption[:-1]
    rcon(attr, f"({val_attr}={new_value})")


def callback_rgb_worldInfo(option: Options.Value, new_value) -> None:  # noqa: N802
    val_attr = option.Caption[-1]
    attr = option.Caption[:-1]
    rcon(
        "DefaultPostProcessSettings",
        f"({attr}=({val_attr}={new_value}))",
        obje="WorldInfo",
    )


def callback_xyz_worldInfo(option: Options.Value, new_value):  # noqa: N802
    val_attr = option.Caption[-1]
    attr = option.Caption[:-1]
    rcon(
        "DefaultPostProcessSettings",
        f"({attr}=({val_attr}={new_value / 100}))",
        obje="WorldInfo",
    )


def callback_slider_worldInfo(option: Options.Slider, new_value):  # noqa: N802
    rcon(
        "DefaultPostProcessSettings",
        f"({option.Caption}={new_value / 100})",
        obje="WorldInfo",
    )


def callback_normal_worldInfo(option: Options.Value, new_value):  # noqa: N802
    rcon(
        "DefaultPostProcessSettings",
        f"({option.Caption}={new_value})",
        obje="WorldInfo",
    )
