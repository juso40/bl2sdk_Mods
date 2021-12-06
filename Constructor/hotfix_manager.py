import os
import re
from typing import List

import unrealsdk
from unrealsdk import *

from . import bl2tools, logging, matinstconsts
from ..ModMenu import Game


@logging.log_all_calls(logging.call_logger)
class Hotfixer:

    def __init__(self, path: os.PathLike):
        self.PATH = path
        self.definition_files = []
        self.keys = []
        self.values = []
        self.is_game_bl2 = Game.GetCurrent() == Game.BL2
        self.load_files()

    def Enable(self) -> None:
        self.merge_files()
        self.execute()
        self.keys.clear()
        self.values.clear()

    def Disable(self) -> None:
        pass

    def load_files(self) -> None:
        for root, dirs, filenames in os.walk(self.PATH):
            for file in sorted([os.path.join(root, x) for x in filenames]):
                # .definition as alternative suffix support for Exodus
                if file.lower().endswith(".definition") or file.lower().endswith(".blcm"):
                    logging.logger.info(f"Loading: {file}")
                    self.definition_files.append(file)

    def execute(self) -> None:
        """
        Executes our merged file
        """
        file = os.path.join(self.PATH, "merge.txt")

        # if tps, "set" the skins fix
        if not self.is_game_bl2:
            with open(file, "r") as fp:
                lines: List[str] = fp.readlines()

            with open(file, "w") as fp:
                for l in lines:  # type: str
                    if l.lower().startswith("set") and unrealsdk.FindObject("MaterialInstanceConstant",
                                                                            l.split()[1]) is not None:
                        logging.logger.debug(f"TPS skin-fix on: {l.split()[1]}")
                        try:
                            matinstconsts.Materials.exec_skins(l, self.is_game_bl2)
                        except Exception as e:
                            logging.logger.error(e)
                            logging.logger.error(f"Error in: {l}")
                    else:
                        fp.write(l)

        exec_path = str(file).split("Binaries\\", 1)[1]
        bl2tools.console_command("exec " + exec_path, False)
        # Clean up the file
        os.remove(file)

    def merge_files(self) -> None:
        SparkServiceConfiguration = None
        set_cmd = "set {} {} ({})\n"
        with open(os.path.join(self.PATH, "merge.txt"), "w", encoding="cp1252") as merge_fp:
            for file in self.definition_files:
                with open(file, "r", encoding="cp1252") as fp:
                    for line in fp:
                        if line.lstrip().lower().startswith("set"):
                            if "SparkService" not in line:
                                merge_fp.write(line)
                            else:
                                _split = line.split(maxsplit=3)
                                attr = _split[2]  # set0 Object1 attribute2 value3:
                                to_merge = _split[3].rstrip()
                                if attr.lower() == "keys":
                                    self.keys.append(to_merge[1:-1])
                                elif attr.lower() == "values":
                                    self.values.append(to_merge[1:-1])

            for x in unrealsdk.FindAll("SparkServiceConfiguration"):
                if x.ServiceName == "Micropatch":
                    SparkServiceConfiguration = x.PathName(x)
                    break
            if not SparkServiceConfiguration:
                SparkServiceConfiguration = "Transient.SparkServiceConfiguration_0"
                merge_fp.write("set Transient.SparkServiceConfiguration_0 ServiceName Micropatch\n")
                merge_fp.write("set Transient.SparkServiceConfiguration_0 ConfigurationGroup Default\n")
                gb_acc = unrealsdk.FindAll("GearboxAccountData")[-1]
                merge_fp.write(
                    "set {} Services (Transient.SparkServiceConfiguration_0)\n".format(gb_acc.PathName(gb_acc)))
                # remove double gearbox hotfixes
            all_keys = ",".join(self.keys)
            all_vals = ",".join(self.values)

            pat = re.compile(r"\"([^\"\\]*(?:\\.[^\"\\]*)*)\"")

            gbx_keys = set()
            gbx_vals = set()
            own_keys = list()
            own_vals = list()
            for k, v in zip(re.findall(pat, all_keys), re.findall(pat, all_vals)):
                if k not in gbx_keys:
                    own_keys.append(f"\"{k}\"")
                    own_vals.append(f"\"{v}\"")
                if "gbx_fixes" in k.lower():  # filter out all duplicate gbx hotfixes
                    gbx_keys.add(k)
                    gbx_vals.add(v)

            merge_fp.write(set_cmd.format(SparkServiceConfiguration, "Keys", ",".join(own_keys)))
            merge_fp.write(set_cmd.format(SparkServiceConfiguration, "Values", ",".join(own_vals)))
