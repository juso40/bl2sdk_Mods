from typing import Dict, List

import unrealsdk
from unrealsdk import *

from Mods import ModMenu

import sys
from pathlib import Path

import os
import re

class SkinFix(ModMenu.SDKMod):
    Name: str = "TPS: Skin Fix"
    Version: str = "1.0"
    Author: str = "Juso"
    Description: str = f"Allows the exec and set command for MaterialInstanceConstant Objects."
    SupportedGames: ModMenu.Game = ModMenu.Game.TPS
    SaveEnabledState: ModMenu.EnabledSaveType = ModMenu.EnabledSaveType.LoadOnMainMenu
    
    def _exec_skins(command: str) -> None:
        args: List[str] = command.split()
    
        pattern_simple_param_name = re.compile(r"ParameterName=\"(.*?)\"")
        pattern_simple_float = re.compile(r"-?\d+\.\d+")
        pattern_simple_obj = re.compile(r"ParameterValue=(.*?),")
        pattern_simple_rgba = re.compile(r"ParameterValue=\(R=(-?\d+\.\d+),G=(-?\d+\.\d+),B=(-?\d+\.\d+),A=(-?\d+\.\d+)\)")
        obj: unrealsdk.UObject = unrealsdk.FindObject("Object", args[1])
    
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

    def command(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        args: List[str] = params.Command.split()
        cmd: str = args[0].strip().lower()
    
        if cmd == "exec":
            binaries = Path(sys.executable).parent.parent
            exec_file = os.path.join(binaries, args[1].lstrip("/").lstrip("\\"))  # this is case-sensitive
            if not os.path.isfile(exec_file):  # we could not find the file
                return True
            with open(exec_file) as fp:
                for line in fp:  # type: str
                    if line.lower().startswith("set") \
                            and unrealsdk.FindObject("MaterialInstanceConstant", line.split()[1]) is not None:
                        try:
                            SkinFix._exec_skins(line)
                        except Exception as e:
                            unrealsdk.Log(e)
        elif cmd == "set":
            if len(args) >= 4:
                if unrealsdk.FindObject("MaterialInstanceConstant", args[1]) is not None:
                    SkinFix._exec_skins(params.Command)
        return True
        
    unrealsdk.RegisterHook("Engine.PlayerController.ConsoleCommand", "Command", command)
        
instance = SkinFix()

ModMenu.RegisterMod(instance)
