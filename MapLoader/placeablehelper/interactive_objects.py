from contextlib import suppress
from typing import List, Tuple, Union

import unrealsdk  # type: ignore

from .. import bl2tools  # noqa: TID252


def set_materials(iobject: unrealsdk.UObject, materials: List[unrealsdk.UObject]) -> None:
    # As of now, the MapEditor doesent handle Materials for IO 100% correctly and sometimes exports wrong MICs.
    # So for now we simply ignore any materials, else the game might crash.
    return
    if materials is None or iobject.ObjectMesh is None:
        return
    iobject.ObjectMesh.Materials = materials


def get_materials(iobject: unrealsdk.UObject) -> List[unrealsdk.UObject]:
    raise NotImplementedError


def set_scale(iobject: unrealsdk.UObject, scale: float) -> None:
    iobject.DrawScale = scale


def get_scale(iobject: unrealsdk.UObject) -> float:
    return iobject.DrawScale


def set_scale3d(iobject: unrealsdk.UObject, scale3d: List[float]) -> None:
    iobject.DrawScale3D = tuple(scale3d)


def get_scale3d(iobject: unrealsdk.UObject) -> Tuple[float, float, float]:
    scale_3d = iobject.DrawScale3D
    return (scale_3d.X, scale_3d.Y, scale_3d.Z)


def set_rotation(iobject: unrealsdk.UObject, rotator: Union[List[int], Tuple[int, int, int]]) -> None:
    iobject.Rotation = tuple(rotator)


def get_rotation(iobject: unrealsdk.UObject) -> Tuple[int, int, int]:
    rotation = iobject.Rotation
    return (rotation.Pitch, rotation.Yaw, rotation.Roll)


def set_location(iobject: unrealsdk.UObject, position: Union[List[float], Tuple[float, float, float]]) -> None:
    iobject.Location = tuple(position)


def get_location(iobject: unrealsdk.UObject) -> Tuple[float, float, float]:
    location = iobject.Location
    return (location.X, location.Y, location.Z)


def instantiate(io_definition: unrealsdk.UObject) -> unrealsdk.UObject:
    if not io_definition:
        return False
    pc = bl2tools.get_player_controller()
    _loc = (pc.Location.X, pc.Location.Y, pc.Location.Z)
    pop_master = unrealsdk.FindAll("WillowPopulationMaster")[-1]

    is_bal_def = bl2tools.obj_is_in_class(io_definition, "InteractiveObjectBalanceDefinition")
    if is_bal_def:
        iobject = pop_master.SpawnPopulationControlledActor(
            io_definition.DefaultInteractiveObject.InteractiveObjectClass,
            None,
            "",
            _loc,
            (0, 0, 0),
        )
    else:
        iobject = pop_master.SpawnPopulationControlledActor(
            io_definition.InteractiveObjectClass,
            None,
            "",
            _loc,
            (0, 0, 0),
        )

    if pc.GetCurrentPlaythrough() != 2:
        will_pop = unrealsdk.FindAll("WillowPopulationOpportunityPoint")[1:]
        pop = unrealsdk.FindAll("PopulationOpportunityPoint")[1:]
        regions = pop if len(pop) > len(will_pop) else will_pop
        region_game_stage = max(pc.GetGameStageFromRegion(x.GameStageRegion) for x in regions if x.GameStageRegion)
    else:
        region_game_stage = max(x.GetGameStage() for x in unrealsdk.FindAll("WillowPlayerPawn") if x.Arms)

    iobject.SetGameStage(region_game_stage)
    iobject.SetExpLevel(region_game_stage)

    if is_bal_def:
        x = io_definition.SelectGradeIndex(region_game_stage, 0)
        iobject.InitializeBalanceDefinitionState(io_definition, x)
        io_definition.SetupInteractiveObjectLoot(iobject, x)
        iobject.InitializeFromDefinition(io_definition.DefaultInteractiveObject, False)

        if bl2tools.obj_is_in_class(iobject, "WillowVendingMachine") or bl2tools.obj_is_in_class(
            iobject,
            "WillowVendingMachineBlackMarket",
        ):
            _initialize_vending_machine(iobject)
    else:
        iobject.InitializeFromDefinition(io_definition, False)

    return iobject


def destroy(iobject: unrealsdk.UObject) -> None:
    with suppress(Exception):
        set_location(iobject, (-9999999, -9999999, -9999999))
        set_scale(iobject, 0)
        iobject.Destroyed()


def _initialize_vending_machine(iobject: unrealsdk.UObject) -> None:
    vending_name: str = bl2tools.get_obj_path_name(iobject.InteractiveObjectDefinition).lower()

    if "health" in vending_name:
        iobject.ShopType = 2
    elif "ammo" in vending_name:
        iobject.ShopType = 1
    else:
        iobject.ShopType = 0

    gamestage = unrealsdk.FindObject(
        "AttributeInitializationDefinition",
        "GD_Population_Shopping.Balance.Init_FeaturedItem_GameStage",
    )
    if "seraph" in vending_name:
        iobject.FixedItemCost = 120
        iobject.FixedFeaturedItemCost = 50
        iobject.FormOfCurrency = 2
        markup = None
        awesome = None
    elif "torgue" in vending_name:
        iobject.FixedItemCost = -1
        iobject.FixedFeaturedItemCost = 613
        iobject.FormOfCurrency = 4
        markup = unrealsdk.FindObject(
            "AttributeInitializationDefinition",
            "GD_Iris_TorgueTokenVendor.CommerceMarkup",
        )
        gamestage = unrealsdk.FindObject(
            "AttributeInitializationDefinition",
            "GD_Iris_TorgueTokenVendor.Balance.Init_FeaturedItem_GameStage",
        )
        awesome = None
    else:
        iobject.FixedItemCost = -1
        iobject.FixedFeaturedItemCost = -1
        iobject.FormOfCurrency = 0
        markup = unrealsdk.FindObject(
            "AttributeInitializationDefinition",
            "GD_Economy.VendingMachine.Init_MarkupCalc_P1",
        )
        awesome = unrealsdk.FindObject(
            "AttributeInitializationDefinition",
            "GD_Population_Shopping.Balance.Init_FeaturedItem_AwesomeLevel",
        )

    iobject.bOverrideFormOfCurrency = True

    iobject.CommerceMarkup = (1, None, markup, 1)
    iobject.InventoryConfigurationName = "Inventory"
    iobject.FeaturedItemCommerceMarkup = (int("togue" in vending_name), None, markup, 1)
    iobject.FeaturedItemConfigurationName = "FeaturedItem"
    iobject.FeaturedItemGameStage = (int(awesome is None), None, gamestage, 1)
    iobject.FeaturedItemAwesomeLevel = (0, None, awesome, 1)

    iobject.ResetInventory()

    if "blackmarket" in vending_name:
        iobject.ShopType = 3
        iobject.DefinitionData = unrealsdk.FindObject(
            "BlackMarketDefinition",
            "GD_BlackMarket.BlackMarket.MarketDef_BlackMarket",
        )
        iobject.FixedItemCost = 0
        iobject.FixedFeaturedItemCost = 0
