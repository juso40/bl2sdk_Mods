import os
import re
from typing import Dict, List

import unrealsdk  # type: ignore

from Mods.ModMenu import Game

from . import bl2tools, logging, matinstconsts


@logging.log_all_calls(logging.call_logger)
class Hotfixer:
    def __init__(self, path: os.PathLike) -> None:
        self.PATH = path
        self.definition_files = []
        self.keys: List[str] = []
        self.values: List[str] = []
        self.is_game_bl2: bool = Game.GetCurrent() == Game.BL2
        self.load_files()

    def Enable(self) -> None:  # noqa: N802
        self.merge_files()
        self.execute()
        self.keys.clear()
        self.values.clear()

    def Disable(self) -> None:  # noqa: N802
        pass

    def load_files(self) -> None:
        for root, _dirs, filenames in os.walk(self.PATH):
            for file in sorted([os.path.join(root, x) for x in filenames]):
                # .definition as alternative suffix support for Exodus
                if file.lower().endswith(".definition") or file.lower().endswith(".blcm"):
                    logging.logger.info(f"Loading: {file}")
                    self.definition_files.append(file)

    def execute(self) -> None:
        """Execute our merged file"""
        file = os.path.join(self.PATH, "merge.txt")

        # if tps, "set" the skins fix
        if not self.is_game_bl2:
            with open(file, encoding="cp1252") as fp:
                lines: List[str] = fp.readlines()

            with open(file, "w") as fp:
                for line in lines:
                    # If the line is a set command on a MaterialInstanceConstant
                    # manually exec the skin set command
                    if (
                        line.lower().startswith("set")
                        and unrealsdk.FindObject("MaterialInstanceConstant", line.split()[1]) is not None
                    ):
                        logging.logger.debug(f"TPS skin-fix on: {line.split()[1]}")
                        try:
                            matinstconsts.Materials.exec_skins(line, self.is_game_bl2)
                        except Exception as e:  # noqa: BLE001
                            logging.logger.error(e)
                            logging.logger.error(f"Error in: {line}")
                    else:
                        fp.write(line)

        exec_path = str(file).split("Binaries\\", 1)[1]
        bl2tools.console_command("exec " + exec_path, False)
        # Clean up the file
        os.remove(file)

    def merge_files(self) -> None:
        spark_service_configuration: str = ""
        set_cmd = "set {} {} ({})\n"
        with open(os.path.join(self.PATH, "merge.txt"), "w", encoding="cp1252") as merge_fp:
            for file in self.definition_files:
                with open(file, encoding="cp1252") as fp:
                    for line in fp:
                        if line.lstrip().lower().startswith("set"):
                            if "SparkService" not in line:  # write normal set commands directly to merge.txt
                                merge_fp.write(line)
                            else:
                                # Hotfixes require manual merging later on
                                _split = line.split(maxsplit=3)
                                attr = _split[2]  # set0 Object1 attribute2 value3:
                                to_merge = _split[3].rstrip()
                                if attr.lower() == "keys":
                                    self.keys.append(to_merge[1:-1])
                                elif attr.lower() == "values":
                                    self.values.append(to_merge[1:-1])

            # Find the appropriate HotFix method, either:
            # Online -> Use the existing SparkServiceConfiguration
            # Offline -> Create a new SparkServiceConfiguration for our hotfixes
            for x in unrealsdk.FindAll("SparkServiceConfiguration"):
                if x.ServiceName == "Micropatch":  # Online
                    spark_service_configuration = x.PathName(x)
                    logging.logger.debug(f"Found SparkServiceConfiguration: {spark_service_configuration}")
                    break
            if not spark_service_configuration:  # Offline
                logging.logger.debug("No Micropatch SparkServiceConfiguration found, creating one")
                # Dump the current SparkServiceConfiguration to the merge file
                spark_service_configuration = "Transient.SparkServiceConfiguration_0"
                merge_fp.write(f"set {spark_service_configuration} ServiceName Micropatch\n")
                merge_fp.write(f"set {spark_service_configuration} ConfigurationGroup Default\n")
                gb_acc = unrealsdk.FindAll("GearboxAccountData")[-1]
                merge_fp.write(
                    f"set {gb_acc.PathName(gb_acc)} Services ({spark_service_configuration})\n",
                )

            # remove double gearbox hotfixes
            all_keys: str = ",".join(self.keys)
            all_vals: str = ",".join(self.values)

            pat = re.compile(r"\"([^\"\\]*(?:\\.[^\"\\]*)*)\"")

            # NOTE: ======== Map Change Crashes ========
            # NOTE: Trinton Flats to Stanton's Liver
            # NOTE: Outlands Spur to Outlands Canyon
            # AUTOR: - Neumatic

            # NOTE: For BL2 23 official hotfixes are being injected
            # NOTE: For TPS 21 official hotfixes are being injected
            # NOTE: OpenBLCMM injects the official hotfix data with the keys f'*-BLCMM{i}'
            # NOTE: The legacy BLCMM uses f'*-GBX_fixes{i}' or f'*-GBX_Fixes{i}' depending on the hotfix type
            #
            # We probably shouldn't generally assume that every hotfix file includes every official hotfix
            # but for Exodus at least, the initial file will always include all official hotfixes.
            # So we can simply filter out the first 21 or 23 hotfixes depending on the game.
            # We do so by checking for the keys and adding the values to a set.
            # And later on removing duplicate hotfix values from the merge file.

            tmp_keys: List[str] = []
            for i in range(1, int([22, 24][self.is_game_bl2])):
                tmp_keys.append(f"blcmm{i}")  # thanks to Neumatic on Discord
                tmp_keys.append(f"gbx_fixes{i}")
            official_hotfixes: tuple = tuple(tmp_keys)

            gbx_vals: set = set()
            own_keys: List[str] = []
            own_vals: List[str] = []
            # NOTE: When merging multiple hotfix files we most likely will have duplicate keys
            # NOTE: Hotfix values with duplicate keys will be ignored by the game
            key_fixup: Dict[str, int] = {}
            k: str
            v: str
            for k, v in zip(re.findall(pat, all_keys), re.findall(pat, all_vals)):
                if v not in gbx_vals:  # on first occurence of a gbx hotfix, add it to the merge file
                    key: str = k
                    if k in key_fixup:
                        key = f"{k}_{key_fixup[k]}"
                        key_fixup[k] += 1
                    else:
                        key_fixup[k] = 1
                    own_keys.append(f'"{key}"')
                    own_vals.append(f'"{v}"')
                if k.lower().endswith(official_hotfixes):  # filter out all duplicate gbx hotfixes
                    gbx_vals.add(v)

            merge_fp.write(set_cmd.format(spark_service_configuration, "Keys", ",".join(own_keys)))
            merge_fp.write(set_cmd.format(spark_service_configuration, "Values", ",".join(own_vals)))
