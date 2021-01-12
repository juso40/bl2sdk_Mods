import unrealsdk
from unrealsdk import *

from Exodus import set_iterpreter
from Exodus import bl2tools

import os
import random


class Spawner:
    def __init__(self, PATH):
        self.PATH = PATH
        self.file_data = []

    def Enable(self):
        self.load_files()

    def Disable(self):
        pass

    def load_files(self):
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".spawn"):
                    with open(os.path.join(root, file), "r") as f:
                        self.file_data.extend([x.strip() for x in f if x.rstrip()])

    def on_end_load(self):
        # After the map loads, we want to check our loaded file data for things to spawn.
        in_class = None
        b_skip_to_next = False
        for line in self.file_data:
            if line[0] == "/":  # we now want to check if its the map we just loaded in
                if line[1:].strip().lower() == str(
                        GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()).lower() or\
                        line[1:].strip().lower() == "none":
                    continue
                else:
                    b_skip_to_next = True
            elif line[0] == "-" or b_skip_to_next:  # The line does not start with a map check, continue to next line.
                continue
            elif line[0] == "#":  # We now have the class of the objects that we will spawn
                in_class = line[1:].lstrip()
            else:  # This should now be the "<Object> <Location> [level offset]
                line = line.split()
                if in_class.lower() == "WeaponBalanceDefinition".lower():
                    self.spawn_item_from_balance_definition(in_class, line)

    def spawn_item_from_balance_definition(self, balance_definition, line_list):
        world_info = unrealsdk.GetEngine().GetCurrentWorldInfo()
        if balance_definition.lower() == "WeaponBalanceDefinition".lower():
            def_data = Spawner.get_item_def_data(balance_definition, line_list[0], (50, 50))
            item = world_info.Spawn(unrealsdk.FindClass("WillowWeapon"), None, "None", (), (), None, True)
            item.InitializeFromDefinitionData(def_data, None)
            pickup = unrealsdk.FindAll("WillowPickup")[-1].WillowPickup(item.GetPickup(True, True))  # dies here, Nonetype is not callable
            pickup.AdjustPickupPhysicsAndCollisionForBeingAttached()
            pickup.bCanBeSavedAcrossLevelTransition = False
            bl2tools.console_command(f"obj dump {bl2tools.get_obj_path_name(item)}")

    @staticmethod
    def get_item_def_data(balance_definition, obj_path_name, level_range):
        if balance_definition.lower() == "WeaponBalanceDefinition".lower():
            obj = unrealsdk.FindObject(balance_definition, obj_path_name)
            part_list = obj.RuntimePartListCollection

            WeaponTypeDefinition = part_list.AssociatedWeaponType
            BalanceDefinition = obj
            ManufacturerDefinition = None

            t = obj
            while t.BaseDefinition:
                t = t.BaseDefinition
            ManufacturerDefinition = t.Manufacturers[0].Manufacturer

            ManufacturerGradeIndex = random.randint(*level_range)
            BodyPartDefinition = None if not part_list.BodyPartData.bEnabled else random.choice(
                [x.Part for x in part_list.BodyPartData.WeightedParts])
            GripPartDefinition = None if not part_list.GripPartData.bEnabled else random.choice(
                [x.Part for x in part_list.GripPartData.WeightedParts]
            )
            BarrelPartDefinition = None if not part_list.BarrelPartData.bEnabled else random.choice(
                [x.Part for x in part_list.BarrelPartData.WeightedParts]
            )
            SightPartDefinition = None if not part_list.SightPartData.bEnabled else random.choice(
                [x.Part for x in part_list.SightPartData.WeightedParts]
            )
            StockPartDefinition = None if not part_list.StockPartData.bEnabled else random.choice(
                [x.Part for x in part_list.StockPartData.WeightedParts]
            )
            ElementalPartDefinition = None if not part_list.ElementalPartData.bEnabled else random.choice(
                [x.Part for x in part_list.ElementalPartData.WeightedParts]
            )
            Accessory1PartDefinition = None if not part_list.Accessory1PartData.bEnabled else random.choice(
                [x.Part for x in part_list.Accessory1PartData.WeightedParts]
            )
            Accessory2PartDefinition = None if not part_list.Accessory2PartData.bEnabled else random.choice(
                [x.Part for x in part_list.Accessory2PartData.WeightedParts]
            )
            MaterialPartDefinition = None if not part_list.MaterialPartData.bEnabled else random.choice(
                [x.Part for x in part_list.MaterialPartData.WeightedParts]
            )
            PrefixPartDefinition = None
            TitlePartDefinition = None if not BarrelPartDefinition else BarrelPartDefinition.TitleList[0]
            GameStage = ManufacturerGradeIndex
            UniqueId = -1
            return (
                WeaponTypeDefinition, BalanceDefinition, ManufacturerDefinition, ManufacturerGradeIndex,
                BodyPartDefinition,
                GripPartDefinition, BarrelPartDefinition, SightPartDefinition, StockPartDefinition,
                ElementalPartDefinition,
                Accessory1PartDefinition, Accessory2PartDefinition, MaterialPartDefinition, PrefixPartDefinition,
                TitlePartDefinition, GameStage, UniqueId)
