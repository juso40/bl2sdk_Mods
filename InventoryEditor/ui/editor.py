from functools import lru_cache
from typing import List, Tuple, cast

import imgui
import unrealsdk  # type: ignore

from Mods.InventoryEditor.backpack import ItemData, WeaponData, player_inventory

from .components import combo_with_title


def part_changed(part_name: str, value: unrealsdk.UObject) -> None:
    player_inventory.on_part_changed(part_name, value)


@lru_cache(maxsize=32)
def readable_list(items: Tuple[unrealsdk.UObject]) -> List[str]:
    return [part.PathName(part) if part else "None" for part in items]


def parts_combo(
    part_name: str, current: int, parts_uobject: Tuple[unrealsdk.UObject]
) -> int:
    changed: bool
    changed, index = combo_with_title(
        title=part_name,
        current=current,
        items=readable_list(parts_uobject),
        spacing=True,
    )
    if changed:
        part_changed(part_name, parts_uobject[index])

    return index


def game_stage_slider(attr: str, value: int) -> int:
    changed: bool
    imgui.spacing()
    imgui.text(f"{attr}:")
    imgui.push_item_width(-1)
    changed, value = imgui.slider_int(f"##{attr}", value, 1, 90)
    if changed:
        setattr(player_inventory.item.DefinitionData, attr, value)
    imgui.pop_item_width()
    return value


def draw() -> None:
    """Draws the Editor Content in the current Child region."""
    if not player_inventory.item:
        return

    if player_inventory.item.Class.Name == "WillowWeapon":
        draw_weapon_editor()
    else:
        draw_item_editor()


def draw_weapon_editor() -> None:
    weapon_data: WeaponData = cast(WeaponData, player_inventory.item_data)

    weapon_data.WeaponTypeDefinition_Index = parts_combo(
        "WeaponTypeDefinition",
        weapon_data.WeaponTypeDefinition_Index,
        weapon_data.WeaponTypeDefinition,
    )

    weapon_data.BalanceDefinition_Index = parts_combo(
        "BalanceDefinition",
        weapon_data.BalanceDefinition_Index,
        weapon_data.BalanceDefinition,
    )

    weapon_data.ManufacturerDefinition_Index = parts_combo(
        "ManufacturerDefinition",
        weapon_data.ManufacturerDefinition_Index,
        weapon_data.ManufacturerDefinition,
    )

    weapon_data.ManufacturerGradeIndex = game_stage_slider(
        "ManufacturerGradeIndex", weapon_data.ManufacturerGradeIndex
    )

    weapon_data.BodyPartDefinition_Index = parts_combo(
        "BodyPartDefinition",
        weapon_data.BodyPartDefinition_Index,
        weapon_data.BodyPartDefinition,
    )

    weapon_data.GripPartDefinition_Index = parts_combo(
        "GripPartDefinition",
        weapon_data.GripPartDefinition_Index,
        weapon_data.GripPartDefinition,
    )

    weapon_data.BarrelPartDefinition_Index = parts_combo(
        "BarrelPartDefinition",
        weapon_data.BarrelPartDefinition_Index,
        weapon_data.BarrelPartDefinition,
    )

    weapon_data.SightPartDefinition_Index = parts_combo(
        "SightPartDefinition",
        weapon_data.SightPartDefinition_Index,
        weapon_data.SightPartDefinition,
    )

    weapon_data.StockPartDefinition_Index = parts_combo(
        "StockPartDefinition",
        weapon_data.StockPartDefinition_Index,
        weapon_data.StockPartDefinition,
    )

    weapon_data.ElementalPartDefinition_Index = parts_combo(
        "ElementalPartDefinition",
        weapon_data.ElementalPartDefinition_Index,
        weapon_data.ElementalPartDefinition,
    )

    weapon_data.Accessory1PartDefinition_Index = parts_combo(
        "Accessory1PartDefinition",
        weapon_data.Accessory1PartDefinition_Index,
        weapon_data.Accessory1PartDefinition,
    )

    weapon_data.Accessory2PartDefinition_Index = parts_combo(
        "Accessory2PartDefinition",
        weapon_data.Accessory2PartDefinition_Index,
        weapon_data.Accessory2PartDefinition,
    )

    weapon_data.MaterialPartDefinition_Index = parts_combo(
        "MaterialPartDefinition",
        weapon_data.MaterialPartDefinition_Index,
        weapon_data.MaterialPartDefinition,
    )

    weapon_data.PrefixPartDefinition_Index = parts_combo(
        "PrefixPartDefinition",
        weapon_data.PrefixPartDefinition_Index,
        weapon_data.PrefixPartDefinition,
    )

    weapon_data.TitlePartDefinition_Index = parts_combo(
        "TitlePartDefinition",
        weapon_data.TitlePartDefinition_Index,
        weapon_data.TitlePartDefinition,
    )

    weapon_data.GameStage = game_stage_slider("GameStage", weapon_data.GameStage)


def draw_item_editor() -> None:
    item_data: ItemData = cast(ItemData, player_inventory.item_data)

    item_data.ItemDefinition_Index = parts_combo(
        "ItemDefinition", item_data.ItemDefinition_Index, item_data.ItemDefinition
    )

    item_data.BalanceDefinition_Index = parts_combo(
        "BalanceDefinition",
        item_data.BalanceDefinition_Index,
        item_data.BalanceDefinition,
    )

    item_data.ManufacturerDefinition_Index = parts_combo(
        "ManufacturerDefinition",
        item_data.ManufacturerDefinition_Index,
        item_data.ManufacturerDefinition,
    )

    item_data.ManufacturerGradeIndex = game_stage_slider(
        "ManufacturerGradeIndex", item_data.ManufacturerGradeIndex
    )

    item_data.AlphaItemPartDefinition_Index = parts_combo(
        "AlphaItemPartDefinition",
        item_data.AlphaItemPartDefinition_Index,
        item_data.AlphaItemPartDefinition,
    )

    item_data.BetaItemPartDefinition_Index = parts_combo(
        "BetaItemPartDefinition",
        item_data.BetaItemPartDefinition_Index,
        item_data.BetaItemPartDefinition,
    )

    item_data.GammaItemPartDefinition_Index = parts_combo(
        "GammaItemPartDefinition",
        item_data.GammaItemPartDefinition_Index,
        item_data.GammaItemPartDefinition,
    )

    item_data.DeltaItemPartDefinition_Index = parts_combo(
        "DeltaItemPartDefinition",
        item_data.DeltaItemPartDefinition_Index,
        item_data.DeltaItemPartDefinition,
    )

    item_data.EpsilonItemPartDefinition_Index = parts_combo(
        "EpsilonItemPartDefinition",
        item_data.EpsilonItemPartDefinition_Index,
        item_data.EpsilonItemPartDefinition,
    )

    item_data.ZetaItemPartDefinition_Index = parts_combo(
        "ZetaItemPartDefinition",
        item_data.ZetaItemPartDefinition_Index,
        item_data.ZetaItemPartDefinition,
    )

    item_data.EtaItemPartDefinition_Index = parts_combo(
        "EtaItemPartDefinition",
        item_data.EtaItemPartDefinition_Index,
        item_data.EtaItemPartDefinition,
    )

    item_data.ThetaItemPartDefinition_Index = parts_combo(
        "ThetaItemPartDefinition",
        item_data.ThetaItemPartDefinition_Index,
        item_data.ThetaItemPartDefinition,
    )

    item_data.MaterialItemPartDefinition_Index = parts_combo(
        "MaterialItemPartDefinition",
        item_data.MaterialItemPartDefinition_Index,
        item_data.MaterialItemPartDefinition,
    )

    item_data.GameStage = game_stage_slider("GameStage", item_data.GameStage)

    imgui.separator()
    imgui.text("Quantity:")
    imgui.push_item_width(-1)
    changed, player_inventory.item.Quantity = imgui.slider_int(
        "##Quantity", player_inventory.item.Quantity, 1, 999
    )
