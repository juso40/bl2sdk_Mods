from typing import List

import unrealsdk

from .. import bl2tools

# only for auto complete
WeaponTypeDefinition = "WeaponTypeDefinition"
BalanceDefinition = "BalanceDefinition"
ManufacturerDefinition = "ManufacturerDefinition"
ManufacturerGradeIndex = "ManufacturerGradeIndex"
BodyPartDefinition = "BodyPartDefinition"
GripPartDefinition = "GripPartDefinition"
BarrelPartDefinition = "BarrelPartDefinition"
SightPartDefinition = "SightPartDefinition"
StockPartDefinition = "StockPartDefinition"
ElementalPartDefinition = "ElementalPartDefinition"
Accessory1PartDefinition = "Accessory1PartDefinition"
Accessory2PartDefinition = "Accessory2PartDefinition"
MaterialPartDefinition = "MaterialPartDefinition"
PrefixPartDefinition = "PrefixPartDefinition"
TitlePartDefinition = "TitlePartDefinition"
GameStage = "GameStage"

data = {WeaponTypeDefinition: [0, []],
        BalanceDefinition: [0, []],
        ManufacturerDefinition: [0, []],
        ManufacturerGradeIndex: 0,
        BodyPartDefinition: [0, []],
        GripPartDefinition: [0, []],
        BarrelPartDefinition: [0, []],
        SightPartDefinition: [0, []],
        StockPartDefinition: [0, []],
        ElementalPartDefinition: [0, []],
        Accessory1PartDefinition: [0, []],
        Accessory2PartDefinition: [0, []],
        MaterialPartDefinition: [0, []],
        PrefixPartDefinition: [0, []],
        TitlePartDefinition: [0, []],
        GameStage: 0
        }


def _index(sequence: list, obj, default=0) -> int:
    try:
        return sequence.index(obj)
    except ValueError:
        return default


def _get_available_parts(_attr: unrealsdk.FStruct) -> list:
    if not _attr:
        return []
    return [x.Part for x in _attr]


def update(edit_weapon: unrealsdk.UObject) -> None:
    global data
    weapon_data = edit_weapon.DefinitionData
    # get all possible weapon types and balances, we will filter them later
    available_wtd: List[unrealsdk.UObject] = unrealsdk.FindAll("WeaponTypeDefinition")[1:]
    available_wtd.append(None)
    all_wbd: List[unrealsdk.UObject] = unrealsdk.FindAll("WeaponBalanceDefinition")[2:]

    balance: unrealsdk.UObject = weapon_data.BalanceDefinition

    # the user should be able to completely change the weapon type. So let's allow all WTD.
    data[WeaponTypeDefinition] = [_index(available_wtd, weapon_data.WeaponTypeDefinition), available_wtd]

    curr_wtd: unrealsdk.UObject = available_wtd[data[WeaponTypeDefinition][0]]  # the current WeaponTypeDefinition
    # now filter the possible WeaponBalanceDefinitions, only if they hold the current WeaponType
    available_wbd: List[unrealsdk.UObject] = [x for x in all_wbd if x.RuntimePartListCollection.AssociatedWeaponType
                                              is curr_wtd]
    available_wbd.append(None)
    data[BalanceDefinition] = [_index(available_wbd, balance), available_wbd]

    manus: List[unrealsdk.UObject] = unrealsdk.FindAll("ManufacturerDefinition")[1:]
    manus.append(None)
    data[ManufacturerDefinition] = [_index(manus, weapon_data.ManufacturerDefinition), manus]

    data[ManufacturerGradeIndex] = weapon_data.ManufacturerGradeIndex

    if not balance:
        for val in data.values():
            if isinstance(val, list):
                val[1]: List[str] = [bl2tools.get_obj_path_name(x) for x in val[1] if not isinstance(x, str)]
        return
    part_list: unrealsdk.UObject = balance.RuntimePartListCollection  # holds all possible combinations

    bodies: List[unrealsdk.UObject] = _get_available_parts(part_list.BodyPartData.WeightedParts)
    bodies.append(None)
    data[BodyPartDefinition] = [_index(bodies, weapon_data.BodyPartDefinition), bodies]

    grips: List[unrealsdk.UObject] = _get_available_parts(part_list.GripPartData.WeightedParts)
    grips.append(None)
    data[GripPartDefinition] = [_index(grips, weapon_data.GripPartDefinition), grips]

    barrels: List[unrealsdk.UObject] = _get_available_parts(part_list.BarrelPartData.WeightedParts)
    barrels.append(None)
    data[BarrelPartDefinition] = [_index(barrels, weapon_data.BarrelPartDefinition), barrels]

    sights: List[unrealsdk.UObject] = _get_available_parts(part_list.SightPartData.WeightedParts)
    sights.append(None)
    data[SightPartDefinition] = [_index(sights, weapon_data.SightPartDefinition), sights]

    stocks: List[unrealsdk.UObject] = _get_available_parts(part_list.StockPartData.WeightedParts)
    stocks.append(None)
    data[StockPartDefinition] = [_index(stocks, weapon_data.StockPartDefinition), stocks]

    elements: List[unrealsdk.UObject] = _get_available_parts(part_list.ElementalPartData.WeightedParts)
    elements.append(None)
    data[ElementalPartDefinition] = [_index(elements, weapon_data.ElementalPartDefinition), elements]

    acc1: List[unrealsdk.UObject] = _get_available_parts(part_list.Accessory1PartData.WeightedParts)
    acc1.append(None)
    data[Accessory1PartDefinition] = [_index(acc1, weapon_data.Accessory1PartDefinition), acc1]

    acc2: List[unrealsdk.UObject] = _get_available_parts(part_list.Accessory2PartData.WeightedParts)
    acc2.append(None)
    data[Accessory2PartDefinition] = [_index(acc2, weapon_data.Accessory2PartDefinition), acc2]

    materials: List[unrealsdk.UObject] = _get_available_parts(part_list.MaterialPartData.WeightedParts)
    materials.append(None)
    data[MaterialPartDefinition] = [_index(grips, weapon_data.MaterialPartDefinition), materials]

    prefixes: List[unrealsdk.UObject] = []
    data[PrefixPartDefinition] = [-1, prefixes]

    titles: List[unrealsdk.UObject] = []
    data[TitlePartDefinition] = [-1, titles]

    data[GameStage] = weapon_data.GameStage

    # we only care for their names
    for val in data.values():
        if isinstance(val, list):
            val[1]: List[str] = [bl2tools.get_obj_path_name(x) for x in val[1]]
