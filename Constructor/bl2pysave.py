import json
import os
from typing import Optional, TextIO, Union, Tuple

import unrealsdk
from unrealsdk import *

from . import bl2tools
from . import logging


def get_weapon_from_data(defdata: unrealsdk.FStruct, mark: int = 1) -> dict:
    return {"WeaponTypeDefinition": bl2tools.get_obj_path_name(defdata.WeaponTypeDefinition),
            "BalanceDefinition": bl2tools.get_obj_path_name(defdata.BalanceDefinition),
            "ManufacturerDefinition": bl2tools.get_obj_path_name(defdata.ManufacturerDefinition),
            "ManufacturerGradeIndex": defdata.ManufacturerGradeIndex,
            "BodyPartDefinition": bl2tools.get_obj_path_name(defdata.BodyPartDefinition),
            "GripPartDefinition": bl2tools.get_obj_path_name(defdata.GripPartDefinition),
            "BarrelPartDefinition": bl2tools.get_obj_path_name(defdata.BarrelPartDefinition),
            "SightPartDefinition": bl2tools.get_obj_path_name(defdata.SightPartDefinition),
            "StockPartDefinition": bl2tools.get_obj_path_name(defdata.StockPartDefinition),
            "ElementalPartDefinition": bl2tools.get_obj_path_name(defdata.ElementalPartDefinition),
            "Accessory1PartDefinition": bl2tools.get_obj_path_name(defdata.Accessory1PartDefinition),
            "Accessory2PartDefinition": bl2tools.get_obj_path_name(defdata.Accessory2PartDefinition),
            "MaterialPartDefinition": bl2tools.get_obj_path_name(defdata.MaterialPartDefinition),
            "PrefixPartDefinition": bl2tools.get_obj_path_name(defdata.PrefixPartDefinition),
            "TitlePartDefinition": bl2tools.get_obj_path_name(defdata.TitlePartDefinition),
            "GameStage": defdata.GameStage,
            "UniqueId": defdata.UniqueId,
            "Mark": mark}


def get_item_from_data(defdata: unrealsdk.FStruct, mark: int = 1) -> dict:
    return {"ItemDefinition": bl2tools.get_obj_path_name(defdata.ItemDefinition),
            "BalanceDefinition": bl2tools.get_obj_path_name(defdata.BalanceDefinition),
            "ManufacturerDefinition": bl2tools.get_obj_path_name(defdata.ManufacturerDefinition),
            "ManufacturerGradeIndex": defdata.ManufacturerGradeIndex,
            "AlphaItemPartDefinition": bl2tools.get_obj_path_name(defdata.AlphaItemPartDefinition),
            "BetaItemPartDefinition": bl2tools.get_obj_path_name(defdata.BetaItemPartDefinition),
            "GammaItemPartDefinition": bl2tools.get_obj_path_name(defdata.GammaItemPartDefinition),
            "DeltaItemPartDefinition": bl2tools.get_obj_path_name(defdata.DeltaItemPartDefinition),
            "EpsilonItemPartDefinition": bl2tools.get_obj_path_name(defdata.EpsilonItemPartDefinition),
            "ZetaItemPartDefinition": bl2tools.get_obj_path_name(defdata.ZetaItemPartDefinition),
            "EtaItemPartDefinition": bl2tools.get_obj_path_name(defdata.EtaItemPartDefinition),
            "ThetaItemPartDefinition": bl2tools.get_obj_path_name(defdata.ThetaItemPartDefinition),
            "MaterialItemPartDefinition": bl2tools.get_obj_path_name(defdata.MaterialItemPartDefinition),
            "PrefixItemNamePartDefinition": bl2tools.get_obj_path_name(defdata.PrefixItemNamePartDefinition),
            "TitleItemNamePartDefinition": bl2tools.get_obj_path_name(defdata.TitleItemNamePartDefinition),
            "GameStage": defdata.GameStage,
            "UniqueId": defdata.UniqueId,
            "Mark": mark}


def load_weapon_data(_json: dict) -> Tuple[Tuple, int]:
    return (unrealsdk.FindObject("Object", _json.get("WeaponTypeDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("BalanceDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("ManufacturerDefinition", "_")),
            _json.get("ManufacturerGradeIndex", 1),
            unrealsdk.FindObject("Object", _json.get("BodyPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("GripPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("BarrelPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("SightPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("StockPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("ElementalPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("Accessory1PartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("Accessory2PartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("MaterialPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("PrefixPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("TitlePartDefinition", "_")),
            _json.get("GameStage", 0),
            _json.get("UniqueId", -1),
            ), _json.get("Mark", 1)


def load_item_data(_json: dict) -> Tuple[Tuple, int]:
    return (unrealsdk.FindObject("Object", _json.get("ItemDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("BalanceDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("ManufacturerDefinition", "_")),
            _json.get("ManufacturerGradeIndex", 1),
            unrealsdk.FindObject("Object", _json.get("AlphaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("BetaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("GammaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("DeltaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("EpsilonItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("ZetaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("EtaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("ThetaItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("MaterialItemPartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("PrefixItemNamePartDefinition", "_")),
            unrealsdk.FindObject("Object", _json.get("TitleItemNamePartDefinition", "_")),
            _json.get("GameStage", 0),
            _json.get("UniqueId", -1),
            ), _json.get("Mark", 1)


# noinspection PyUnusedLocal
@logging.log_all_calls(logging.call_logger)
class PySave:

    def __init__(self, path: str):
        self.LOAD_PATH: Optional[os.PathLike] = None
        self.STASH_PATH: Optional[os.PathLike] = None
        self.stash_size: int = 6
        self.PATH: Union[str, os.PathLike] = path

    # noinspection PyPep8Naming
    def Enable(self) -> None:
        try:
            pc: unrealsdk.UObject = bl2tools.get_player_controller()
            self.set_load_path(pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId))
        except Exception as e:
            logging.logger.info(e)
            logging.logger.info("No CachedSaveGame found!")

        def hk_save_game(caller: unrealsdk.UObject,
                         function: unrealsdk.UFunction,
                         params: unrealsdk.FStruct) -> bool:
            self.set_load_path(params.Filename)
            self.on_save_game(params)
            return True

        def hk_begin_load(caller: unrealsdk.UObject,
                          function: unrealsdk.UFunction,
                          params: unrealsdk.FStruct) -> bool:
            self.set_load_path(params.Filename)
            return True

        # It seems that ApplyItemSaveGameData() gets always called before ApplyWeaponSaveGameData().
        # I hope this is consistent
        def hk_apply_items(caller: unrealsdk.UObject,
                           function: unrealsdk.UFunction,
                           params: unrealsdk.FStruct) -> bool:
            try:  # if an exception raises it's because of NewGame
                # noinspection PyShadowingNames
                pc: unrealsdk.UObject = bl2tools.get_player_controller()
                self.set_load_path(pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId))
                self.apply_save_game_data(params.SaveGame)
            except AttributeError:
                pass
            return True

        def hk_apply_weapons(caller: unrealsdk.UObject, function: unrealsdk.UFunction,
                             params: unrealsdk.FStruct) -> bool:
            return True

        def hk_bank_store_weapon(caller: unrealsdk.UObject,
                                 function: unrealsdk.UFunction,
                                 params: unrealsdk.FStruct) -> bool:
            self.save_bank(params.WWeapon, True, caller)
            return True

        def hk_bank_store_item(caller: unrealsdk.UObject,
                               function: unrealsdk.UFunction,
                               params: unrealsdk.FStruct) -> bool:
            self.save_bank(params.WItem, False, caller)
            return True

        def hk_bank_open(caller: unrealsdk.UObject,
                         function: unrealsdk.UFunction,
                         params: unrealsdk.FStruct) -> bool:
            return self.bank_on_open(caller)

        def hk_bank_close(caller: unrealsdk.UObject,
                          function: unrealsdk.UFunction,
                          params: unrealsdk.FStruct) -> bool:
            return self.bank_on_close(caller)

        def hk_load_pawn_data(caller: unrealsdk.UObject,
                              function: unrealsdk.UFunction,
                              params: unrealsdk.FStruct) -> bool:
            if bl2tools.get_world_info().GetStreamingPersistentMapName().lower() != "menumap":
                return True

            # noinspection PyShadowingNames
            pc: unrealsdk.UObject = bl2tools.get_player_controller()
            self.set_load_path(pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId))
            self.apply_save_game_data(params.Payload.SaveGame)
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerPawnDataManager.LoadPlayerPawnDataAsync",
                               "LoadPlayerPawnDataAsync_Hook", hk_load_pawn_data)

        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.SaveGame", "SaveGame_Hook", hk_save_game)
        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.BeginLoadGame", "BeginLoadGame_Hook",
                               hk_begin_load)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ApplyItemSaveGameData", "ApplyItem_Hook",
                               hk_apply_items)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ApplyWeaponSaveGameData", "ApplyGun_Hook",
                               hk_apply_weapons)

        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.PutWeapon", "BankStoreWeapon",
                               hk_bank_store_weapon)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.PutItem", "BankStoreItem", hk_bank_store_item)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.Open", "BankOpen", hk_bank_open)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.Close", "BankClose", hk_bank_close)

    def Disable(self) -> None:
        pass

    def set_load_path(self, filename: str) -> None:
        if not os.path.exists(os.path.join(self.PATH, "Saves")):
            logging.logger.debug(f"Could not find /Saves/ will now attempt to create it!")
            # if the "Saves/" folder does not exist, create it
            os.makedirs(os.path.join(self.PATH, "Saves"))
            logging.logger.debug(f"/Saves/ exists: {os.path.exists(os.path.join(self.PATH, 'Saves'))}")

        filename = filename.split(".")[0]  # get the save name without its .sav extension
        if os.path.isfile(os.path.join(self.PATH, "Saves", f"{filename}.json")):
            # if the json save exist, set it as the loading path
            self.LOAD_PATH = os.path.join(self.PATH, "Saves", filename + ".json")
        else:
            # else we need to create the json, mark it as new, so that the .sav items get loaded and won't be removed
            # because it now does exist, set it as the load path
            with open(os.path.join(self.PATH, "Saves", f"{filename}.json"), "w") as _:
                self.LOAD_PATH = os.path.join(self.PATH, "Saves", f"{filename}.json")
                logging.logger.debug(f"Created 'Saves/{filename}.json'")

        if not os.path.isfile(os.path.join(self.PATH, "Saves", "STASH.json")):
            with open(os.path.join(self.PATH, "Saves", "STASH.json"), "w") as f:
                json.dump({"Weapons": [], "Items": []}, f, indent=2)
        self.STASH_PATH = os.path.join(self.PATH, "Saves", "STASH.json")

    def save_bank(self, item: unrealsdk.UObject, is_wpn: bool, caller: unrealsdk.UObject) -> None:
        # We don't need to check for file existence because if you store an item to the bank you already had saved
        # at least once
        if caller.MaxSlots == 4:
            save_file = open(self.STASH_PATH, "r")
        elif caller.MaxSlots == 3:  # tps grinder
            return
        else:
            save_file = open(self.LOAD_PATH, "r")
        save_json = json.load(save_file)
        save_file.close()

        if caller.MaxSlots == 4:
            # actually the stash
            save_bank = save_json
        else:
            save_bank = save_json.get("Bank", list())

        with open(self.LOAD_PATH if caller.MaxSlots != 4 else self.STASH_PATH, "w") as fp:
            dump = {"Weapons": save_bank.get("Weapons", list()), "Items": save_bank.get("Items", list())}

            if is_wpn:
                dump["Weapons"].append(get_weapon_from_data(item.DefinitionData, item.Mark))
            else:
                dump["Items"].append(get_item_from_data(item.DefinitionData, item.Mark))
            save_json["Bank"] = dump
            json.dump(save_json, fp, indent=4)

    # noinspection PyMethodMayBeStatic
    def save_backpack(self, fd: TextIO, save_game: unrealsdk.UObject, bank: dict) -> None:
        # we also need the bank to not overwrite it, we will append it again
        dump = {}
        inventory = []
        curr_equipped = []
        for WeaponSaveGameData in save_game.WeaponData:  # type: unrealsdk.FStruct
            defdata: unrealsdk.FStruct = WeaponSaveGameData.WeaponDefinitionData
            mark: int = WeaponSaveGameData.Mark
            if WeaponSaveGameData.Quickslot < 1:
                inventory.append(get_weapon_from_data(defdata, mark=mark))
            else:
                curr_equipped.append((WeaponSaveGameData.Quickslot, get_weapon_from_data(defdata, mark=mark)))

        curr_equipped.sort()
        dump["Wpn_Equipped"] = [x[1] for x in curr_equipped]
        dump["Weapons"] = inventory

        inventory = []
        curr_equipped = []
        for InventorySaveGameData in save_game.ItemData:  # type: unrealsdk.FStruct
            defdata: unrealsdk.FStruct = InventorySaveGameData.DefinitionData
            mark: int = InventorySaveGameData.Mark
            if not InventorySaveGameData.bEquipped:
                inventory.append(get_item_from_data(defdata, mark=mark))
            else:
                curr_equipped.append(get_item_from_data(defdata, mark=mark))
        dump["Itm_Equipped"] = curr_equipped
        dump["Items"] = inventory
        dump["Bank"] = bank
        json.dump(dump, fd, indent=4)
        logging.logger.debug(f"Successfully wrote to {fd}")

    def on_save_game(self, params: unrealsdk.FStruct) -> None:
        if bl2tools.get_player_controller() and bl2tools.get_player_controller().Pawn:
            read_f = open(self.LOAD_PATH, "r")
            try:  # This case only happens when the .json is completely empty, then it can't be decoded
                bank = json.load(read_f).get("Bank", dict())
            except json.JSONDecodeError:
                bank = dict()
            read_f.close()
            logging.logger.debug(f"Trying to write to {self.LOAD_PATH}")
            with open(self.LOAD_PATH, "w") as file:
                self.save_backpack(file, params.SaveGame, bank)

    def apply_save_game_data(self, save_game: unrealsdk.UObject) -> None:
        weapon_data = []
        item_data = []

        with open(self.LOAD_PATH, "r") as file:
            logging.logger.debug(f"Successfully opened file {self.LOAD_PATH}")
            try:
                json_save_file = json.load(file)

                for slot, weapons in enumerate(json_save_file["Wpn_Equipped"]):
                    my_weap_def, mark = load_weapon_data(weapons)
                    weapon_data.append((my_weap_def, 1 + slot, mark))

                for weapons in json_save_file["Weapons"]:
                    my_weap_def, mark = load_weapon_data(weapons)
                    weapon_data.append((my_weap_def, 0, mark))

                for items in json_save_file["Itm_Equipped"]:
                    my_item_def, mark = load_item_data(items)
                    item_data.append((my_item_def, 1, True, mark))

                for items in json_save_file["Items"]:
                    my_item_def, mark = load_item_data(items)
                    item_data.append((my_item_def, 1, False, mark))

                save_game.WeaponData = weapon_data
                save_game.ItemData = item_data
                logging.logger.debug(f"Successfully loaded the .json!")
            except Exception as e:
                logging.logger.debug(e)
                logging.logger.debug(f"{file} is empty or not a .json!")

    def bank_on_open(self, caller: unrealsdk.UObject) -> bool:
        if caller.MaxSlots == 4:
            caller.ChestSlots = self.stash_size
            # we opened the stash
            read_f = open(self.STASH_PATH, "r")
            bank = json.load(read_f)
        elif caller.MaxSlots == 3:  # the grinder in TPS
            return True
        else:
            read_f = open(self.LOAD_PATH, "r")
            bank = json.load(read_f).get("Bank", dict())
        read_f.close()
        owner = bl2tools.get_player_controller().Pawn

        static_wweapon: unrealsdk.UObject = unrealsdk.FindAll("WillowWeapon")[0]
        static_witem: unrealsdk.UObject = unrealsdk.FindAll("WillowItem")[0]

        bank_things: list = []
        for weapon in bank.get("Weapons", list()):
            wpn_data, mark = load_weapon_data(weapon)
            new_weapon: unrealsdk.UObject = static_wweapon.CreateWeaponFromDef(wpn_data, owner, True)
            new_weapon.Mark = mark

            bank_things.append((new_weapon.Class, tuple(), new_weapon))

        for item in bank.get("Items", list()):
            item_data, mark = load_item_data(item)
            new_item: unrealsdk.UObject = static_witem.CreateItemFromDef(item_data, owner, 1, True)
            new_item.Mark = mark

            bank_things.append((new_item.Class, tuple(), new_item))

        caller.TheChest = bank_things
        caller.ChestIsOpen = True
        return False

    def bank_on_close(self, caller: unrealsdk.UObject) -> bool:
        if caller.MaxSlots == 4:
            read_f = open(self.STASH_PATH, "r")
            save_json = json.load(read_f)
        elif caller.MaxSlots == 3:  # the grinder in TPS
            return True
        else:
            read_f = open(self.LOAD_PATH, "r")
            save_json = json.load(read_f)
        read_f.close()
        wweapon_class = unrealsdk.FindClass("WillowWeapon")

        bank = {"Weapons": list(), "Items": list()}
        for chest_data in caller.TheChest:
            if not chest_data.Inventory:
                break

            mark: int = chest_data.Inventory.Mark
            if chest_data.Inventory.Class == wweapon_class:
                bank["Weapons"].append(get_weapon_from_data(chest_data.Inventory.DefinitionData, mark=mark))
            else:
                bank["Items"].append(get_item_from_data(chest_data.Inventory.DefinitionData, mark=mark))
            chest_data.Inventory.Destroy()
            chest_data.Inventory = None

        bl2tools.get_player_controller().OnChestClosing(caller)
        caller.ChestIsOpen = False

        with open(self.LOAD_PATH if caller.MaxSlots != 4 else self.STASH_PATH, "w") as f:
            if caller.MaxSlots == 4:
                json.dump(bank, f, indent=4)
            else:
                save_json["Bank"] = bank
                json.dump(save_json, f, indent=4)
        return False

    def check_load_json_is_valid(self) -> bool:
        if self.LOAD_PATH is None:
            return False
        with open(self.LOAD_PATH, "r") as file:
            try:
                _ = json.load(file)
                logging.logger.debug(f"{self.LOAD_PATH} is valid JSON.")

                return True
            except Exception as e:
                # we could not load the json or work with it, so instead load the original .sav items
                logging.logger.error(e)
                logging.logger.debug(f"{self.LOAD_PATH} is invalid JSON.")
                return False
