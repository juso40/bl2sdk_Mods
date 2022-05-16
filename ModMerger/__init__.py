import os
import re

import unrealsdk
from unrealsdk import *

from ..ModMenu import EnabledSaveType, ModTypes, SDKMod, RegisterMod

try:
    from Mods import CommandExtensions
except ImportError:
    CommandExtensions = None


class ModMerger(SDKMod):
    Name = "Mod Merger"
    Description = "Small mod that Merges any .blcm mod file in its subfolders. Will also guarantee that the mods " \
                  "hotfixes will work, both online and offline."
    Author = "Juso"
    Version = "2.1"
    Types = ModTypes.Utility
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu

    def __init__(self):
        self.PATH = os.path.dirname(os.path.realpath(__file__))
        self.definition_files = []
        self.keys = []
        self.values = []
        self.load_files()

    def Enable(self):
        self.merge_files()
        self.execute()
        self.keys.clear()
        self.values.clear()

    def Disable(self):
        pass

    def load_files(self):
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".txt") or file.lower().endswith(".blcm"):
                    self.definition_files.append(os.path.join(root, file))

    def execute(self):
        """
        Executes our merged file
        """
        file = os.path.join(self.PATH, "merge.txt")
        exec_path = str(file).split("Binaries\\", 1)[1]
        if CommandExtensions is not None:
            CommandExtensions.try_handle_command("exec", f"\"{exec_path}\"")
        else:
            unrealsdk.GetEngine().GamePlayers[0].Actor.ConsoleCommand("exec " + exec_path, False)
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


RegisterMod(ModMerger())
