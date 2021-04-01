from typing import Dict, List

import unrealsdk

from .. import bl2tools

# only for auto complete
ItemDefinition = "ItemDefinition"
BalanceDefinition = "BalanceDefinition"
ManufacturerDefinition = "ManufacturerDefinition"
ManufacturerGradeIndex = "ManufacturerGradeIndex"
AlphaItemPartDefinition = "AlphaItemPartDefinition"
BetaItemPartDefinition = "BetaItemPartDefinition"
GammaItemPartDefinition = "GammaItemPartDefinition"
DeltaItemPartDefinition = "DeltaItemPartDefinition"
EpsilonItemPartDefinition = "EpsilonItemPartDefinition"
ZetaItemPartDefinition = "ZetaItemPartDefinition"
EtaItemPartDefinition = "EtaItemPartDefinition"
ThetaItemPartDefinition = "ThetaItemPartDefinition"
MaterialItemPartDefinition = "MaterialItemPartDefinition"
PrefixItemNamePartDefinition = "PrefixItemNamePartDefinition"
TitleItemNamePartDefinition = "TitleItemNamePartDefinition"
GameStage = "GameStage"

classes: Dict[str, List[str]] = {
    "Class WillowGame.WillowUsableItem": ["UsableItemDefinition"],
    "Class WillowGame.WillowArtifact": ["ArtifactDefinition"],
    "Class WillowGame.WillowClassMod": ["ClassModDefinition", "CrossDLCClassModDefinition"],
    "Class WillowGame.WillowGrenadeMod": ["GrenadeModDefinition"],
    "Class WillowGame.WillowMissionItem": ["MissionItemDefinition"],
    "Class WillowGame.WillowUsableCustomizationItem": ["UsableCustomizationItemDefinition"],
    "Class WillowGame.WillowShield": ["ShieldDefinition"],

}

data = {ItemDefinition: [0, []],
        BalanceDefinition: [0, []],
        ManufacturerDefinition: [0, []],
        ManufacturerGradeIndex: 0,
        AlphaItemPartDefinition: [0, []],
        BetaItemPartDefinition: [0, []],
        GammaItemPartDefinition: [0, []],
        DeltaItemPartDefinition: [0, []],
        EpsilonItemPartDefinition: [0, []],
        ZetaItemPartDefinition: [0, []],
        EtaItemPartDefinition: [0, []],
        ThetaItemPartDefinition: [0, []],
        MaterialItemPartDefinition: [0, []],
        PrefixItemNamePartDefinition: [0, []],
        TitleItemNamePartDefinition: [0, []],
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


def update(edit_item: unrealsdk.UObject) -> None:
    global data
    global classes
    item_data: unrealsdk.FStruct = edit_item.DefinitionData
    # get all possible weapon types and balances, we will filter them later
    available_item_defs: List[unrealsdk.UObject] = []
    for uclass in classes[str(edit_item.Class)]:
        available_item_defs.extend(unrealsdk.FindAll(uclass)[1:])
    available_item_defs.append(None)

    all_bd: List[unrealsdk.UObject] = unrealsdk.FindAll("InventoryBalanceDefinition")[1:]
    all_bd.extend(unrealsdk.FindAll("ClassModBalanceDefinition")[1:])

    balance: unrealsdk.UObject = item_data.BalanceDefinition

    # the user should be able to completely change the weapon type. So let's allow all WTD.
    data[ItemDefinition] = [_index(available_item_defs, item_data.ItemDefinition), available_item_defs]
    curr_item_def: unrealsdk.UObject = available_item_defs[data[ItemDefinition][0]]  # the current ItemDefinition

    # now filter the possible BalanceDefinitions, only if they hold the current WeaponType
    available_item_defs: List[unrealsdk.UObject] = []
    for x in all_bd:  # type: unrealsdk.UObject
        if bl2tools.obj_is_in_class(x, "ClassModBalanceDefinition"):
            t = x
            while t.ClassModDefinitions is None and t.BaseDefinition is not None:
                t = t.BaseDefinition
            if curr_item_def in t.ClassModDefinitions:
                available_item_defs.append(x)
        else:
            if curr_item_def is x.InventoryDefinition:
                available_item_defs.append(x)
    available_item_defs.append(None)

    data[BalanceDefinition] = [_index(available_item_defs, balance), available_item_defs]

    manus: List[unrealsdk.UObject] = unrealsdk.FindAll("ManufacturerDefinition")[1:]
    manus.append(None)
    data[ManufacturerDefinition] = [_index(manus, item_data.ManufacturerDefinition), manus]

    data[ManufacturerGradeIndex] = item_data.ManufacturerGradeIndex

    if curr_item_def and any([bl2tools.obj_is_in_class(curr_item_def, "UsableCustomizationItemDefinition"),
                              bl2tools.obj_is_in_class(curr_item_def, "UsableItemDefinition"),
                              bl2tools.obj_is_in_class(curr_item_def, "MissionItemDefinition")]):
        if bl2tools.obj_is_in_class(curr_item_def, "MissionItemDefinition"):
            data[BalanceDefinition] = [0, [None]]
            data[ManufacturerDefinition] = [0, [None]]

        # I fucking hate how inconsistent WillowItems are
        data[AlphaItemPartDefinition] = [0, [None]]
        data[BetaItemPartDefinition] = [0, [None]]
        data[GammaItemPartDefinition] = [0, [None]]
        data[DeltaItemPartDefinition] = [0, [None]]
        data[EpsilonItemPartDefinition] = [0, [None]]
        data[ZetaItemPartDefinition] = [0, [None]]
        data[EtaItemPartDefinition] = [0, [None]]
        data[ThetaItemPartDefinition] = [0, [None]]
        data[MaterialItemPartDefinition] = [0, [None]]
        for val in data.values():
            if isinstance(val, list):
                val[1]: List[str] = [bl2tools.get_obj_path_name(x) for x in val[1]]
        return
    ############

    if not balance:
        for val in data.values():
            if isinstance(val, list):
                val[1]: List[str] = [bl2tools.get_obj_path_name(x) for x in val[1] if not isinstance(x, str)]
        return

    ###
    # Stupid monkey patch for stupid WillowShields, cuz WillowItems are fucking dumb
    ###
    if balance.InventoryDefinition \
            and bl2tools.obj_is_in_class(balance.InventoryDefinition, "ShieldDefinition") \
            and not balance.PartListCollection:
        return willow_shield_fixup(balance, item_data)

    ###

    part_list: unrealsdk.UObject = balance.PartListCollection  # holds all possible combinations

    if bl2tools.obj_is_in_class(balance, "ClassModBalanceDefinition"):
        part_list = balance.RuntimePartListCollection

    alphas: List[unrealsdk.UObject] = _get_available_parts(part_list.AlphaPartData.WeightedParts)
    alphas.append(None)
    data[AlphaItemPartDefinition] = [_index(alphas, item_data.AlphaItemPartDefinition), alphas]

    betas: List[unrealsdk.UObject] = _get_available_parts(part_list.BetaPartData.WeightedParts)
    betas.append(None)
    data[BetaItemPartDefinition] = [_index(betas, item_data.BetaItemPartDefinition), betas]

    gammas: List[unrealsdk.UObject] = _get_available_parts(part_list.GammaPartData.WeightedParts)
    gammas.append(None)
    data[GammaItemPartDefinition] = [_index(gammas, item_data.GammaItemPartDefinition), gammas]

    deltas: List[unrealsdk.UObject] = _get_available_parts(part_list.DeltaPartData.WeightedParts)
    deltas.append(None)
    data[DeltaItemPartDefinition] = [_index(deltas, item_data.DeltaItemPartDefinition), deltas]

    epsilons: List[unrealsdk.UObject] = _get_available_parts(part_list.EpsilonPartData.WeightedParts)
    epsilons.append(None)
    data[EpsilonItemPartDefinition] = [_index(epsilons, item_data.EpsilonItemPartDefinition), epsilons]

    zetas: List[unrealsdk.UObject] = _get_available_parts(part_list.ZetaPartData.WeightedParts)
    zetas.append(None)
    data[ZetaItemPartDefinition] = [_index(zetas, item_data.ZetaItemPartDefinition), zetas]

    etas: List[unrealsdk.UObject] = _get_available_parts(part_list.EtaPartData.WeightedParts)
    etas.append(None)
    data[EtaItemPartDefinition] = [_index(etas, item_data.EtaItemPartDefinition), etas]

    thetas: List[unrealsdk.UObject] = _get_available_parts(part_list.ThetaPartData.WeightedParts)
    thetas.append(None)
    data[ThetaItemPartDefinition] = [_index(thetas, item_data.ThetaItemPartDefinition), thetas]

    materials: List[unrealsdk.UObject] = _get_available_parts(part_list.MaterialPartData.WeightedParts)
    materials.append(None)
    data[MaterialItemPartDefinition] = [_index(materials, item_data.MaterialItemPartDefinition), materials]

    prefixes: List[unrealsdk.UObject] = []
    data[PrefixItemNamePartDefinition] = [-1, prefixes]

    titles: List[unrealsdk.UObject] = []
    data[TitleItemNamePartDefinition] = [-1, titles]

    data[GameStage] = item_data.GameStage

    # we only care for their names
    for val in data.values():
        if isinstance(val, list):
            val[1]: List[str] = [bl2tools.get_obj_path_name(x) for x in val[1]]


def willow_shield_fixup(balance: unrealsdk.UObject, item_data: unrealsdk.FStruct) -> None:
    global data
    shield_def: unrealsdk.UObject = balance.InventoryDefinition

    if shield_def.AlphaParts:
        alphas: List[unrealsdk.UObject] = _get_available_parts(shield_def.AlphaParts.WeightedParts)
        alphas.append(None)
        data[AlphaItemPartDefinition] = [_index(alphas, item_data.AlphaItemPartDefinition), alphas]
    else:
        data[AlphaItemPartDefinition] = [0, [None]]

    if shield_def.BetaParts:
        betas: List[unrealsdk.UObject] = _get_available_parts(shield_def.BetaParts.WeightedParts)
        betas.append(None)
        data[BetaItemPartDefinition] = [_index(betas, item_data.BetaItemPartDefinition), betas]
    else:
        data[BetaItemPartDefinition] = [0, [None]]

    if shield_def.GammaParts:
        gammas: List[unrealsdk.UObject] = _get_available_parts(shield_def.GammaParts.WeightedParts)
        gammas.append(None)
        data[GammaItemPartDefinition] = [_index(gammas, item_data.GammaItemPartDefinition), gammas]
    else:
        data[GammaItemPartDefinition] = [0, [None]]

    if shield_def.DeltaParts:
        deltas: List[unrealsdk.UObject] = _get_available_parts(shield_def.DeltaParts.WeightedParts)
        deltas.append(None)
        data[DeltaItemPartDefinition] = [_index(deltas, item_data.DeltaItemPartDefinition), deltas]
    else:
        data[DeltaItemPartDefinition] = [0, [None]]

    if shield_def.EpsilonParts:
        epsilons: List[unrealsdk.UObject] = _get_available_parts(shield_def.EpsilonParts.WeightedParts)
        epsilons.append(None)
        data[EpsilonItemPartDefinition] = [_index(epsilons, item_data.EpsilonItemPartDefinition), epsilons]
    else:
        data[EpsilonItemPartDefinition] = [0, [None]]

    if shield_def.ZetaParts:
        zetas: List[unrealsdk.UObject] = _get_available_parts(shield_def.ZetaParts.WeightedParts)
        zetas.append(None)
        data[ZetaItemPartDefinition] = [_index(zetas, item_data.ZetaItemPartDefinition), zetas]
    else:
        data[ZetaItemPartDefinition] = [0, [None]]

    if shield_def.EtaParts:
        etas: List[unrealsdk.UObject] = _get_available_parts(shield_def.EtaParts.WeightedParts)
        etas.append(None)
        data[EtaItemPartDefinition] = [_index(etas, item_data.EtaItemPartDefinition), etas]
    else:
        data[EtaItemPartDefinition] = [0, [None]]

    if shield_def.ThetaParts:

        thetas: List[unrealsdk.UObject] = _get_available_parts(shield_def.ThetaParts.WeightedParts)
        thetas.append(None)
        data[ThetaItemPartDefinition] = [_index(thetas, item_data.ThetaItemPartDefinition), thetas]
    else:
        data[ThetaItemPartDefinition] = [0, [None]]

    if shield_def.MaterialParts:
        materials: List[unrealsdk.UObject] = _get_available_parts(shield_def.MaterialParts.WeightedParts)
        materials.append(None)
        data[MaterialItemPartDefinition] = [_index(materials, item_data.MaterialItemPartDefinition), materials]
    else:
        data[MaterialItemPartDefinition] = [0, [None]]

    prefixes: List[unrealsdk.UObject] = []
    data[PrefixItemNamePartDefinition] = [-1, prefixes]

    titles: List[unrealsdk.UObject] = []
    data[TitleItemNamePartDefinition] = [-1, titles]

    data[GameStage] = item_data.GameStage

    for val in data.values():
        if isinstance(val, list):
            val[1]: List[str] = [bl2tools.get_obj_path_name(x) for x in val[1]]

