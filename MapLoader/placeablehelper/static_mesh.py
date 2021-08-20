from typing import List, Tuple, Union

import unrealsdk

from .. import bl2tools


def set_materials(sm_component: unrealsdk.UObject, materials: List[unrealsdk.UObject]) -> None:
    if materials is None:
        return
    sm_component.Materials = materials
    sm_component.ForceUpdate(False)


def set_scale(sm_component: unrealsdk.UObject, scale: float) -> None:
    sm_component.SetScale(scale)
    sm_component.ForceUpdate(False)


def set_scale3d(sm_component: unrealsdk.UObject, scale3d: List[float]) -> None:
    sm_component.Scale3D = tuple(scale3d)
    sm_component.ForceUpdate(False)


def set_rotation(sm_component: unrealsdk.UObject, rotator: Union[List[int], Tuple[int, int, int]]) -> None:
    sm_component.Rotation = tuple(rotator)
    sm_component.ForceUpdate(False)


def set_location(sm_component: unrealsdk.UObject, position: Union[List[float], Tuple[float, float, float]]) -> None:
    x, y, z = position
    sm_component.CachedParentToWorld.WPlane.X = x
    sm_component.CachedParentToWorld.WPlane.Y = y
    sm_component.CachedParentToWorld.WPlane.Z = z
    sm_component.ForceUpdate(False)
    sm_component.SetComponentRBFixed(True)


def instantiate(static_mesh: unrealsdk.UObject) -> unrealsdk.UObject:
    if not static_mesh:
        return None
    new_smc = bl2tools.get_world_info().MyEmitterPool.GetFreeStaticMeshComponent(True)
    collection_actor = unrealsdk.FindAll("StaticMeshCollectionActor")[-1]
    new_smc.SetStaticMesh(static_mesh, True)
    new_smc.SetBlockRigidBody(True)
    new_smc.SetActorCollision(True, True, True)
    new_smc.SetTraceBlocking(True, True)
    collection_actor.AttachComponent(new_smc)

    return new_smc


# noinspection PyBroadException
def destroy(sm_component: unrealsdk.UObject) -> None:
    try:  # faster than if statement for this case. Exception shouldn't happen most of the time.
        sm_component.DetachFromAny()
    except Exception:  # We really don't care if our object does not exist or is already deleted.
        pass
