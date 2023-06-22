from typing import List

import unrealsdk  # type: ignore

from .classes import ItemData, ItemDefinition, WeaponData


def _index(sequence: list, obj, default=0) -> int:
    try:
        return sequence.index(obj)
    except ValueError:
        return default


def _get_available_parts(_attr: unrealsdk.FStruct) -> list:
    return [x.Part for x in _attr] if _attr else []


class WillowWeapon:
    @staticmethod
    def filter_allowed_parts(weapon: unrealsdk.UObject) -> WeaponData:
        result: WeaponData = WeaponData()
        if not weapon:
            return result

        definition_data = weapon.DefinitionData
        weapon_type_definitions: List[unrealsdk.UObject] = unrealsdk.FindAll(
            "WeaponTypeDefinition"
        )[1:]
        weapon_type_definitions.append(None)
        weapon_balance_definitions: List[unrealsdk.UObject] = unrealsdk.FindAll(
            "WeaponBalanceDefinition"
        )[2:]

        # The current Weapons WeaponBalanceDefinition
        # We need it to determine what parts are available
        # so in case it is None, we can't determine the parts and return empty lists
        balance_definition: unrealsdk.UObject = definition_data.BalanceDefinition

        # DefinitionData.WeaponTypeDefinition
        result.WeaponTypeDefinition = tuple(weapon_type_definitions)
        result.WeaponTypeDefinition_Index = _index(
            weapon_type_definitions, definition_data.WeaponTypeDefinition
        )

        current_weapon_type_definition: unrealsdk.UObject = weapon_type_definitions[
            result.WeaponTypeDefinition_Index
        ]
        # Filter the possible WeaponBalanceDefinitions, only if they hold the current WeaponType
        weapon_balance_definitions = [
            weapon_balance_definition
            for weapon_balance_definition in weapon_balance_definitions
            if weapon_balance_definition.RuntimePartListCollection.AssociatedWeaponType
            is current_weapon_type_definition
        ]
        weapon_balance_definitions.append(None)

        # DefinitionData.BalanceDefinition
        result.BalanceDefinition = tuple(weapon_balance_definitions)
        result.BalanceDefinition_Index = _index(
            weapon_balance_definitions, balance_definition
        )

        # DefinitionData.ManufacturerDefinition
        manufacturer_definitions: List[unrealsdk.UObject] = unrealsdk.FindAll(
            "ManufacturerDefinition"
        )[1:]
        manufacturer_definitions.append(None)
        result.ManufacturerDefinition = tuple(manufacturer_definitions)
        result.ManufacturerDefinition_Index = _index(
            manufacturer_definitions, definition_data.ManufacturerDefinition
        )

        # DefinitionData.ManufacturerGradeIndex
        result.ManufacturerGradeIndex = definition_data.ManufacturerGradeIndex

        # DefinitionData.GameStage
        result.GameStage = definition_data.GameStage

        # If no BalanceDefinition is set, we can't determine the possible parts, so return empty lists
        if not balance_definition:
            return result

        # The RuntimePartListCollection contains all allowed parts for our current weapon
        part_list: unrealsdk.UObject = balance_definition.RuntimePartListCollection

        # DefinitionData.BodyPartDefinition
        bodies: List[unrealsdk.UObject] = _get_available_parts(
            part_list.BodyPartData.WeightedParts
        )
        bodies.append(None)
        result.BodyPartDefinition = tuple(bodies)
        result.BodyPartDefinition_Index = _index(
            bodies, definition_data.BodyPartDefinition
        )

        # DefinitionData.GripPartDefinition
        grips: List[unrealsdk.UObject] = _get_available_parts(
            part_list.GripPartData.WeightedParts
        )
        grips.append(None)
        result.GripPartDefinition = tuple(grips)
        result.GripPartDefinition_Index = _index(
            grips, definition_data.GripPartDefinition
        )

        # DefinitionData.BarrelPartDefinition
        barrels: List[unrealsdk.UObject] = _get_available_parts(
            part_list.BarrelPartData.WeightedParts
        )
        barrels.append(None)
        result.BarrelPartDefinition = tuple(barrels)
        result.BarrelPartDefinition_Index = _index(
            barrels, definition_data.BarrelPartDefinition
        )

        # DefinitionData.SightPartDefinition
        sights: List[unrealsdk.UObject] = _get_available_parts(
            part_list.SightPartData.WeightedParts
        )
        sights.append(None)
        result.SightPartDefinition = tuple(sights)
        result.SightPartDefinition_Index = _index(
            sights, definition_data.SightPartDefinition
        )

        # DefinitionData.StockPartDefinition
        stocks: List[unrealsdk.UObject] = _get_available_parts(
            part_list.StockPartData.WeightedParts
        )
        stocks.append(None)
        result.StockPartDefinition = tuple(stocks)
        result.StockPartDefinition_Index = _index(
            stocks, definition_data.StockPartDefinition
        )

        # DefinitionData.ElementalPartDefinition
        elements: List[unrealsdk.UObject] = _get_available_parts(
            part_list.ElementalPartData.WeightedParts
        )
        elements.append(None)
        result.ElementalPartDefinition = tuple(elements)
        result.ElementalPartDefinition_Index = _index(
            elements, definition_data.ElementalPartDefinition
        )

        # DefinitionData.Accessory1PartDefinition
        acc1: List[unrealsdk.UObject] = _get_available_parts(
            part_list.Accessory1PartData.WeightedParts
        )
        acc1.append(None)
        result.Accessory1PartDefinition = tuple(acc1)
        result.Accessory1PartDefinition_Index = _index(
            acc1, definition_data.Accessory1PartDefinition
        )

        # DefinitionData.Accessory2PartDefinition
        acc2: List[unrealsdk.UObject] = _get_available_parts(
            part_list.Accessory2PartData.WeightedParts
        )
        acc2.append(None)
        result.Accessory2PartDefinition = tuple(acc2)
        result.Accessory2PartDefinition_Index = _index(
            acc2, definition_data.Accessory2PartDefinition
        )

        # DefinitionData.MaterialPartDefinition
        materials: List[unrealsdk.UObject] = _get_available_parts(
            part_list.MaterialPartData.WeightedParts
        )
        materials.append(None)
        result.MaterialPartDefinition = tuple(materials)
        result.MaterialPartDefinition_Index = _index(
            grips, definition_data.MaterialPartDefinition
        )

        # DefinitionData.PrefixPartDefinition
        # Keep it empty, the game will auto generate the prefix
        result.PrefixPartDefinition_Index = -1

        # DefinitionData.TitlePartDefinition
        # Keep it empty, the game will auto generate the title
        result.TitlePartDefinition_Index = -1

        return result


class WillowItem:
    @staticmethod
    def filter_allowed_parts(item: unrealsdk.UObject) -> ItemData:
        result: ItemData = ItemData()
        if not item:
            return result

        # DefinitionData is the struct that holds the parts of the item
        definition_data = item.DefinitionData

        item_type_definitions: List[unrealsdk.UObject] = []
        for uclass in ItemDefinition.definitions[item.Class.Name]:
            item_type_definitions.extend(unrealsdk.FindAll(uclass)[1:])
        item_type_definitions.append(None)

        inventory_balance_definitions: List[unrealsdk.UObject] = unrealsdk.FindAll(
            "InventoryBalanceDefinition"
        )[1:]
        inventory_balance_definitions.extend(
            unrealsdk.FindAll("ClassModBalanceDefinition")[1:]
        )

        balance_definition = definition_data.BalanceDefinition

        result.ItemDefinition = tuple(item_type_definitions)
        result.ItemDefinition_Index = _index(
            item_type_definitions, definition_data.ItemDefinition
        )

        item_definition = item_type_definitions[result.ItemDefinition_Index]

        # Filter the allowed InventoryBalanceDefinitions for our selected item's ItemDefinition
        balance_definitions = []
        for bd in inventory_balance_definitions:
            if bd.Class.Name == "ClassModBalanceDefinition":
                t = bd
                while t.ClassModDefinitions is None and t.BaseDefinition is not None:
                    t = t.BaseDefinition
                if item_definition in t.ClassModDefinitions:
                    balance_definitions.append(bd)
            elif item_definition is bd.InventoryDefinition:
                balance_definitions.append(bd)
        balance_definitions.append(None)

        result.BalanceDefinition = tuple(balance_definitions)
        result.BalanceDefinition_Index = _index(balance_definitions, balance_definition)

        # DefinitionData.ManufacturerDefinition
        manufacturers: List[unrealsdk.UObject] = unrealsdk.FindAll(
            "ManufacturerDefinition"
        )[1:]
        manufacturers.append(None)
        result.ManufacturerDefinition = tuple(manufacturers)
        result.ManufacturerDefinition_Index = _index(
            manufacturers, definition_data.ManufacturerDefinition
        )

        # DefinitionData.ManufacturerGradeIndex
        result.ManufacturerGradeIndex = definition_data.ManufacturerGradeIndex
        # DefinitionData.GameStage
        result.GameStage = definition_data.GameStage

        # The following ItemDefinitions don't have parts, so we can return here
        if item_definition and item_definition.Class.Name in (
            "UsableCustomizationItemDefinition",
            "UsableItemDefinition",
            "MissionItemDefinition",
        ):
            if item_definition.Class.Name == "MissionItemDefinition":
                result.BalanceDefinition = (None,)
                result.BalanceDefinition_Index = 0
                result.ManufacturerDefinition = (None,)
                result.ManufacturerDefinition_Index = 0
            result.AlphaItemPartDefinition = (None,)
            result.AlphaItemPartDefinition_Index = 0
            result.BetaItemPartDefinition = (None,)
            result.BetaItemPartDefinition_Index = 0
            result.GammaItemPartDefinition = (None,)
            result.GammaItemPartDefinition_Index = 0
            result.DeltaItemPartDefinition = (None,)
            result.DeltaItemPartDefinition_Index = 0
            result.EpsilonItemPartDefinition = (None,)
            result.EpsilonItemPartDefinition_Index = 0
            result.ZetaItemPartDefinition = (None,)
            result.ZetaItemPartDefinition_Index = 0
            result.EtaItemPartDefinition = (None,)
            result.EtaItemPartDefinition_Index = 0
            result.ThetaItemPartDefinition = (None,)
            result.ThetaItemPartDefinition_Index = 0
            result.MaterialItemPartDefinition = (None,)
            result.MaterialItemPartDefinition_Index = 0
            return result

        # If no BalanceDefinition is set, we can't determine the possible parts, so return empty lists
        if not balance_definition:
            return result

        if (
            balance_definition.InventoryDefinition
            and balance_definition.InventoryDefinition.Class.Name == "ShieldDefinition"
            and not balance_definition.PartListCollection
        ):
            return WillowItem.update_fixup_shield(item, result)

        # The RuntimePartListCollection contains all allowed parts for our current item
        part_list: unrealsdk.UObject = balance_definition.PartListCollection
        if balance_definition.Class.Name == "ClassModBalanceDefinition":
            part_list = balance_definition.RuntimePartListCollection

        # DefinitionData.AlphaItemPartDefinition
        alphas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.AlphaPartData.WeightedParts
        )
        alphas.append(None)
        result.AlphaItemPartDefinition = tuple(alphas)
        result.AlphaItemPartDefinition_Index = _index(
            alphas, definition_data.AlphaItemPartDefinition
        )

        # DefinitionData.BetaItemPartDefinition
        betas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.BetaPartData.WeightedParts
        )
        betas.append(None)
        result.BetaItemPartDefinition = tuple(betas)
        result.BetaItemPartDefinition_Index = _index(
            betas, definition_data.BetaItemPartDefinition
        )

        # DefinitionData.GammaItemPartDefinition
        gammas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.GammaPartData.WeightedParts
        )
        gammas.append(None)
        result.GammaItemPartDefinition = tuple(gammas)
        result.GammaItemPartDefinition_Index = _index(
            gammas, definition_data.GammaItemPartDefinition
        )

        # DefinitionData.DeltaItemPartDefinition
        deltas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.DeltaPartData.WeightedParts
        )
        deltas.append(None)
        result.DeltaItemPartDefinition = tuple(deltas)
        result.DeltaItemPartDefinition_Index = _index(
            deltas, definition_data.DeltaItemPartDefinition
        )

        # DefinitionData.EpsilonItemPartDefinition
        epsilons: List[unrealsdk.UObject] = _get_available_parts(
            part_list.EpsilonPartData.WeightedParts
        )
        epsilons.append(None)
        result.EpsilonItemPartDefinition = tuple(epsilons)
        result.EpsilonItemPartDefinition_Index = _index(
            epsilons, definition_data.EpsilonItemPartDefinition
        )

        # DefinitionData.ZetaItemPartDefinition
        zetas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.ZetaPartData.WeightedParts
        )
        zetas.append(None)
        result.ZetaItemPartDefinition = tuple(zetas)
        result.ZetaItemPartDefinition_Index = _index(
            zetas, definition_data.ZetaItemPartDefinition
        )

        # DefinitionData.EtaItemPartDefinition
        etas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.EtaPartData.WeightedParts
        )
        etas.append(None)
        result.EtaItemPartDefinition = tuple(etas)
        result.EtaItemPartDefinition_Index = _index(
            etas, definition_data.EtaItemPartDefinition
        )

        # DefinitionData.ThetaItemPartDefinition
        thetas: List[unrealsdk.UObject] = _get_available_parts(
            part_list.ThetaPartData.WeightedParts
        )
        thetas.append(None)
        result.ThetaItemPartDefinition = tuple(thetas)
        result.ThetaItemPartDefinition_Index = _index(
            thetas, definition_data.ThetaItemPartDefinition
        )

        # DefinitionData.MaterialItemPartDefinition
        materials: List[unrealsdk.UObject] = _get_available_parts(
            part_list.MaterialPartData.WeightedParts
        )
        materials.append(None)
        result.MaterialItemPartDefinition = tuple(materials)
        result.MaterialItemPartDefinition_Index = _index(
            materials, definition_data.MaterialItemPartDefinition
        )

        # DefinitionData.PrefixItemNamePartDefinition
        result.PrefixItemNamePartDefinition_Index = -1

        # DefinitionData.TitleItemNamePartDefinition
        result.TitleItemNamePartDefinition_Index = -1

        return result

    @staticmethod
    def update_fixup_shield(item: unrealsdk.UObject, data: ItemData) -> ItemData:
        shield_definition = item.DefinitionData.BalanceDefinition.InventoryDefinition

        if shield_definition.AlphaParts:
            alphas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.AlphaParts.WeightedParts
            )
            alphas.append(None)
            data.AlphaItemPartDefinition = tuple(alphas)
            data.AlphaItemPartDefinition_Index = _index(
                alphas, item.DefinitionData.AlphaItemPartDefinition
            )
        else:
            data.AlphaItemPartDefinition = (None,)
            data.AlphaItemPartDefinition_Index = 0

        if shield_definition.BetaParts:
            betas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.BetaParts.WeightedParts
            )
            betas.append(None)
            data.BetaItemPartDefinition = tuple(betas)
            data.BetaItemPartDefinition_Index = _index(
                betas, item.DefinitionData.BetaItemPartDefinition
            )
        else:
            data.BetaItemPartDefinition = (None,)
            data.BetaItemPartDefinition_Index = 0

        if shield_definition.GammaParts:
            gammas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.GammaParts.WeightedParts
            )
            gammas.append(None)
            data.GammaItemPartDefinition = tuple(gammas)
            data.GammaItemPartDefinition_Index = _index(
                gammas, item.DefinitionData.GammaItemPartDefinition
            )
        else:
            data.GammaItemPartDefinition = (None,)
            data.GammaItemPartDefinition_Index = 0

        if shield_definition.DeltaParts:
            deltas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.DeltaParts.WeightedParts
            )
            deltas.append(None)
            data.DeltaItemPartDefinition = tuple(deltas)
            data.DeltaItemPartDefinition_Index = _index(
                deltas, item.DefinitionData.DeltaItemPartDefinition
            )
        else:
            data.DeltaItemPartDefinition = (None,)
            data.DeltaItemPartDefinition_Index = 0

        if shield_definition.EpsilonParts:
            epsilons: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.EpsilonParts.WeightedParts
            )
            epsilons.append(None)
            data.EpsilonItemPartDefinition = tuple(epsilons)
            data.EpsilonItemPartDefinition_Index = _index(
                epsilons, item.DefinitionData.EpsilonItemPartDefinition
            )
        else:
            data.EpsilonItemPartDefinition = (None,)
            data.EpsilonItemPartDefinition_Index = 0

        if shield_definition.ZetaParts:
            zetas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.ZetaParts.WeightedParts
            )
            zetas.append(None)
            data.ZetaItemPartDefinition = tuple(zetas)
            data.ZetaItemPartDefinition_Index = _index(
                zetas, item.DefinitionData.ZetaItemPartDefinition
            )
        else:
            data.ZetaItemPartDefinition = (None,)
            data.ZetaItemPartDefinition_Index = 0

        if shield_definition.EtaParts:
            etas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.EtaParts.WeightedParts
            )
            etas.append(None)
            data.EtaItemPartDefinition = tuple(etas)
            data.EtaItemPartDefinition_Index = _index(
                etas, item.DefinitionData.EtaItemPartDefinition
            )
        else:
            data.EtaItemPartDefinition = (None,)
            data.EtaItemPartDefinition_Index = 0

        if shield_definition.ThetaParts:
            thetas: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.ThetaParts.WeightedParts
            )
            thetas.append(None)
            data.ThetaItemPartDefinition = tuple(thetas)
            data.ThetaItemPartDefinition_Index = _index(
                thetas, item.DefinitionData.ThetaItemPartDefinition
            )
        else:
            data.ThetaItemPartDefinition = (None,)
            data.ThetaItemPartDefinition_Index = 0

        if shield_definition.MaterialParts:
            materials: List[unrealsdk.UObject] = _get_available_parts(
                shield_definition.MaterialParts.WeightedParts
            )
            materials.append(None)
            data.MaterialItemPartDefinition = tuple(materials)
            data.MaterialItemPartDefinition_Index = _index(
                materials, item.DefinitionData.MaterialItemPartDefinition
            )
        else:
            data.MaterialItemPartDefinition = (None,)
            data.MaterialItemPartDefinition_Index = 0

        return data
