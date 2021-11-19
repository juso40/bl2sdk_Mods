from typing import Optional, Sequence, List

import unrealsdk

from . import bl2tools
from . import inventory
from ..ModMenu import *

from .. import PyImgui
from ..PyImgui import pyd_imgui


IMGUI_SHOW: bool = False
def _toggle() -> None:
    global IMGUI_SHOW
    IMGUI_SHOW = PyImgui.toggle_gui()
    if PyImgui.toggle_cursor():
        inventory.update_inventory()


class InventoryEditor(SDKMod):
    Name: str = "Inventory Editor"
    Author: str = "Juso"
    Description: str = "Allows you to edit/add/remove items in your Inventory while ingame."
    Version: str = "1.3.1"

    Types: ModTypes = ModTypes.Utility
    Priority: int = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.NotSaved

    Status: str = "Disabled"

    def __init__(self):
        self.Options: Sequence[Options.Base] = []
        self.Keybinds: Sequence[Keybind] = [Keybind("Open Editor", "F1", OnPress=_toggle)]

    def Enable(self) -> None:
        PyImgui.subscribe_end_scene(self.end_scene)

    def Disable(self) -> None:
        PyImgui.unsubscribe_end_scene(self.end_scene)

    backpack_index: int = -1

    b_update_helper: bool = False

    u_class_index: int = 0
    u_classes: List[str] = ["WillowWeapon",
                            "WillowShield",
                            "WillowUsableItem",
                            "WillowArtifact",
                            "WillowClassMod",
                            "WillowGrenadeMod",
                            "WillowMissionItem",
                            "WillowUsableCustomizationItem",
                            ]

    def end_scene(self) -> None:
        if not IMGUI_SHOW:
            return

        pyd_imgui.begin("Inventory Editor")

        _, self.u_class_index = pyd_imgui.combo("Add Class", self.u_class_index, self.u_classes)
        if _:
            self.edit_obj = None

        # noinspection PyArgumentList
        if pyd_imgui.button("Add New"):
            pc: unrealsdk.UObject = bl2tools.get_player_controller()
            new_uclass: str = self.u_classes[self.u_class_index]
            if new_uclass == "WillowWeapon":
                pc.GetPawnInventoryManager().ClientAddWeaponToBackpack((), 1, False)
            else:
                new_item: unrealsdk.UObject = pc.Spawn(unrealsdk.FindClass(new_uclass))
                new_item.Quantity = 1
                pc.GetPawnInventoryManager().AddInventoryToBackpack(new_item)

            inventory.update_inventory()

        pyd_imgui.separator()

        pyd_imgui.text(f"Backpack")
        _, self.backpack_index = pyd_imgui.list_box_stretch("##backpack",
                                                            self.backpack_index,
                                                            inventory.player_inventory_readable)
        if _:
            self.b_update_helper = True
        pyd_imgui.end()

        if not inventory.player_inventory:
            return
        try:
            self.edit_obj = inventory.player_inventory[self.backpack_index]
        except IndexError:
            # in case the user removed too many objects from his inventory we might run into this exception
            # so let's just reset his backpack index to -1
            self.backpack_index = len(inventory.player_inventory) - 1
            self.edit_obj = inventory.player_inventory[self.backpack_index]
            self.b_update_helper = True

        if not self.edit_obj:
            return

        self.edit_helper()

    edit_obj: Optional[unrealsdk.UObject] = None

    def edit_helper(self) -> None:
        pyd_imgui.begin("Helper")

        if bl2tools.obj_is_in_class(self.edit_obj, "WillowWeapon"):
            self.weapon_part_selector()
        else:
            self.item_part_selector()

        pyd_imgui.end()

    def weapon_part_selector(self) -> None:
        if self.b_update_helper:
            self.b_update_helper = False
            inventory.weapon_helper.update(self.edit_obj)

        pyd_imgui.text(str(self.edit_obj.Class))
        pyd_imgui.separator()

        if pyd_imgui.button("Refresh Title"):
            self.edit_obj.DefinitionData.TitlePartDefinition = None
            self.edit_obj.DefinitionData.PrefixPartDefinition = None
            self.edit_obj.InitializeInternal(True)
            inventory.update_inventory()

        wtd_i: int
        wtd_l: List[str]
        wtd_i, wtd_l = inventory.weapon_data["WeaponTypeDefinition"]
        new_wtd: bool
        new_wtd, wtd_i = pyd_imgui.combo("WeaponTypeDefinition", wtd_i, wtd_l)
        if new_wtd:
            inventory.weapon_data["WeaponTypeDefinition"][0] = wtd_i
            self.edit_obj.DefinitionData.WeaponTypeDefinition = unrealsdk.FindObject("Object", wtd_l[wtd_i])
            inventory.weapon_helper.update(self.edit_obj)

        bd_i: int
        bd_l: List[str]
        bd_i, bd_l = inventory.weapon_data["BalanceDefinition"]
        new_bd: bool
        new_bd, bd_i = pyd_imgui.combo("BalanceDefinition", bd_i, bd_l)
        if new_bd:
            inventory.weapon_data["BalanceDefinition"][0] = bd_i
            self.edit_obj.DefinitionData.BalanceDefinition = unrealsdk.FindObject("Object", bd_l[bd_i])
            inventory.weapon_helper.update(self.edit_obj)

        man_i: int
        man_l: List[str]
        man_i, man_l = inventory.weapon_data["ManufacturerDefinition"]
        new_man: bool
        new_man, man_i = pyd_imgui.combo("ManufacturerDefinition", man_i, man_l)
        if new_man:
            inventory.weapon_data["ManufacturerDefinition"][0] = man_i
            self.edit_obj.DefinitionData.ManufacturerDefinition = unrealsdk.FindObject("Object", man_l[man_i])

        man_grade: int = inventory.weapon_data["ManufacturerGradeIndex"]
        new_grade: bool
        new_grade, man_grade = pyd_imgui.slider_int("ManufacturerGradeIndex", man_grade, 0, 90)
        if new_grade:
            inventory.weapon_data["ManufacturerGradeIndex"] = man_grade
            self.edit_obj.DefinitionData.ManufacturerGradeIndex = man_grade

        body_i: int
        body_l: List[str]
        body_i, body_l = inventory.weapon_data["BodyPartDefinition"]
        new_body: bool
        new_body, body_i = pyd_imgui.combo("BodyPartDefinition", body_i, body_l)
        if new_body:
            inventory.weapon_data["BodyPartDefinition"][0] = body_i
            self.edit_obj.DefinitionData.BodyPartDefinition = unrealsdk.FindObject("Object", body_l[body_i])

        grip_i: int
        grip_l: List[str]
        grip_i, grip_l = inventory.weapon_data["GripPartDefinition"]
        new_grip: bool
        new_grip, grip_i = pyd_imgui.combo("GripPartDefinition", grip_i, grip_l)
        if new_grip:
            inventory.weapon_data["GripPartDefinition"][0] = grip_i
            self.edit_obj.DefinitionData.GripPartDefinition = unrealsdk.FindObject("Object", grip_l[grip_i])

        barrel_i: int
        barrel_l: List[str]
        barrel_i, barrel_l = inventory.weapon_data["BarrelPartDefinition"]
        new_barrel: bool
        new_barrel, barrel_i = pyd_imgui.combo("BarrelPartDefinition", barrel_i, barrel_l)
        if new_barrel:
            inventory.weapon_data["BarrelPartDefinition"][0] = barrel_i
            self.edit_obj.DefinitionData.BarrelPartDefinition = unrealsdk.FindObject("Object", barrel_l[barrel_i])

        sight_i: int
        sight_l: List[str]
        sight_i, sight_l = inventory.weapon_data["SightPartDefinition"]
        new_sight: bool
        new_sight, sight_i = pyd_imgui.combo("SightPartDefinition", sight_i, sight_l)
        if new_sight:
            inventory.weapon_data["SightPartDefinition"][0] = sight_i
            self.edit_obj.DefinitionData.SightPartDefinition = unrealsdk.FindObject("Object", sight_l[sight_i])

        stock_i: int
        stock_l: List[str]
        stock_i, stock_l = inventory.weapon_data["StockPartDefinition"]
        new_stock: bool
        new_stock, stock_i = pyd_imgui.combo("StockPartDefinition", stock_i, stock_l)
        if new_stock:
            inventory.weapon_data["StockPartDefinition"][0] = stock_i
            self.edit_obj.DefinitionData.StockPartDefinition = unrealsdk.FindObject("Object", stock_l[stock_i])

        elem_i: int
        elem_l: List[str]
        elem_i, elem_l = inventory.weapon_data["ElementalPartDefinition"]
        new_elem: bool
        new_elem, elem_i = pyd_imgui.combo("ElementalPartDefinition", elem_i, elem_l)
        if new_elem:
            inventory.weapon_data["ElementalPartDefinition"][0] = elem_i
            self.edit_obj.DefinitionData.ElementalPartDefinition = unrealsdk.FindObject("Object", elem_l[elem_i])

        acc1_i: int
        acc1_l: List[str]
        acc1_i, acc1_l = inventory.weapon_data["Accessory1PartDefinition"]
        new_acc1: bool
        new_acc1, acc1_i = pyd_imgui.combo("Accessory1PartDefinition", acc1_i, acc1_l)
        if new_acc1:
            inventory.weapon_data["Accessory1PartDefinition"][0] = acc1_i
            self.edit_obj.DefinitionData.Accessory1PartDefinition = unrealsdk.FindObject("Object", acc1_l[acc1_i])

        acc2_i: int
        acc2_l: List[str]
        acc2_i, acc2_l = inventory.weapon_data["Accessory2PartDefinition"]
        new_acc2: bool
        new_acc2, acc2_i = pyd_imgui.combo("Accessory2PartDefinition", acc2_i, acc2_l)
        if new_acc2:
            inventory.weapon_data["Accessory2PartDefinition"][0] = acc2_i
            self.edit_obj.DefinitionData.Accessory2PartDefinition = unrealsdk.FindObject("Object", acc2_l[acc2_i])

        mat_i: int
        mat_l: List[str]
        mat_i, mat_l = inventory.weapon_data["MaterialPartDefinition"]
        new_mat: bool
        new_mat, mat_i = pyd_imgui.combo("MaterialPartDefinition", mat_i, mat_l)
        if new_mat:
            inventory.weapon_data["MaterialPartDefinition"][0] = mat_i
            self.edit_obj.DefinitionData.MaterialPartDefinition = unrealsdk.FindObject("Object", mat_l[mat_i])

        stage: int = inventory.weapon_data["GameStage"]
        new_stage: bool
        new_stage, stage = pyd_imgui.slider_int("GameStage", stage, 0, 90)
        if new_stage:
            inventory.weapon_data["GameStage"] = stage
            self.edit_obj.DefinitionData.GameStage = stage

    def item_part_selector(self) -> None:
        if self.b_update_helper:
            self.b_update_helper = False
            inventory.item_helper.update(self.edit_obj)

        pyd_imgui.text(str(self.edit_obj.Class))
        pyd_imgui.separator()

        if pyd_imgui.button("Refresh Title"):
            self.edit_obj.DefinitionData.TitleItemNamePartDefinition = None
            self.edit_obj.DefinitionData.PrefixItemNamePartDefinition = None
            self.edit_obj.InitializeInternal(True)
            inventory.update_inventory()

        itm_def_i: int
        item_def_l: List[str]
        itm_def_i, item_def_l = inventory.item_data["ItemDefinition"]
        new_itm_def: bool
        new_itm_def, itm_def_i = pyd_imgui.combo("ItemDefinition", itm_def_i, item_def_l)
        if new_itm_def:
            inventory.item_data["ItemDefinition"][0] = itm_def_i
            self.edit_obj.DefinitionData.ItemDefinition = unrealsdk.FindObject("Object", item_def_l[itm_def_i])
            inventory.item_helper.update(self.edit_obj)

        bd_i: int
        bd_l: List[str]
        bd_i, bd_l = inventory.item_data["BalanceDefinition"]
        new_bd: bool
        new_bd, bd_i = pyd_imgui.combo("BalanceDefinition", bd_i, bd_l)
        if new_bd:
            inventory.item_data["BalanceDefinition"][0] = bd_i
            self.edit_obj.DefinitionData.BalanceDefinition = unrealsdk.FindObject("Object", bd_l[bd_i])
            inventory.item_helper.update(self.edit_obj)

        man_i: int
        man_l: List[str]
        man_i, man_l = inventory.item_data["ManufacturerDefinition"]
        new_man: bool
        new_man, man_i = pyd_imgui.combo("ManufacturerDefinition", man_i, man_l)
        if new_man:
            inventory.item_data["ManufacturerDefinition"][0] = man_i
            self.edit_obj.DefinitionData.ManufacturerDefinition = unrealsdk.FindObject("Object", man_l[man_i])

        man_grade: int = inventory.item_data["ManufacturerGradeIndex"]
        new_grade: bool
        new_grade, man_grade = pyd_imgui.slider_int("ManufacturerGradeIndex", man_grade, 0, 90)
        if new_grade:
            inventory.item_data["ManufacturerGradeIndex"] = man_grade
            self.edit_obj.DefinitionData.ManufacturerGradeIndex = man_grade

        alpha_i: int
        alpha_l: List[str]
        alpha_i, alpha_l = inventory.item_data["AlphaItemPartDefinition"]
        new_alpha: bool
        new_alpha, alpha_i = pyd_imgui.combo("AlphaItemPartDefinition", alpha_i, alpha_l)
        if new_alpha:
            inventory.item_data["AlphaItemPartDefinition"][0] = alpha_i
            self.edit_obj.DefinitionData.AlphaItemPartDefinition = unrealsdk.FindObject("Object", alpha_l[alpha_i])

        beta_i: int
        beta_l: List[str]
        beta_i, beta_l = inventory.item_data["BetaItemPartDefinition"]
        new_beta: bool
        new_beta, beta_i = pyd_imgui.combo("BetaItemPartDefinition", beta_i, beta_l)
        if new_beta:
            inventory.item_data["BetaItemPartDefinition"][0] = beta_i
            self.edit_obj.DefinitionData.BetaItemPartDefinition = unrealsdk.FindObject("Object", beta_l[beta_i])

        gamma_i: int
        gamma_l: List[str]
        gamma_i, gamma_l = inventory.item_data["GammaItemPartDefinition"]
        new_gamma: bool
        new_gamma, gamma_i = pyd_imgui.combo("GammaItemPartDefinition", gamma_i, gamma_l)
        if new_gamma:
            inventory.item_data["GammaItemPartDefinition"][0] = gamma_i
            self.edit_obj.DefinitionData.GammaItemPartDefinition = unrealsdk.FindObject("Object", gamma_l[gamma_i])

        delta_i: int
        delta_l: List[str]
        delta_i, delta_l = inventory.item_data["DeltaItemPartDefinition"]
        new_delta: bool
        new_delta, delta_i = pyd_imgui.combo("DeltaItemPartDefinition", delta_i, delta_l)
        if new_delta:
            inventory.item_data["DeltaItemPartDefinition"][0] = delta_i
            self.edit_obj.DefinitionData.DeltaItemPartDefinition = unrealsdk.FindObject("Object", delta_l[delta_i])

        eps_i: int
        eps_l: List[str]
        eps_i, eps_l = inventory.item_data["EpsilonItemPartDefinition"]
        new_eps: bool
        new_eps, eps_i = pyd_imgui.combo("EpsilonItemPartDefinition", eps_i, eps_l)
        if new_eps:
            inventory.item_data["EpsilonItemPartDefinition"][0] = eps_i
            self.edit_obj.DefinitionData.EpsilonItemPartDefinition = unrealsdk.FindObject("Object", eps_l[eps_i])

        zeta_i: int
        zeta_l: List[str]
        zeta_i, zeta_l = inventory.item_data["ZetaItemPartDefinition"]
        new_zeta: bool
        new_zeta, zeta_i = pyd_imgui.combo("ZetaItemPartDefinition", zeta_i, zeta_l)
        if new_zeta:
            inventory.item_data["ZetaItemPartDefinition"][0] = zeta_i
            self.edit_obj.DefinitionData.ZetaItemPartDefinition = unrealsdk.FindObject("Object", zeta_l[zeta_i])

        eta_i: int
        eta_l: List[str]
        eta_i, eta_l = inventory.item_data["EtaItemPartDefinition"]
        new_eta: bool
        new_eta, eta_i = pyd_imgui.combo("EtaItemPartDefinition", eta_i, eta_l)
        if new_eta:
            inventory.item_data["EtaItemPartDefinition"][0] = eta_i
            self.edit_obj.DefinitionData.EtaItemPartDefinition = unrealsdk.FindObject("Object", eta_l[eta_i])

        theta_i: int
        theta_l: List[str]
        theta_i, theta_l = inventory.item_data["ThetaItemPartDefinition"]
        new_theta: bool
        new_theta, theta_i = pyd_imgui.combo("ThetaItemPartDefinition", theta_i, theta_l)
        if new_theta:
            inventory.item_data["ThetaItemPartDefinition"][0] = theta_i
            self.edit_obj.DefinitionData.ThetaItemPartDefinition = unrealsdk.FindObject("Object", theta_l[theta_i])

        mat_i: int
        mat_l: List[str]
        mat_i, mat_l = inventory.item_data["MaterialItemPartDefinition"]
        new_mat: bool
        new_mat, mat_i = pyd_imgui.combo("MaterialItemPartDefinition", mat_i, mat_l)
        if new_mat:
            inventory.item_data["MaterialItemPartDefinition"][0] = mat_i
            self.edit_obj.DefinitionData.MaterialItemPartDefinition = unrealsdk.FindObject("Object", mat_l[mat_i])

        stage: int = inventory.item_data["GameStage"]
        new_stage: bool
        new_stage, stage = pyd_imgui.slider_int("GameStage", stage, 0, 90)
        if new_stage:
            inventory.item_data["GameStage"] = stage
            self.edit_obj.DefinitionData.GameStage = stage


RegisterMod(InventoryEditor())
