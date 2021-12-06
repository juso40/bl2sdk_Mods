from typing import Tuple, List

import unrealsdk
from unrealsdk import *

from . import set_iterpreter
from . import bl2tools
from . import logging
from . import hookmanager

import os
import random
import re


@logging.log_all_calls(logging.call_logger)
class Spawner:
    def __init__(self, path: os.PathLike):
        self.PATH: os.PathLike = path
        self.file_data = []
        self.xyz_pattern = re.compile(r"\(\s*x\s*=(?P<x>.*?),\s*y\s*=(?P<y>.*?),\s*z\s*=(?P<z>.*?)\)",
                                      flags=re.IGNORECASE)
        self.rot_pattern = re.compile(r"\(pitch\s*=(?P<pitch>.*?),\s*yaw\s*=(?P<yaw>.*?),\s*roll\s*=(?P<roll>.*?)\)",
                                      flags=re.IGNORECASE)
        self.lvl_pattern = re.compile(r"\(\s*(?P<low>-?\d*?)\s*,\s*(?P<high>-?\d*?)\s*\)")
        self.is_game_bl2: bool = unrealsdk.FindObject("Object", "GD_Itempools.Runnables.Pool_Bunker") is not None
        self.spawned_pawns: List[unrealsdk.UObject] = []

    def Enable(self) -> None:
        hookmanager.instance.register_end_load(self.on_end_load, 4)
        hookmanager.instance.register_start_load(self.on_start_load, 0)
        self.load_files()

    def Disable(self) -> None:
        pass

    def on_start_load(self, movie_name: str) -> None:
        if movie_name != "Loading.bik":  # loading main menu, all pawns already got cleaned up
            # for some weird reason some WillowAiPawns don't get destroyed, resulting in endless loading screens
            for pawn in self.spawned_pawns:
                if pawn:
                    unrealsdk.Log(bl2tools.get_obj_path_name(pawn))
                    pawn.Destroyed()
        self.spawned_pawns.clear()  # all pawns are dead

    def load_files(self) -> None:
        self.file_data.clear()
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".spawn"):
                    with open(os.path.join(root, file), "r", encoding="cp1252") as f:
                        self.file_data.extend([x.strip() for x in f if x.rstrip()])

    def on_end_load(self, curr_map: str) -> None:
        if logging.logger.level in logging.logger.levels[:2]:
            self.load_files()

        # After the map loads, we want to check our loaded file data for things to spawn.
        random_spawn_group = {}
        add_to_group = None
        in_class = None
        region_game_stage: int = set_iterpreter.get_current_region_stage()
        b_skip_to_next: bool = False
        b_skip_once: bool = False
        for line in self.file_data:  # type: str
            try:
                if line[0] == "/":  # we now want to check if it's the map we just loaded in
                    if line[1:].strip().lower() == curr_map or line[1:].strip().lower() == "none":
                        b_skip_to_next = False
                        continue
                    else:
                        b_skip_to_next = True
                elif line[0] == "-" or b_skip_to_next:
                    continue

                elif line[0] == "!":
                    unrealsdk.LoadPackage(line[1:].strip())
                elif line[0] == "#":  # We now have the class of the objects that we will spawn
                    in_class: str
                    in_class = line[1:].lstrip()
                elif line[0] == "+":  # check the given conditions
                    __conditional_ret = set_iterpreter.check_conditions(line[1:])
                    if isinstance(__conditional_ret, bool):
                        b_skip_once = __conditional_ret
                    else:
                        add_to_group = __conditional_ret
                else:  # This should now be the "<Object> <Location> <Rotation> [level offset]
                    if b_skip_once:  # earlier given conditions failed, skip this
                        b_skip_once = False
                        continue

                    if add_to_group is not None:
                        random_spawn_group.setdefault(in_class, {add_to_group: []})[add_to_group].append(
                            (line, region_game_stage)
                        )
                        add_to_group = None  # we always only want to add the next line to the group
                    else:  # if not added to randomGroup just exec now
                        if in_class.lower() == "WeaponBalanceDefinition".lower() \
                                or in_class.lower() == "InventoryBalanceDefinition".lower():
                            self.spawn_item_from_balance_definition(in_class, line, region_game_stage)
                        elif in_class.lower() == "AIPawnBalanceDefinition".lower():
                            self.spawn_ai_pawn(line, region_game_stage)
                        elif in_class.lower() == "InteractiveObjectBalanceDefinition".lower() \
                                or in_class.lower() == "InteractiveObjectDefinition".lower():
                            self.spawn_interactive_object(line, region_game_stage)
            except Exception as e:
                logging.logger.error(repr(e))
                logging.logger.error(f"Please check the following line in your .spawn file:\n-> {line}")

        for cls, group in random_spawn_group.items():
            for g_name, choice_of in group.items():
                l: Tuple[str, int] = random.choice(choice_of)
                try:
                    if cls.lower() == "WeaponBalanceDefinition".lower() \
                            or cls.lower() == "InventoryBalanceDefinition".lower():
                        self.spawn_item_from_balance_definition(cls, *l)
                    elif cls.lower() == "AIPawnBalanceDefinition".lower():
                        self.spawn_ai_pawn(*l)
                    elif in_class.lower() == "InteractiveObjectBalanceDefinition".lower() \
                            or in_class.lower() == "InteractiveObjectDefinition".lower():
                        self.spawn_interactive_object(*l)
                except Exception as e:
                    logging.logger.error(repr(e))
                    logging.logger.error(f"Please check the following line in your .spawn file:\n-> {l}")

    def spawn_ai_pawn(self, line: str, level: int) -> None:
        m = re.search(self.xyz_pattern, line)
        _xyz = (float(m.group("x")), float(m.group("y")), float(m.group("z")))
        m = re.search(self.rot_pattern, line)
        _rotation = (int(m.group("pitch")), int(m.group("yaw")), int(m.group("roll")))
        m = re.search(self.lvl_pattern, line)
        if m:
            _level = (max(level + int(m.group("low")), 1), max(level + int(m.group("high")), 1))
        else:
            _level = (level, level)

        ai_pawn_obj_str = line.split(" ", 1)[0]
        ai_pawn_balance_def = unrealsdk.FindObject("AIPawnBalanceDefinition", ai_pawn_obj_str)
        if ai_pawn_balance_def is None:
            logging.logger.error(f"Could not find object AIPawnBalanceDefinition'{ai_pawn_obj_str}'!")
            return

        pop_master = unrealsdk.FindAll("WillowPopulationMaster")[-1]
        pawn = pop_master.SpawnPopulationControlledActor(ai_pawn_balance_def.AIPawnArchetype.Class,
                                                         None, "", _xyz, _rotation, ai_pawn_balance_def.AIPawnArchetype,
                                                         False, False)
        self.spawned_pawns.append(pawn)  # for cleanup on travel
        logging.logger.debug(f"AiPawnBalanceDefinition'{ai_pawn_obj_str}'\n->{bl2tools.get_obj_path_name(pawn)}")
        level = random.randint(*_level)
        # PopulationFactoryBalancedAIPawn 105-120:
        pawn.SetGameStage(level)
        pawn.SetExpLevel(level)
        pawn.SetGameStageForSpawnedInventory(level)
        pawn.SetAwesomeLevel(0)
        pawn.Controller.InitializeCharacterClass()
        pawn.Controller.RecalculateAttributeInitializedState()
        pawn.InitializeBalanceDefinitionState(ai_pawn_balance_def, -1)
        ai_pawn_balance_def.SetupPawnItemPoolList(pawn)
        pawn.AddDefaultInventory()
        # maybe change clan/Allegiance so it only aggros  at player

    def spawn_item_from_balance_definition(self, balance_definition: str, line: str, level: int) -> None:
        # get coordinates and optional level offset using regex
        m = re.search(self.xyz_pattern, line)
        _xyz = (float(m.group("x")), float(m.group("y")), float(m.group("z")))
        m = re.search(self.rot_pattern, line)
        _rotation = (int(m.group("pitch")), int(m.group("yaw")), int(m.group("roll")))
        m = re.search(self.lvl_pattern, line)
        if m:
            # clamp between 1 and max level possible
            pc = bl2tools.get_player_controller()
            if self.is_game_bl2:
                _max = pc.GetMaximumPossiblePlayerLevelCap() + pc.GetMaximumPossibleOverpowerModifier()
            else:
                _max = pc.GetMaxExpLevel()
            _level = (min(max(level + int(m.group("low")), 1), _max), min(max(level + int(m.group("high")), 1), _max))
        else:
            _level = (level, level)

        # get the WorldInfo object, then decide how to spawn the actual items
        world_info = unrealsdk.GetEngine().GetCurrentWorldInfo()
        obj_name = line.split(maxsplit=1)[0]

        def_data, inv_class = Spawner.get_item_def_data(balance_definition, obj_name, _level, True)
        item = world_info.Spawn(inv_class, None, "None", _xyz, _rotation, None, True)
        item.InitializeFromDefinitionData(def_data, None, True)
        pickup = item.GetPickup(False, True)
        pickup.AdjustPickupPhysicsAndCollisionForBeingAttached()
        pickup.Location = _xyz
        # pickup.RelativeRotation = _rotation
        pickup.Rotation = _rotation
        # pickup.SetSaveRotation(_rotation)
        logging.logger.debug(f"Spawned Item: {bl2tools.get_obj_path_name(pickup)}")

    def spawn_interactive_object(self, line: str, level: int) -> None:
        m = re.search(self.xyz_pattern, line)
        _loc: Tuple[float, float, float] = (float(m.group("x")), float(m.group("y")), float(m.group("z")))
        m = re.search(self.rot_pattern, line)
        _rotation: Tuple[int, int, int] = (int(m.group("pitch")), int(m.group("yaw")), int(m.group("roll")))
        m = re.search(self.lvl_pattern, line)
        pc: unrealsdk.UObject = bl2tools.get_player_controller()
        if m:
            # clamp between 1 and max level possible
            if self.is_game_bl2:
                _max: int = pc.GetMaximumPossiblePlayerLevelCap() + pc.GetMaximumPossibleOverpowerModifier()
            else:
                _max: int = pc.GetMaxExpLevel()
            _level = (min(max(level + int(m.group("low")), 1), _max), min(max(level + int(m.group("high")), 1), _max))
        else:
            _level = (level, level)

        obj_str: str = line.split(" ", 1)[0]
        io_definition: unrealsdk.UObject = unrealsdk.FindObject("Object", obj_str)

        pop_master: unrealsdk.UObject = unrealsdk.FindAll("WillowPopulationMaster")[-1]

        is_bal_def: bool = bl2tools.obj_is_in_class(io_definition, "InteractiveObjectBalanceDefinition")
        if is_bal_def:
            iobject: unrealsdk.UObject = pop_master.SpawnPopulationControlledActor(
                io_definition.DefaultInteractiveObject.InteractiveObjectClass, None, "", _loc, _rotation
            )
        else:
            iobject: unrealsdk.UObject = pop_master.SpawnPopulationControlledActor(
                io_definition.InteractiveObjectClass, None, "", _loc, _rotation
            )

        if pc.GetCurrentPlaythrough() != 2:
            will_pop = unrealsdk.FindAll("WillowPopulationOpportunityPoint")[1:]
            pop = unrealsdk.FindAll("PopulationOpportunityPoint")[1:]
            regions = pop if len(pop) > len(will_pop) else will_pop
            region_game_stage = max(pc.GetGameStageFromRegion(x.GameStageRegion)
                                    for x in regions if x.GameStageRegion)
        else:
            region_game_stage = max(x.GetGameStage() for x in unrealsdk.FindAll("WillowPlayerPawn") if x.Arms)

        iobject.SetGameStage(region_game_stage)
        iobject.SetExpLevel(region_game_stage)

        if is_bal_def:
            x = io_definition.SelectGradeIndex(region_game_stage, 0)
            iobject.InitializeBalanceDefinitionState(io_definition, x)
            io_definition.SetupInteractiveObjectLoot(iobject, x)
            iobject.InitializeFromDefinition(io_definition.DefaultInteractiveObject, False)

            if bl2tools.obj_is_in_class(iobject, "WillowVendingMachine"):
                vending_name = bl2tools.get_obj_path_name(iobject.InteractiveObjectDefinition).lower()
                markup = unrealsdk.FindObject("AttributeInitializationDefinition",
                                              "GD_Economy.VendingMachine.Init_MarkupCalc_P1")
                iobject.CommerceMarkup.InitializationDefinition = markup
                iobject.FeaturedItemCommerceMarkup.InitializationDefinition = markup
                iobject.InventoryConfigurationName = "Inventory"
                iobject.FeaturedItemConfigurationName = "FeaturedItem"
                item_stage = unrealsdk.FindObject("AttributeInitializationDefinition",
                                                  "GD_Population_Shopping.Balance.Init_FeaturedItem_GameStage")
                item_awesome = unrealsdk.FindObject("AttributeInitializationDefinition",
                                                    "GD_Population_Shopping.Balance.Init_FeaturedItem_AwesomeLevel")
                iobject.FeaturedItemGameStage.InitializationDefinition = item_stage
                iobject.FeaturedItemAwesomeLevel.InitializationDefinition = item_awesome
                if "health" in vending_name:
                    iobject.ShopType = 2
                elif "ammo" in vending_name:
                    iobject.ShopType = 1
                elif "weapon" in vending_name:
                    iobject.ShopType = 0

                iobject.ResetInventory()
        else:
            iobject.InitializeFromDefinition(io_definition, False)

    # noinspection PyPep8Naming
    @staticmethod
    def get_item_def_data(balance_definition: str, obj_path_name: str, level_range: Tuple[int, int],
                          b_need_inv_class: bool = False):

        obj: unrealsdk.UObject = unrealsdk.FindObject(balance_definition, obj_path_name)
        if balance_definition.lower() == "WeaponBalanceDefinition".lower():
            part_list = obj.RuntimePartListCollection
            WeaponTypeDefinition = part_list.AssociatedWeaponType
            BalanceDefinition = obj
            t = obj
            while t.BaseDefinition is not None:
                t = t.BaseDefinition
            InventoryDefinition = t.InventoryDefinition
            ManufacturerDefinition = t.Manufacturers[0].Manufacturer
            ManufacturerGradeIndex = random.randint(*level_range)

            BodyPartDefinition = bl2tools.choice([x.Part for x in part_list.BodyPartData.WeightedParts])
            GripPartDefinition = bl2tools.choice([x.Part for x in part_list.GripPartData.WeightedParts])
            BarrelPartDefinition = bl2tools.choice([x.Part for x in part_list.BarrelPartData.WeightedParts])
            SightPartDefinition = bl2tools.choice([x.Part for x in part_list.SightPartData.WeightedParts])
            StockPartDefinition = bl2tools.choice([x.Part for x in part_list.StockPartData.WeightedParts])
            ElementalPartDefinition = bl2tools.choice([x.Part for x in part_list.ElementalPartData.WeightedParts])
            Accessory1PartDefinition = bl2tools.choice([x.Part for x in part_list.Accessory1PartData.WeightedParts])
            Accessory2PartDefinition = bl2tools.choice([x.Part for x in part_list.Accessory2PartData.WeightedParts])
            MaterialPartDefinition = bl2tools.choice([x.Part for x in part_list.MaterialPartData.WeightedParts])
            PrefixPartDefinition = None
            TitlePartDefinition = None
            GameStage = ManufacturerGradeIndex
            UniqueId = -1
            def_data = (WeaponTypeDefinition, BalanceDefinition, ManufacturerDefinition, ManufacturerGradeIndex,
                        BodyPartDefinition, GripPartDefinition, BarrelPartDefinition, SightPartDefinition,
                        StockPartDefinition, ElementalPartDefinition, Accessory1PartDefinition,
                        Accessory2PartDefinition, MaterialPartDefinition, PrefixPartDefinition,
                        TitlePartDefinition, GameStage, UniqueId)
        elif balance_definition.lower() == "InventoryBalanceDefinition".lower():
            part_list = obj.PartListCollection
            ItemDefinition = obj.InventoryDefinition
            InventoryDefinition = ItemDefinition
            if bl2tools.obj_is_in_class(obj, "ClassModBalanceDefinition"):
                x = obj
                while not obj.ClassModDefinitions:
                    x = x.BaseDefinition
                InventoryDefinition = x.ClassModDefinitions[0]

            BalanceDefinition = obj
            ManufacturerDefinition = obj.Manufacturers[0].Manufacturer
            ManufacturerGradeIndex = random.randint(*level_range)
            if part_list is not None:
                AlphaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.AlphaPartData.WeightedParts])
                BetaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.BetaPartData.WeightedParts])
                GammaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.GammaPartData.WeightedParts])
                DeltaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.DeltaPartData.WeightedParts])
                EpsilonItemPartDefinition = bl2tools.choice([x.Part for x in part_list.EpsilonPartData.WeightedParts])
                ZetaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.ZetaPartData.WeightedParts])
                EtaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.EtaPartData.WeightedParts])
                ThetaItemPartDefinition = bl2tools.choice([x.Part for x in part_list.ThetaPartData.WeightedParts])
                MaterialItemPartDefinition = bl2tools.choice([x.Part for x in part_list.MaterialPartData.WeightedParts])
            else:
                AlphaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.AlphaParts.WeightedParts]
                ) if ItemDefinition.AlphaParts else None

                BetaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.BetaParts.WeightedParts]
                ) if ItemDefinition.BetaParts else None

                GammaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.GammaParts.WeightedParts]
                ) if ItemDefinition.GammaParts else None

                DeltaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.DeltaParts.WeightedParts]
                ) if ItemDefinition.DeltaParts else None

                EpsilonItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.EpsilonParts.WeightedParts]
                ) if ItemDefinition.EpsilonParts else None

                ZetaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.ZetaParts.WeightedParts]
                ) if ItemDefinition.ZetaParts else None

                EtaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.EtaParts.WeightedParts]
                ) if ItemDefinition.EtaParts else None

                ThetaItemPartDefinition = bl2tools.choice(
                    [x.Part for x in ItemDefinition.ThetaParts.WeightedParts]
                ) if ItemDefinition.ThetaParts else None

                MaterialItemPartDefinition = bl2tools.choice(
                    [x.Part for x in
                     ItemDefinition.MaterialParts.WeightedParts]
                ) if ItemDefinition.MaterialParts else None

            PrefixItemNamePartDefinition = None
            TitleItemNamePartDefinition = None
            GameStage = ManufacturerGradeIndex
            UniqueId = 42069
            def_data = (ItemDefinition, BalanceDefinition, ManufacturerDefinition,
                        ManufacturerGradeIndex, AlphaItemPartDefinition, BetaItemPartDefinition,
                        GammaItemPartDefinition, DeltaItemPartDefinition, EpsilonItemPartDefinition,
                        ZetaItemPartDefinition, EtaItemPartDefinition, ThetaItemPartDefinition,
                        MaterialItemPartDefinition, PrefixItemNamePartDefinition, TitleItemNamePartDefinition,
                        GameStage, UniqueId)

        else:
            raise ValueError

        if b_need_inv_class:
            return def_data, InventoryDefinition.InventoryClass
        return def_data
