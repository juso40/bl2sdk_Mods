from typing import Dict, List

import unrealsdk
from unrealsdk import *

from ..ModMenu.ModObjects import Game, ModPriorities, EnabledSaveType
from ..ModMenu import SDKMod, Hook, RegisterHooks

import os
import re


def _exec_skins(command: str) -> None:
    args: List[str] = command.split()

    pattern_simple_param_name = re.compile(r"ParameterName=\"(.*?)\"")
    pattern_simple_float = re.compile(r"-?\d+\.\d+")
    pattern_simple_obj = re.compile(r"ParameterValue=(.*?),")
    pattern_simple_rgba = re.compile(r"ParameterValue=\(R=(-?\d+\.\d+),G=(-?\d+\.\d+),B=(-?\d+\.\d+),A=(-?\d+\.\d+)\)")
    obj: unrealsdk.UObject = unrealsdk.FindObject("Object", args[1])

    if obj is None:
        return  # When we don't find our object, simply skip

    new_mat = obj

    attr: str = args[2].lower()
    values: str = args[3].strip()
    if attr == "parent":
        new_mat.SetParent(unrealsdk.FindObject("Object", values))
    elif attr == "scalarparametervalues":
        for param, val in zip(re.finditer(pattern_simple_param_name, values),
                              re.finditer(pattern_simple_float, values)):
            value = float(val.group())
            new_mat.SetScalarParameterValue(param.group(1), value)

    elif attr == "textureparametervalues":
        for param, val in zip(re.finditer(pattern_simple_param_name, values),
                              re.finditer(pattern_simple_obj, values)):
            value = unrealsdk.FindObject("Object", val.group(1))
            new_mat.SetTextureParameterValue(param.group(1), value)

    elif attr == "vectorparametervalues":
        for param, val in zip(re.finditer(pattern_simple_param_name, values),
                              re.finditer(pattern_simple_rgba, values)):
            new_mat.SetVectorParameterValue(param.group(1),
                                            tuple(float(x) for x in val.groups()))


class SkinFix(SDKMod):
    Name: str = "TPS: Skin Fix"
    Version: str = "1.0"
    Description: str = f"Allows the exec and set command for MaterialInstanceConstant Objects."
    Author: str = "Juso"
    Types: unrealsdk.ModTypes = unrealsdk.ModTypes.Library
    SupportedGames: Game = Game.TPS
    Priority: int = ModPriorities.High
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu

    SettingsInputs: Dict[str, str] = {}

    def __init__(self):
        self.Status = "Enabled"
        self.FILE_PATH = os.path.dirname(os.path.realpath(__file__))

    # noinspection PyUnusedLocal
    @Hook("Engine.PlayerController.ConsoleCommand")
    def command(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        args: List[str] = params.Command.split()
        cmd: str = args[0].strip().lower()

        if cmd == "exec":
            binaries = self.FILE_PATH
            while os.path.basename(binaries).lower() != "binaries":
                binaries = os.path.abspath(os.path.join(binaries, ".."))
            exec_file = os.path.join(binaries, args[1].lstrip("/").lstrip("\\"))  # this is case-sensitive
            if not os.path.isfile(exec_file):  # we could not find the file
                return True
            with open(exec_file) as fp:
                for line in fp:  # type: str
                    if line.lower().startswith("set") \
                            and unrealsdk.FindObject("MaterialInstanceConstant", line.split()[1]) is not None:
                        try:
                            _exec_skins(line)
                        except Exception as e:
                            unrealsdk.Log(e)
        elif cmd == "set":
            if len(args) >= 4:
                if unrealsdk.FindObject("MaterialInstanceConstant", args[1]) is not None:
                    _exec_skins(params.Command)
        return True


if __name__.startswith("Mods"):
    SkinFixInstance = SkinFix()
    unrealsdk.RegisterMod(SkinFixInstance)
    RegisterHooks(SkinFixInstance)
