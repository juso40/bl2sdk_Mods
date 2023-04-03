import unrealsdk  # type: ignore

from Mods.ModMenu import Options


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


from .bloom import BloomOptions  # noqa: E402
from .dof import DOFOptions  # noqa: E402
from .grain import ImageGrainOptions  # noqa: E402
from .motionblur import MotionBlurOptions  # noqa: E402
from .scene import SceneOptions  # noqa: E402
from .tonemapper import TonemapperOptions  # noqa: E402
from .vignette import VignetteOptions  # noqa: E402

all_options = [
    TonemapperOptions,
    SceneOptions,
    VignetteOptions,
    MotionBlurOptions,
    ImageGrainOptions,
    BloomOptions,
    DOFOptions,
]
