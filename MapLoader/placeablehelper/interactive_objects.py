from typing import List, Tuple, Union

import unrealsdk

from .. import bl2tools


def set_materials(iobject: unrealsdk.UObject, materials: List[unrealsdk.UObject]) -> None:
    if materials is None or iobject.ObjectMesh is None:
        return
    iobject.ObjectMesh.Materials = materials


def set_scale(iobject: unrealsdk.UObject, scale: float) -> None:
    iobject.DrawScale = scale


def set_scale3d(iobject: unrealsdk.UObject, scale3d: List[float]) -> None:
    iobject.DrawScale3D = tuple(scale3d)


def set_rotation(iobject: unrealsdk.UObject, rotator: Union[List[int], Tuple[int, int, int]]) -> None:
    iobject.Rotation = tuple(rotator)


def set_location(iobject: unrealsdk.UObject, position: Union[List[float], Tuple[float, float, float]]) -> None:
    iobject.Location = tuple(position)


def instantiate(io_definition: unrealsdk.UObject) -> unrealsdk.UObject:
    if not io_definition:
        unrealsdk.Log("Nope io")

        return False
    pc = bl2tools.get_player_controller()
    _loc = (pc.Location.X, pc.Location.Y, pc.Location.Z)
    pop_master = unrealsdk.FindAll("WillowPopulationMaster")[-1]

    is_bal_def = bl2tools.obj_is_in_class(io_definition, "InteractiveObjectBalanceDefinition")
    if is_bal_def:
        iobject = pop_master.SpawnPopulationControlledActor(
            io_definition.DefaultInteractiveObject.InteractiveObjectClass, None, "", _loc, (0, 0, 0)
        )
    else:
        iobject = pop_master.SpawnPopulationControlledActor(
            io_definition.InteractiveObjectClass, None, "", _loc, (0, 0, 0)
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

    return iobject


# noinspection PyBroadException
def destroy(iobject: unrealsdk.UObject) -> None:
    try:  # faster than if statement for this case. Exception shouldn't happen most of the time.
        set_location(iobject, (-9999999, -9999999, -9999999))
        set_scale(iobject, 0)
        iobject.Destroyed()
    except Exception:  # We really don't care if our object does not exist or is already deleted.
        pass
