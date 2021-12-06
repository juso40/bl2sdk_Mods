import unrealsdk
from unrealsdk import *

from . import logging
from . import bl2tools
from . import hookmanager

import os
import re

MESH = unrealsdk.FindObject("StaticMeshComponent",
                            "GD_Weap_AssaultRifle.Projectiles.Projectile_Jakobs_Cannonball:StaticMeshComponent_18")


@logging.log_all_calls(logging.call_logger)
class Materials:

    def __init__(self, path: os.PathLike):
        self.PATH = path
        self.files = []
        self.need_mat_inst_const = []
        self.b_has_mats = False
        self.load_files()
        self.is_game_bl2 = unrealsdk.FindObject("Object", "GD_Itempools.Runnables.Pool_Bunker") is not None

    def Enable(self) -> None:
        hookmanager.instance.register_end_load(self.on_end_load, 5)

        for file in self.files:
            with open(file, "r") as File:
                for line in File:
                    if line.split() and line.split()[0].lower() == "set":
                        self.need_mat_inst_const.append(line.split()[1].strip())
        self.need_mat_inst_const = list(unrealsdk.FindObject("Object", x) for x in set(self.need_mat_inst_const))
        self.need_mat_inst_const = [x for x in self.need_mat_inst_const if x is not None]

        def command(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            x = params.Command.split()[0].strip().lower()
            if x == "update":
                self.get_free_mat_inst_consts(True)
                return False

            elif x == "exec_skin" and not self.is_game_bl2:
                # we need to read the file and find all MatInstConsts in case we are playing TPS
                binaries = self.PATH
                while os.path.basename(binaries).lower() != "binaries":
                    binaries = os.path.abspath(os.path.join(binaries, ".."))
                exec_file = os.path.join(binaries,
                                         params.Command.split()[1].lstrip("/").lstrip("\\"))  # this is case-sensitive
                if not os.path.isfile(exec_file):  # we could not find the file
                    return True
                with open(exec_file) as fp:
                    for l in fp:
                        if l.lower().startswith("set") and unrealsdk.FindObject("MaterialInstanceConstant",
                                                                                l.split()[1]) is not None:
                            try:
                                Materials.exec_skins(l, self.is_game_bl2)
                            except Exception as e:
                                logging.logger.error(e)
                                logging.logger.error(f"Error in: {l}")
                # we need to return false because fuck TPS.
                # If the game handles the exec it will sometimes not apply skins for whatever reason
                return False
                # we still want to return to the original function
            return True

        unrealsdk.RegisterHook("Engine.PlayerController.ConsoleCommand", "ConsoleCommand", command)

    def Disable(self) -> None:
        pass

    def on_end_load(self, curr_map: str) -> None:
        if not self.b_has_mats:
            self.get_free_mat_inst_consts()
            self.b_has_mats = True

    def load_files(self) -> None:
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".material"):
                    self.files.append(os.path.join(root, file))

    def get_free_mat_inst_consts(self, reload_only: bool = False) -> None:

        # We need any MeshComponent to create new MatInstConsts, I just use this cuz it's always loaded

        if not reload_only:
            # create and assign the new MatInstConsts
            for obj in self.need_mat_inst_const:
                mat = MESH.CreateAndSetMaterialInstanceConstant(0)
                unrealsdk.KeepAlive(mat)

                if obj.Class in (unrealsdk.FindClass("ClassModDefinition"),
                                 unrealsdk.FindClass("CrossDLCClassModDefinition"),
                                 unrealsdk.FindClass("ArtifactDefinition")):
                    obj.OverrideMaterial = mat
                else:
                    obj.Material = mat

        for file in self.files:
            with open(file, "r") as TemplateFile:
                for line in TemplateFile:
                    if not line.split() or line.split()[0].lower() != "set":
                        continue
                    else:
                        try:
                            Materials.exec_skins(line, self.is_game_bl2)
                        except Exception as e:
                            logging.logger.error(e)
                            logging.logger.error(f"Error in: {line}")

    @staticmethod
    def exec_skins(command: str, is_bl2: bool) -> None:
        """

        :type is_bl2: bool
        :type command: str
        """
        pc = bl2tools.get_player_controller()

        pattern_simple_param_name = re.compile("ParameterName=\"(.*?)\"")
        pattern_simple_float = re.compile("-?\d+\.\d+")
        pattern_simple_obj = re.compile("ParameterValue=(.*?),")
        pattern_simple_rgba = re.compile(
            "ParameterValue=\(R=(-?\d+\.\d+),G=(-?\d+\.\d+),B=(-?\d+\.\d+),A=(-?\d+\.\d+)\)")
        obj = unrealsdk.FindObject("Object", command.split()[1])

        if obj is None:
            # When we don't find our object, simply skip to the next line
            return

        # this is used in case we dynamically created a MatInstConst for a constructed MaterialPart, so we need to get
        # its MatInstConst from the known MatPart Object inside the '.Material' file.
        if obj.Class in (unrealsdk.FindClass("ClassModDefinition"),
                         unrealsdk.FindClass("CrossDLCClassModDefinition"),
                         unrealsdk.FindClass("ArtifactDefinition")):
            new_mat = obj.OverrideMaterial
        else:
            new_mat = obj.Material

        # this happens if we are not using the .material file and want to edit the MatInstConst object directly
        if new_mat is None:
            new_mat = obj


        if is_bl2:
            set_cmd = "set "
            set_cmd += bl2tools.get_obj_path_name(new_mat) + " "
            set_cmd += command.split()[2] + " " + command.split()[3]
            pc.ConsoleCommand(set_cmd, 1)

        # The following code will only run if the game is TPS
        else:
            attr = command.split()[2].lower()
            values = command.split()[3].strip()
            if attr == "parent":
                new_mat.SetParent(unrealsdk.FindObject("Object", values))
            elif attr == "scalarparametervalues":
                for param, val in zip(re.finditer(pattern_simple_param_name, values),
                                      re.finditer(pattern_simple_float, values)):
                    value = float(val.group())
                    new_mat.SetScalarParameterValue(param.group(1), value)
                    logging.logger.verbose(
                        f"{bl2tools.get_obj_path_name(new_mat)}.SetScalarParameterValue({param.group(1)}, {value})")

            elif attr == "textureparametervalues":
                for param, val in zip(re.finditer(pattern_simple_param_name, values),
                                      re.finditer(pattern_simple_obj, values)):
                    value = unrealsdk.FindObject("Object", val.group(1))
                    new_mat.SetTextureParameterValue(param.group(1), value)
                    logging.logger.verbose(
                        f"{bl2tools.get_obj_path_name(new_mat)}.SetTextureParameterValue({param.group(1)}, {value})")
            elif attr == "vectorparametervalues":
                for param, val in zip(re.finditer(pattern_simple_param_name, values),
                                      re.finditer(pattern_simple_rgba, values)):
                    new_mat.SetVectorParameterValue(param.group(1),
                                                    tuple(float(x) for x in val.groups()))
                    logging.logger.verbose(
                        f"{bl2tools.get_obj_path_name(new_mat)}.SetVectorParameterValue({param.group(1)}, "
                        f"{tuple(float(x) for x in val.groups())})")
