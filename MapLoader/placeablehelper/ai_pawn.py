from typing import List, Tuple, Union

import unrealsdk  # type: ignore

from .. import bl2tools  # noqa: TID252


def set_materials(ai_pawn: unrealsdk.UObject, materials: List[unrealsdk.UObject]) -> None:
    if materials is None:
        return
    ai_pawn.Mesh.Materials = materials


def set_scale(ai_pawn: unrealsdk.UObject, scale: float) -> None:
    ai_pawn.Mesh.Scale = scale


def set_scale3d(ai_pawn: unrealsdk.UObject, scale3d: List[float]) -> None:
    ai_pawn.Mesh.Scale3D = tuple(scale3d)
    ai_pawn.Mesh.ForceUpdate(True)


def set_rotation(ai_pawn: unrealsdk.UObject, rotator: Union[List[int], Tuple[int, int, int]]) -> None:
    ai_pawn.Mesh.Rotation = tuple(rotator)
    ai_pawn.Mesh.ForceUpdate(True)


def set_location(ai_pawn: unrealsdk.UObject, position: Union[List[float], Tuple[float, float, float]]) -> None:
    ai_pawn.Location = tuple(position)


def instantiate(ai_pawn_balance: unrealsdk.UObject) -> unrealsdk.UObject:
    if not ai_pawn_balance:
        return None
    pc = bl2tools.get_player_controller()
    _loc = (pc.Location.X, pc.Location.Y, pc.Location.Z)
    pop_master = unrealsdk.FindAll("WillowPopulationMaster")[-1]
    pawn = pop_master.SpawnPopulationControlledActor(
        ai_pawn_balance.AIPawnArchetype.Class,
        None,
        "",
        _loc,
        (0, 0, 0),
        ai_pawn_balance.AIPawnArchetype,
        False,
        False,
    )

    if pc.GetCurrentPlaythrough() != 2:
        will_pop = unrealsdk.FindAll("WillowPopulationOpportunityPoint")[1:]
        pop = unrealsdk.FindAll("PopulationOpportunityPoint")[1:]
        regions = pop if len(pop) > len(will_pop) else will_pop
        region_game_stage = max(pc.GetGameStageFromRegion(x.GameStageRegion) for x in regions if x.GameStageRegion)
    else:
        region_game_stage = max(x.GetGameStage() for x in unrealsdk.FindAll("WillowPlayerPawn") if x.Arms)
    # PopulationFactoryBalancedAIPawn 105-120:
    pawn.SetGameStage(region_game_stage)
    pawn.SetExpLevel(region_game_stage)
    pawn.SetGameStageForSpawnedInventory(region_game_stage)
    pawn.SetAwesomeLevel(0)
    pawn.Controller.InitializeCharacterClass()
    pawn.Controller.RecalculateAttributeInitializedState()
    pawn.InitializeBalanceDefinitionState(ai_pawn_balance, -1)
    ai_pawn_balance.SetupPawnItemPoolList(pawn)
    pawn.AddDefaultInventory()

    ai = pawn.MyWillowMind.GetAIDefinition()
    ai.TargetSearchRadius = 12000

    return pawn
