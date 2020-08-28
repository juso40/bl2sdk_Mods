import unrealsdk
from unrealsdk import *

from . import logging

import json
import os


@logging.log_all_calls(logging.call_logger)
class PySave:

    def __init__(self, path):
        self.LOAD_PATH = None
        self.STASH_PATH = None
        self.stash_size = 6
        self.PATH = path
        self.b_load_json = False
        self.b_new_save = False
        self.b_apply_savedata = False

    def Enable(self):
        try:
            self.set_load_path(self.get_player_controller().
                               GetSaveGameNameFromid(self.get_player_controller().GetCachedSaveGame().SaveGameId))
        except Exception as e:
            logging.logger.info(e)
            logging.logger.info("No CachedSaveGame found!")

        def SaveGame_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.set_load_path(params.Filename)
            self.on_save_game(params)
            return True

        def BeginLoadGame_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.set_load_path(params.Filename)
            return True

        # It seems that ApplyItemSaveGameData() gets always called before ApplyWeaponSaveGameData().
        # I hope this is consistent
        def ApplyItem_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if self.b_apply_savedata or not self.check_load_json_is_valid() or self.b_new_save:
                return True
            return False

        def ApplyGun_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if self.b_apply_savedata or not self.check_load_json_is_valid() or self.b_new_save:
                self.b_new_save = False
                return True
            return False

        def OnSpawn_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            """Not needed anymore maybe"""
            if self.b_new_save:
                return True
            if params.bIsInitialSpawn or params.bIsClassChange:
                self.b_load_json = True
            return True

        def BankStoreWpn_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.save_bank(params.WWeapon.DefinitionData, True, caller)
            return True

        def BankStoreItm_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.save_bank(params.WItem.DefinitionData, False, caller)
            return True

        def BankOpen_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            return self.bank_on_open(caller)

        def BankClose_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            return self.bank_on_close(caller)

        def NewGame_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.b_load_json = False
            self.b_new_save = True
            logging.logger.info(f"bl2pysave b_new_save: {self.b_new_save}")
            return True

        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.SaveGame", "SaveGame_Hook", SaveGame_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.BeginLoadGame", "BeginLoadGame_Hook",
                               BeginLoadGame_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ApplyItemSaveGameData", "ApplyItem_Hook",
                               ApplyItem_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ApplyWeaponSaveGameData", "ApplyGun_Hook",
                               ApplyGun_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ShouldLoadSaveGameOnSpawn", "OnSpawn_Hook",
                               OnSpawn_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.PutWeapon", "BankStoreWeapon",
                               BankStoreWpn_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.PutItem", "BankStoreItem", BankStoreItm_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.Open", "BankOpen", BankOpen_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowInventoryStorage.Close", "BankCloe", BankClose_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowGlobals.GetDefaultPlayerSaveGame", "NewGame", NewGame_Hook)

    def Disable(self):
        pass

    def on_end_load(self):
        # We load our saves after the new materials got assigned or else the equipped gear wont have the right skin
        if self.b_load_json:
            logging.logger.debug(f"Will now try to load {self.LOAD_PATH}")
            self.compare_and_load()
            self.b_load_json = False
            if self.b_apply_savedata:
                self.b_apply_savedata = False

    def set_load_path(self, Filename):
        if not os.path.exists(os.path.join(self.PATH, "Saves")):
            logging.logger.debug(f"Could not find /Saves/ will now attempt to create it!")
            # if the "Saves/" folder does not exist, create it
            os.makedirs(os.path.join(self.PATH, "Saves"))
            logging.logger.debug(f"/Saves/ exists: {os.path.exists(os.path.join(self.PATH, 'Saves'))}")

        filename = Filename.split(".")[0]  # get the save name without its .sav extension
        if os.path.isfile(os.path.join(self.PATH, "Saves", f"{filename}.json")):
            # if the json save exist, set it as the loading path
            self.LOAD_PATH = os.path.join(self.PATH, "Saves", filename + ".json")
            self.b_new_save = False
        else:
            # else we need to create the json, mark it as new, so that the .sav items get loaded and wont be removed
            # because it now does exist, set it as the load path
            with open(os.path.join(self.PATH, "Saves", f"{filename}.json"), "w") as file:
                self.b_new_save = True
                self.LOAD_PATH = os.path.join(self.PATH, "Saves", filename + ".json")
                logging.logger.debug(f"Created 'Saves/{filename}.json'")

        if not os.path.isfile(os.path.join(self.PATH, "Saves", "STASH.json")):
            with open(os.path.join(self.PATH, "Saves", "STASH.json"), "w") as f:
                json.dump({"Weapons": [], "Items": []}, f, indent=2)
        self.STASH_PATH = os.path.join(self.PATH, "Saves", "STASH.json")

    def get_player_controller(self):
        return GetEngine().GamePlayers[0].Actor

    def get_full_name(self, obj):
        if obj is not None:
            return obj.PathName(obj)
        elif obj is None:
            return "None"

    def get_weapon_from_data(self, defdata):
        return {"WeaponTypeDefinition": self.get_full_name(defdata.WeaponTypeDefinition),
                "BalanceDefinition": self.get_full_name(defdata.BalanceDefinition),
                "ManufacturerDefinition": self.get_full_name(defdata.ManufacturerDefinition),
                "ManufacturerGradeIndex": defdata.ManufacturerGradeIndex,
                "BodyPartDefinition": self.get_full_name(defdata.BodyPartDefinition),
                "GripPartDefinition": self.get_full_name(defdata.GripPartDefinition),
                "BarrelPartDefinition": self.get_full_name(defdata.BarrelPartDefinition),
                "SightPartDefinition": self.get_full_name(defdata.SightPartDefinition),
                "StockPartDefinition": self.get_full_name(defdata.StockPartDefinition),
                "ElementalPartDefinition": self.get_full_name(defdata.ElementalPartDefinition),
                "Accessory1PartDefinition": self.get_full_name(defdata.Accessory1PartDefinition),
                "Accessory2PartDefinition": self.get_full_name(defdata.Accessory2PartDefinition),
                "MaterialPartDefinition": self.get_full_name(defdata.MaterialPartDefinition),
                "PrefixPartDefinition": self.get_full_name(defdata.PrefixPartDefinition),
                "TitlePartDefinition": self.get_full_name(defdata.TitlePartDefinition),
                "GameStage": defdata.GameStage,
                "UniqueId": defdata.UniqueId, }

    def get_item_from_data(self, defdata):
        return {"ItemDefinition": self.get_full_name(defdata.ItemDefinition),
                "BalanceDefinition": self.get_full_name(defdata.BalanceDefinition),
                "ManufacturerDefinition": self.get_full_name(defdata.ManufacturerDefinition),
                "ManufacturerGradeIndex": defdata.ManufacturerGradeIndex,
                "AlphaItemPartDefinition": self.get_full_name(defdata.AlphaItemPartDefinition),
                "BetaItemPartDefinition": self.get_full_name(defdata.BetaItemPartDefinition),
                "GammaItemPartDefinition": self.get_full_name(defdata.GammaItemPartDefinition),
                "DeltaItemPartDefinition": self.get_full_name(defdata.DeltaItemPartDefinition),
                "EpsilonItemPartDefinition": self.get_full_name(defdata.EpsilonItemPartDefinition),
                "ZetaItemPartDefinition": self.get_full_name(defdata.ZetaItemPartDefinition),
                "EtaItemPartDefinition": self.get_full_name(defdata.EtaItemPartDefinition),
                "ThetaItemPartDefinition": self.get_full_name(defdata.ThetaItemPartDefinition),
                "MaterialItemPartDefinition": self.get_full_name(defdata.MaterialItemPartDefinition),
                "PrefixItemNamePartDefinition": self.get_full_name(defdata.PrefixItemNamePartDefinition),
                "TitleItemNamePartDefinition": self.get_full_name(defdata.TitleItemNamePartDefinition),
                "GameStage": defdata.GameStage,
                "UniqueId": defdata.UniqueId, }

    def save_bank(self, def_data, is_wpn, caller):
        # We dont need to check for file existence because if you store an item to the bank you already had saved at
        # least once
        if caller.MaxSlots == 4:
            save_file = open(self.STASH_PATH, "r")
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
                dump["Weapons"].append(self.get_weapon_from_data(def_data))
            else:
                dump["Items"].append(self.get_item_from_data(def_data))
            save_json["Bank"] = dump
            json.dump(save_json, fp, indent=4)

    def save_backpack(self, fd, SaveGame, bank):  # we also need the bank to not overwrite it, we will append it again
        dump = {}
        inventory = []
        curr_equipped = []
        for WeaponSaveGameData in SaveGame.WeaponData:
            defdata = WeaponSaveGameData.WeaponDefinitionData
            if WeaponSaveGameData.Quickslot < 1:
                inventory.append(self.get_weapon_from_data(defdata))
            else:
                curr_equipped.append((WeaponSaveGameData.Quickslot, self.get_weapon_from_data(defdata)))
        curr_equipped.sort()
        dump["Wpn_Equipped"] = [x[1] for x in curr_equipped]
        dump["Weapons"] = inventory

        inventory = []
        curr_equipped = []
        for InventorySaveGameData in SaveGame.ItemData:
            defdata = InventorySaveGameData.DefinitionData
            if not InventorySaveGameData.bEquipped:
                inventory.append(self.get_item_from_data(defdata).copy())
            else:
                curr_equipped.append(self.get_item_from_data(defdata))
        dump["Itm_Equipped"] = curr_equipped
        dump["Items"] = inventory
        dump["Bank"] = bank
        json.dump(dump, fd, indent=4)
        logging.logger.debug(f"Successfully wrote to {fd}")

    def on_save_game(self, params):
        if self.get_player_controller() and self.get_player_controller().Pawn:
            read_f = open(self.LOAD_PATH, "r")
            try:  # This case only happens when the .json is completely empty, then it cant be decoded
                bank = json.load(read_f).get("Bank", dict())
            except:
                bank = dict()
            read_f.close()
            logging.logger.debug(f"Trying to write to {self.LOAD_PATH}")
            with open(self.LOAD_PATH, "w") as file:
                self.save_backpack(file, params.SaveGame, bank)

    def compare_and_load(self):
        inv_manager = self.get_player_controller().GetPawnInventoryManager()
        logging.logger.debug(f"Found InventoryManager as: {self.get_full_name(inv_manager) if inv_manager else None}")
        with open(self.LOAD_PATH, "r") as file:
            logging.logger.debug(f"Successfully opened file {self.LOAD_PATH}")
            try:
                json_save_file = json.load(file)
                for weapons in json_save_file["Weapons"]:
                    my_weap_def = tuple(value if isinstance(value, int)
                                        else FindObject("Object", value) for value in weapons.values())
                    # inv_manager.AddBackpackWeaponFromDefinitionData(my_weap_def)
                    inv_manager.ClientAddWeaponToBackpack(my_weap_def, 1, False)
                for slot, weapons in enumerate(json_save_file["Wpn_Equipped"]):
                    my_weap_def = tuple(value if isinstance(value, int)
                                        else FindObject("Object", value) for value in weapons.values())
                    inv_manager.AddBackpackWeaponFromDefinitionData(my_weap_def)
                    # inv_manager.ClientAddWeaponToBackpack(my_weap_def, 1, True)
                    # inv_manager.ServerReadyWeaponFromBackpack(my_weap_def, slot + 1, 1)

                for items in json_save_file["Items"]:
                    my_item_def = tuple(value if isinstance(value, int)
                                        else FindObject("Object", value) for value in items.values())
                    # inv_manager.AddBackpackItemFromDefinitionData(my_item_def)
                    inv_manager.ClientAddItemToBackpack(my_item_def, 1, 1, False)
                for items in json_save_file["Itm_Equipped"]:
                    my_item_def = tuple(value if isinstance(value, int)
                                        else FindObject("Object", value) for value in items.values())
                    inv_manager.AddBackpackItemFromDefinitionData(my_item_def)
                    # inv_manager.ClientAddItemToBackpack(my_item_def, 1, 1, True)
                logging.logger.debug(f"Successfully loaded the .json!")
            except Exception as e:
                logging.logger.debug(e)
                logging.logger.debug(f"{file} is empty or not a .json!")

    def bank_on_open(self, caller):
        if caller.MaxSlots == 4:
            caller.ChestSlots = self.stash_size
            # we opened the stash
            read_f = open(self.STASH_PATH, "r")
            bank = json.load(read_f)
        else:
            read_f = open(self.LOAD_PATH, "r")
            bank = json.load(read_f).get("Bank", dict())
        read_f.close()
        owner = self.get_player_controller().Pawn

        static_wweapon = unrealsdk.FindAll("WillowWeapon")[0]
        static_witem = unrealsdk.FindAll("WillowItem")[0]

        bank_things = []
        for weapon in bank.get("Weapons", list()):
            item_def = tuple(value if isinstance(value, int)
                             else FindObject("Object", value) for value in weapon.values())
            new_weapon = static_wweapon.CreateWeaponFromDef(item_def, owner, True)

            bank_things.append((new_weapon.Class, tuple(), new_weapon))

        for item in bank.get("Items", list()):
            item_def = tuple(value if isinstance(value, int)
                             else FindObject("Object", value) for value in item.values())
            new_item = static_witem.CreateItemFromDef(item_def, owner, 1, True)

            bank_things.append((new_item.Class, tuple(), new_item))
        caller.TheChest = bank_things
        caller.ChestIsOpen = True
        return False

    def bank_on_close(self, caller):
        if caller.MaxSlots == 4:
            read_f = open(self.STASH_PATH, "r")
            save_json = json.load(read_f)
        else:
            read_f = open(self.LOAD_PATH, "r")
            save_json = json.load(read_f)
        read_f.close()
        wweapon_class = unrealsdk.FindClass("WillowWeapon")

        bank = {"Weapons": list(), "Items": list()}
        for chest_data in caller.TheChest:
            if not chest_data.Inventory:
                break

            if chest_data.Inventory.Class == wweapon_class:
                bank["Weapons"].append(self.get_weapon_from_data(chest_data.Inventory.DefinitionData))
            else:
                bank["Items"].append(self.get_item_from_data(chest_data.Inventory.DefinitionData))
            chest_data.Inventory.Destroy()
            chest_data.Inventory = None

        self.get_player_controller().OnChestClosing(caller)
        caller.ChestIsOpen = False

        with open(self.LOAD_PATH if caller.MaxSlots != 4 else self.STASH_PATH, "w") as f:
            if caller.MaxSlots == 4:
                json.dump(bank, f, indent=4)
            else:
                save_json["Bank"] = bank
                json.dump(save_json, f, indent=4)
        return False

    def check_load_json_is_valid(self):
        if self.LOAD_PATH is None:
            return False
        with open(self.LOAD_PATH, "r") as file:
            try:
                json_save_file = json.load(file)
                logging.logger.debug(f"{self.LOAD_PATH} is valid JSON.")

                return True
            except Exception as e:
                # we could not load the json or work with it, so instead load the original .sav items
                logging.logger.error(e)
                self.b_new_save = True
                logging.logger.debug(f"{self.LOAD_PATH} is invalid JSON.")
                return False
