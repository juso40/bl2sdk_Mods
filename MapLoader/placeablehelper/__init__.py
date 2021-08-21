from typing import Dict
import time

import unrealsdk

from . import static_mesh
from . import ai_pawn
from . import interactive_objects

__all__ = ["load_map"]


def load_map(map_data: dict) -> None:
    start = time.time()

    cached_objects: Dict[str, unrealsdk.UObject] = {}

    creation_data: dict = map_data.get("Create", {})
    edit_data: dict = map_data.get("Edit", {})
    destruction_data: dict = map_data.get("Destroy", {})

    ###########
    # AIPawns #
    ###########
    for bp in creation_data.get("AIPawnBalanceDefinition", []):  # create
        for obj, attrs in bp.items():
            uobj: unrealsdk.UObject
            if obj in cached_objects:
                uobj = cached_objects[obj]
            else:
                uobj = unrealsdk.FindObject("AIPawnBalanceDefinition", obj)
                cached_objects[obj] = uobj
            _set_pawn_attrs(
                pawn=ai_pawn.instantiate(uobj),
                attrs=attrs
            )

    #######################
    # StaticMeshComponent #
    #######################
    for obj, attrs in edit_data.get("StaticMeshComponent", {}):  # edit
        _set_smc_attrs(
            smc=unrealsdk.FindObject("StaticMeshComponent", obj),
            attrs=attrs
        )

    for to_destroy in destruction_data.get("StaticMeshComponent", []):  # destroy
        static_mesh.destroy(unrealsdk.FindObject("StaticMeshComponent", to_destroy))

    for bp in creation_data.get("StaticMesh", []):  # create
        for obj, attrs in bp.items():
            uobj: unrealsdk.UObject
            if obj in cached_objects:
                uobj = cached_objects[obj]
            else:
                uobj = unrealsdk.FindObject("StaticMesh", obj)
                cached_objects[obj] = uobj
            _set_smc_attrs(
                smc=static_mesh.instantiate(uobj),
                attrs=attrs
            )

    ###############################
    # InteractiveObjectDefinition #
    ###############################
    for obj, attrs in edit_data.get("InteractiveObjectDefinition", {}).items():  # edit
        _set_io_attrs(
            io=unrealsdk.FindObject("Object", obj),
            attrs=attrs
        )

    for to_destroy in destruction_data.get("InteractiveObjectDefinition", []):  # destroy
        interactive_objects.destroy(unrealsdk.FindObject("Object", to_destroy))

    for bp in creation_data.get("InteractiveObjectDefinition", []):  # create
        for obj, attrs in bp.items():
            uobj: unrealsdk.UObject
            if obj in cached_objects:
                uobj = cached_objects[obj]
            else:
                uobj = unrealsdk.FindObject("Object", obj)
                cached_objects[obj] = uobj

            _set_io_attrs(
                io=interactive_objects.instantiate(uobj),
                attrs=attrs
            )

    unrealsdk.Log(f"Loading Map took {time.time()-start:.3f}s.")


########################################################################################################################

def _set_smc_attrs(smc: unrealsdk.UObject, attrs: dict) -> None:
    if not smc:
        return
    static_mesh.set_location(smc, attrs.get("Location", (0, 0, 0)))
    static_mesh.set_rotation(smc, attrs.get("Rotation", (0, 0, 0)))
    static_mesh.set_scale(smc, attrs.get("Scale", 1))
    static_mesh.set_scale3d(smc, attrs.get("Scale3D", (1, 1, 1)))

    mats = attrs.get("Materials", None)
    if mats is not None:
        mats = [unrealsdk.FindObject("MaterialInstanceConstant", m) for m in mats]
    static_mesh.set_materials(smc, mats)


def _set_io_attrs(io: unrealsdk.UObject, attrs: dict) -> None:
    if not io:
        return
    interactive_objects.set_location(io, attrs.get("Location", (0, 0, 0)))
    interactive_objects.set_rotation(io, attrs.get("Rotation", (0, 0, 0)))
    interactive_objects.set_scale(io, attrs.get("Scale", 1))
    interactive_objects.set_scale3d(io, attrs.get("Scale3D", (1, 1, 1)))

    mats = attrs.get("Materials", None)
    if mats is not None:
        mats = [unrealsdk.FindObject("MaterialInstanceConstant", m) for m in mats]

    interactive_objects.set_materials(io, mats)


def _set_pawn_attrs(pawn: unrealsdk.UObject, attrs: dict) -> None:
    if not pawn:
        return
    ai_pawn.set_location(pawn, attrs.get("Location", (0, 0, 0)))
    ai_pawn.set_rotation(pawn, attrs.get("Rotation", (0, 0, 0)))
    ai_pawn.set_scale(pawn, attrs.get("Scale", 1))
    ai_pawn.set_scale3d(pawn, attrs.get("Scale3D", (1, 1, 1)))

    mats = attrs.get("Materials", None)
    if mats is not None:
        mats = [unrealsdk.FindObject("MaterialInstanceConstant", m) for m in mats]
    ai_pawn.set_materials(pawn, mats)
