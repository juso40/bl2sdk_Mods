import unrealsdk
from unrealsdk import *

from . import logging

import os
import re


@logging.log_all_calls(logging.call_logger)
class Materials:

    def __init__(self, path):
        self.PATH = path
        self.files = []
        self.need_mat_inst_const = []
        self.b_has_mats = False
        self.load_files()
        self.is_game_bl2 = FindObject("Object",
                                      "GD_Itempools.Runnables.Pool_Bunker") is not None  # We need this to chose how
        # to set Materials

    def Enable(self):
        for file in self.files:
            with open(file, "r") as File:
                for line in File:
                    if line.split() and line.split()[0].lower() == "set":
                        self.need_mat_inst_const.append(line.split()[1].strip())
        self.need_mat_inst_const = list(FindObject("Object", x) for x in set(self.need_mat_inst_const))
        self.need_mat_inst_const = [x for x in self.need_mat_inst_const if x is not None]

        def command(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if params.Command.split()[0].strip().lower() == "update":
                self.get_free_mat_inst_consts(True)
                return False
            return True

        unrealsdk.RegisterHook("Engine.PlayerController.ConsoleCommand", "ConsoleCommand", command)

    def Disable(self):
        pass

    def on_end_load(self):
        if not self.b_has_mats:
            self.get_free_mat_inst_consts()
            self.b_has_mats = True

    def load_files(self):
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".material"):
                    self.files.append(os.path.join(root, file))

    def get_player_controller(self):
        return GetEngine().GamePlayers[0].Actor

    def get_free_mat_inst_consts(self, reload_only=False):
        mesh = FindObject("StaticMeshComponent",
                          "GD_Weap_AssaultRifle.Projectiles.Projectile_Jakobs_Cannonball:StaticMeshComponent_18")
        # We need any MeshComponent to create new MatInstConsts, I just use this cuz its always loaded

        if not reload_only:
            for obj in self.need_mat_inst_const:
                # mat = unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool.GetFreeMatInstConsts(True)
                # KeepAlive(mat)  # We cant keep the Mats from EmitterPool alive or else GC will stop the game and crash

                mat = mesh.CreateAndSetMaterialInstanceConstant(0)
                KeepAlive(mat)

                if obj.Class in (FindClass("ClassModDefinition"),
                                 FindClass("CrossDLCClassModDefinition"),
                                 FindClass("ArtifactDefinition")):
                    obj.OverrideMaterial = mat
                else:
                    obj.Material = mat
        pc = GetEngine().GamePlayers[0].Actor

        pattern_simple_param_name = re.compile("ParameterName=\"(.*?)\"")
        pattern_simple_float = re.compile("-?\d+\.\d+")
        pattern_simple_obj = re.compile("ParameterValue=(.*?),")
        pattern_simple_rgba = re.compile(
            "ParameterValue=\(R=(-?\d+\.\d+),G=(-?\d+\.\d+),B=(-?\d+\.\d+),A=(-?\d+\.\d+)\)")

        for file in self.files:
            with open(file, "r") as TemplateFile:
                for line in TemplateFile:
                    if not line.split() or line.split()[0].lower() != "set":
                        continue
                    else:
                        obj = FindObject("Object", line.split()[1])

                        if obj is None:
                            # When we don't find our object, simply skip to the next line
                            continue

                        if obj.Class in (FindClass("ClassModDefinition"),
                                         FindClass("CrossDLCClassModDefinition"),
                                         FindClass("ArtifactDefinition")):
                            new_mat = obj.OverrideMaterial
                        else:
                            new_mat = obj.Material

                        if self.is_game_bl2:
                            set_cmd = "set "
                            set_cmd += pc.PathName(new_mat) + " "
                            set_cmd += line.split()[2] + " " + line.split()[3]
                            pc.ConsoleCommand(set_cmd, 1)

                        # The following code will only run if the game is TPS
                        else:
                            attr = line.split()[2].lower()
                            values = line.split()[3].strip()
                            if attr == "parent":
                                new_mat.SetParent(FindObject("Object", values))
                            elif attr == "scalarparametervalues":
                                for param, val in zip(re.finditer(pattern_simple_param_name, values),
                                                      re.finditer(pattern_simple_float, values)):
                                    value = float(val.group())
                                    new_mat.SetScalarParameterValue(param.group(1), value)

                            elif attr == "textureparametervalues":
                                for param, val in zip(re.finditer(pattern_simple_param_name, values),
                                                      re.finditer(pattern_simple_obj, values)):
                                    value = FindObject("Object", val.group(1))
                                    new_mat.SetTextureParameterValue(param.group(1), value)
                            elif attr == "vectorparametervalues":
                                for param, val in zip(re.finditer(pattern_simple_param_name, values),
                                                      re.finditer(pattern_simple_rgba, values)):
                                    new_mat.SetVectorParameterValue(param.group(1),
                                                                    tuple(float(x) for x in val.groups()))
