from ...ModMenu import Options


import unrealsdk


def rcon(atrr: str, value: str, *, obje: str = "UberPostProcessEffect") -> None:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    pc.RCon(f"set {obje} {atrr} {value}")
    unrealsdk.Log(f"set {obje} {atrr} {value}")


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


from .tonemapper import TonemapperOptions
from .motionblur import MotionBlurOptions
from .grain import ImageGrainOptions
from .vignette import VignetteOptions
from .bloom import BloomOptions
from .dof import DOFOptions
from .scene import SceneOptions


all_options = [
    TonemapperOptions,
    SceneOptions,
    VignetteOptions,
    MotionBlurOptions,
    ImageGrainOptions,
    BloomOptions,
    DOFOptions,
]