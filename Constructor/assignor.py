import unrealsdk
from unrealsdk import *

from . import set_iterpreter as set, bl2tools, logging

import re
import os


@logging.log_all_calls(logging.call_logger)
class Assignor:

    def __init__(self, path):
        self.PATH = path
        self.itempool_files = []
        self.assign_files = []
        self.set_files = []
        self.reward_files = []
        self.lootable_files = []
        self.load_files()

    def Enable(self):
        self.lootpool_helper()
        self.missionreward_helper()
        self.assign_force_set()

    def Disable(self):
        pass

    def on_end_load(self):
        self.assign_force_set()
        self.lootpool_helper()
        self.assign_pools()
        self.assign_lootables()

    def load_files(self):
        # The file extensions may not really make sense all of the time, but thats a bit too late to change now
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".itempool"):
                    with open(os.path.join(root, file), "r", encoding="cp1252") as f:
                        self.itempool_files.extend([x.rstrip() for x in f if x.rstrip()])
                elif file.lower().endswith(".assign"):
                    with open(os.path.join(root, file), "r", encoding="cp1252") as f:
                        self.assign_files.extend([x.rstrip() for x in f if x.rstrip()])
                elif file.lower().endswith(".set"):
                    with open(os.path.join(root, file), "r", encoding="cp1252") as f:
                        self.set_files.extend([x.rstrip() for x in f if x.rstrip()])

                elif file.lower().endswith(".reward"):
                    with open(os.path.join(root, file), "r", encoding="cp1252") as f:
                        self.reward_files.extend([x.rstrip() for x in f if x.rstrip()])
                elif file.lower().endswith(".lootable"):
                    with open(os.path.join(root, file), "r", encoding="cp1252") as f:
                        self.lootable_files.extend([x.rstrip() for x in f if x.rstrip()])

    def lootpool_helper(self):
        """
        Reads in all "*.itempool" text files and then assigns them as usual.
        To assign custom Constructed items to Lootpools you need to rely on this function.
        It does not work to use simple set commands on them, if you do so the ItemPool will be completely empty.
        To Add anything to a Itempool just look at the Template I provided, you can add or remove anything you desire.
        Just make sure you follow the instructions!!!
        """
        b_skip_to_next = False
        for line in self.itempool_files:
            if line[0] == "/":
                b_skip_to_next = False

            if not line.split() or line[0] == "-" or b_skip_to_next:
                continue
            elif line[0] == "/":
                if line[1:].strip() == str(GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()) \
                        or line[1:].strip() == "None":
                    continue
                else:
                    b_skip_to_next = True
            elif line.split()[0].lower() == "set":
                set.set(line)
            elif line[0] == "#":
                item_pool_str = line[1:].strip()
                item_pool = unrealsdk.FindObject("ItemPoolDefinition", item_pool_str)
                temp_list = []
                if not item_pool:
                    b_skip_to_next = True
                    continue
            elif "ItemPoolDefinition" in line:
                item_pool_definition = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "InvBalanceDefinition" in line:
                inv_balance_definition = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "BaseValueConstant" in line:
                base_value_constant = float(line.split()[1].strip())
            elif "BaseValueAttribute" in line:
                base_value_attribute = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "InitializationDefinition" in line:
                initialization_definition = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "BaseValueScaleConstant" in line:
                base_value_scale_constant = float(line.split()[1].strip())
            elif "bDropOnDeath" in line:
                if line.split()[1].strip() == "True":
                    b_drop_on_death = True
                else:
                    b_drop_on_death = False
                ArrayEntry = (
                    item_pool_definition,
                    inv_balance_definition,
                    (
                        base_value_constant,
                        base_value_attribute,
                        initialization_definition,
                        base_value_scale_constant
                    ),
                    b_drop_on_death
                )
                temp_list.append(ArrayEntry)
            elif line.split()[0] in ["+", "++"]:
                if line.split()[0] == "++":
                    existing = [
                        (
                            x.ItmPoolDefinition, x.InvBalanceDefinition, (
                                x.Probability.BaseValueConstant, x.Probability.BaseValueAttribute,
                                x.Probability.InitializationDefinition, x.Probability.BaseValueScaleConstant
                            ),
                            x.bDropOnDeath
                        )
                        for x in item_pool.BalancedItems
                    ]
                    # if all our appended items are already exist in the pool, dont append them.
                    if not all(x in existing for x in temp_list):
                        existing.extend(temp_list)
                    temp_list = existing
                item_pool.BalancedItems = temp_list
                temp_list.clear()

    def missionreward_helper(self):
        """
        It's not really possible to set constructed items as a mission reward using legacy set commands, thats what this
        function is for. The .reward files should be easy enough to use for everyone i hope.
        """
        for line in self.reward_files:
            try:
                if not line.split() or line[0] == "-":
                    continue
                elif line.split()[0].lower() == "set":
                    set.set(line)
                elif line[0] == "#":
                    mission_definition = unrealsdk.FindObject("MissionDefinition", line[1:].strip())
                elif line[0] == "+":
                    reward_array = line[1:].strip()
                else:
                    if reward_array == "RewardItems":
                        mission_definition.Reward.RewardItems = [FindObject("Object", x.strip())
                                                                 for x in line.split(",")]
                    elif reward_array == "RewardItemPools":
                        mission_definition.Reward.RewardItemPools = [FindObject("Object", x.strip())
                                                                     for x in line.split(",")]
                    elif reward_array == "AlternativeRewardItems":
                        mission_definition.AlternativeReward.RewardItems = [FindObject("Object", x.strip())
                                                                            for x in line.split(",")]
                    elif reward_array == "AlternativeRewardItemPools":
                        mission_definition.AlternativeReward.RewardItemPools = [FindObject("Object", x.strip())
                                                                                for x in line.split(",")]
            except Exception as e:
                logging.logger.error(e)
                logging.logger.error(f"Please check this line: {line}")

    def assign_pools(self):
        """
        To assign custom created ItemPools to a Pawn we need to use the SDK.
        Normal set commands do not work.
        Reads in all .assign files and assigns the pools to the corresponding Pawn.
        """
        b_skip = False
        for line in self.assign_files:
            if not line.split() or line[0] == "-":
                continue
            if line[0] == "#":
                b_skip = False
            if b_skip:
                continue
            elif line.split()[0].lower() == "set":
                set.set(line)
            if line[0] == "#":
                pawn_str = line[1:].strip()
                drop_source = unrealsdk.FindObject("Object", pawn_str)
                if drop_source is None:
                    b_skip = True
                    continue
                temp_list = []
            elif "ItemPool" in line:
                item_pool_definition = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "BaseValueConstant" in line:
                base_value_constant = float(line.split()[1].strip())
            elif "BaseValueAttribute" in line:
                base_value_attribute = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "InitializationDefinition" in line:
                initialization_definition = unrealsdk.FindObject("Object", line.split()[1].strip())
            elif "BaseValueScaleConstant" in line:
                base_value_scale_constant = float(line.split()[1].strip())
                array_entry = (
                    item_pool_definition,
                    (
                        base_value_constant,
                        base_value_attribute,
                        initialization_definition,
                        base_value_scale_constant
                    )
                )
                temp_list.append(array_entry)
            elif line.split()[0] in ["+", "++"]:
                if line.split()[0] == "++":
                    if bl2tools.obj_is_in_class(drop_source, "Behavior_SpawnItems"):
                        existing = drop_source.ItemPoolList
                    else:
                        existing = drop_source.DefaultItemPoolList
                    existing = [
                        (
                            x.ItemPool, (
                                x.PoolProbability.BaseValueConstant, x.PoolProbability.BaseValueAttribute,
                                x.PoolProbability.InitializationDefinition, x.PoolProbability.BaseValueScaleConstant
                            )
                        ) for x in existing
                    ]
                    # if all our appended items are already exist in the pool, dont append them.
                    if not all(x in existing for x in temp_list):
                        existing.extend(temp_list)
                    temp_list = existing

                if bl2tools.obj_is_in_class(drop_source, "Behavior_SpawnItems"):
                    drop_source.ItemPoolList = temp_list
                else:
                    drop_source.DefaultItemPoolList = temp_list
                temp_list.clear()

    def assign_lootables(self):
        b_skip_to_next = False
        for line in self.lootable_files:
            if line[0] == "/":
                b_skip_to_next = False

            if not line.split() or line[0] == "-" or b_skip_to_next:
                continue
            elif line.split()[0].lower() == "set":
                set.set(line)
            elif line[0] == "/":
                if line[1:].strip() == str(GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()) \
                        or line[1:].strip() == "None":
                    continue
                else:
                    b_skip_to_next = True
            elif line[0] == "#":
                lootable_obj = FindObject("Object", line[1:].strip())
                if lootable_obj is None:
                    b_skip_to_next = True
                    continue
                b_first_entry = True
                default_loot = []
                temp_list = []
            elif "ConfigurationName" in line:
                if not b_first_entry:
                    default_loot.append((configuration_name,
                                         loot_game_stage_variance_formula,
                                         (weight_bvc, weight_bva, weight_ini, weight_bvsc),
                                         temp_list.copy()))
                    temp_list.clear()
                else:
                    b_first_entry = False
                configuration_name = line.split()[1].strip()
            elif "LootGameStageVarianceFormula" in line:
                loot_game_stage_variance_formula = FindObject("Object", line.split()[1].strip())
            elif "Weight.BaseValueConstant" in line:
                weight_bvc = float(line.split()[1].strip())
            elif "Weight.BaseValueAttribute" in line:
                weight_bva = FindObject("Object", line.split()[1].strip())
            elif "Weight.InitializationDefinition" in line:
                weight_ini = FindObject("Object", line.split()[1].strip())
            elif "Weight.BaseValueScaleConstant" in line:
                weight_bvsc = float(line.split()[1].strip())
            elif "ItemPool" in line:
                item_pool = FindObject("ItemPoolDefinition", line.split()[1].strip())
            elif "PoolProbability.BaseValueConstant" in line:
                pool_bvc = float(line.split()[1].strip())
            elif "PoolProbability.BaseValueAttribute" in line:
                pool_bva = FindObject("ItemPoolDefinition", line.split()[1].strip())
            elif "PoolProbability.InitializationDefinition" in line:
                pool_ini = FindObject("ItemPoolDefinition", line.split()[1].strip())
            elif "PoolProbability.BaseValueScaleConstant" in line:
                pool_bvsc = float(line.split()[1].strip())
            elif "AttachmentPointName" in line:
                att_point = line.split()[1].strip()
                array_entry = (item_pool, (pool_bvc, pool_bva, pool_ini, pool_bvsc), att_point)
                temp_list.append(array_entry)
            elif line.split()[0] in ["+", "++"]:  # either overwrite or append to existing lootlist
                default_loot.append((configuration_name,
                                     loot_game_stage_variance_formula,
                                     (weight_bvc, weight_bva, weight_ini, weight_bvsc),
                                     temp_list))
                if line.split()[0] == "++":  # append
                    if bl2tools.obj_is_in_class(lootable_obj, "InteractiveObjectLootListDefinition"):
                        existing = lootable_obj.LootData
                    else:
                        existing = lootable_obj.DefaultLoot
                    existing = [
                        (
                            x.ConfigurationName, x.LootGameStageVarianceFormula,
                            (
                                x.Weight.BaseValueConstant, x.Weight.BaseValueAttribute,
                                x.Weight.InitializationDefinition, x.Weight.BaseValueScaleConstant
                            ),
                            [
                                (
                                    y.ItemPool,
                                    (
                                        y.PoolProbability.BaseValueConstant, y.PoolProbability.BaseValueAttribute,
                                        y.PoolProbability.InitializationDefinition,
                                        y.PoolProbability.BaseValueScaleConstant
                                    ),
                                    y.AttachmentPointName
                                ) for y in x.ItemAttachments
                            ]
                        ) for x in existing]

                    # if all our appended items are already exist in the pool, dont append them.
                    if not all(x in existing for x in temp_list):
                        existing.extend(default_loot)
                    default_loot = existing

                if bl2tools.obj_is_in_class(lootable_obj, "InteractiveObjectLootListDefinition"):
                    lootable_obj.LootData = default_loot
                else:
                    lootable_obj.DefaultLoot = default_loot
                temp_list.clear()
                default_loot.clear()

    def assign_force_set(self):
        """
        This function reads in all the .set files and will then use the sdk to directly assign the new values to our obj
        This can also be used for some simple 'hotfix' like things on mapload
        Mostly usefull for constructed stuff or to set stuff cross dlcs
        """
        b_skip_to_next = False
        for line in self.set_files:
            if line[0] == "/":
                b_skip_to_next = False

            if not line.split() or line[0] == "-" or b_skip_to_next:
                continue
            elif line[0] == "/":
                if line[1:].strip() == str(GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()) \
                        or line[1:].strip() == "None":
                    continue
                else:
                    b_skip_to_next = True

            elif line.split()[0].lower() == "set":
                set.set(line)
