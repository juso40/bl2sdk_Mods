import time
from dataclasses import dataclass
from typing import Dict, List, Optional

import unrealsdk  # type: ignore

from . import ai_pawn, interactive_objects, static_mesh

__all__ = ["load_map", "unload_map", "CREATED_OBJECTS", "TAGGED_OBJECTS"]


@dataclass
class TaggedObject:
    path_name: str
    uclass: str
    tags: List[str]
    metadata: str

    @property
    def uobj(self) -> Optional[unrealsdk.UObject]:
        return unrealsdk.FindObject(self.uclass, self.path_name)


CREATED_OBJECTS: Dict[str, List[str]] = {
    "StaticMeshComponent": [],
    "InteractiveObjectDefinition": [],
}

TAGGED_OBJECTS: Dict[str, List[TaggedObject]] = {}


def load_map(map_data: dict) -> None:
    start = time.time()

    load_ai_pawns(map_data)
    load_static_meshes(map_data)
    load_interactive_objects(map_data)

    unrealsdk.Log(f"Loading Map took {time.time()-start:.3f}s.")


def load_static_meshes(map_data: dict) -> None:
    cached_objects: Dict[str, unrealsdk.UObject] = {}

    creation_data: dict = map_data.get("Create", {})
    edit_data: dict = map_data.get("Edit", {})
    destruction_data: dict = map_data.get("Destroy", {})

    for obj, attrs in edit_data.get("StaticMeshComponent", {}).items():  # edit
        _set_smc_attrs(smc=unrealsdk.FindObject("StaticMeshComponent", obj), attrs=attrs)

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
            smc: unrealsdk.UObject = static_mesh.instantiate(uobj)
            if smc:
                CREATED_OBJECTS["StaticMeshComponent"].append(smc.PathName(smc))
                _set_smc_attrs(smc=smc, attrs=attrs)


def load_ai_pawns(map_data: dict) -> None:
    cached_objects: Dict[str, unrealsdk.UObject] = {}
    creation_data: dict = map_data.get("Create", {})
    for bp in creation_data.get("AIPawnBalanceDefinition", []):  # create
        for obj, attrs in bp.items():
            uobj: unrealsdk.UObject
            if obj in cached_objects:
                uobj = cached_objects[obj]
            else:
                uobj = unrealsdk.FindObject("AIPawnBalanceDefinition", obj)
                cached_objects[obj] = uobj
            _set_pawn_attrs(pawn=ai_pawn.instantiate(uobj), attrs=attrs)


def load_interactive_objects(map_data: dict) -> None:
    cached_objects: Dict[str, unrealsdk.UObject] = {}

    creation_data: dict = map_data.get("Create", {})
    edit_data: dict = map_data.get("Edit", {})
    destruction_data: dict = map_data.get("Destroy", {})

    for obj, attrs in edit_data.get("InteractiveObjectDefinition", {}).items():  # edit
        _set_io_attrs(io=unrealsdk.FindObject("Object", obj), attrs=attrs)

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

            io_def: unrealsdk.UObject = interactive_objects.instantiate(uobj)
            if io_def:
                CREATED_OBJECTS["InteractiveObjectDefinition"].append(io_def.PathName(io_def))
                _set_io_attrs(io=io_def, attrs=attrs)


def unload_map() -> None:
    start: float = time.time()
    for smc in CREATED_OBJECTS["StaticMeshComponent"]:
        static_mesh.destroy(unrealsdk.FindObject("StaticMeshComponent", smc))
    for io in CREATED_OBJECTS["InteractiveObjectDefinition"]:
        interactive_objects.destroy(unrealsdk.FindObject("Object", io))
    CREATED_OBJECTS["InteractiveObjectDefinition"].clear()
    CREATED_OBJECTS["StaticMeshComponent"].clear()
    TAGGED_OBJECTS.clear()
    unrealsdk.Log(f"Unloaded map in {time.time()-start:.5f}s.")


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

    tagged_object: TaggedObject = TaggedObject(
        path_name=smc.PathName(smc),
        uclass=smc.Class.Name,
        tags=attrs.get("Tags", []),
        metadata=attrs.get("Metadata", ""),
    )
    for tag in attrs.get("Tags", []):
        TAGGED_OBJECTS.setdefault(tag, []).append(tagged_object)


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

    tagged_object: TaggedObject = TaggedObject(
        path_name=io.PathName(io),
        uclass=io.Class.Name,
        tags=attrs.get("Tags", []),
        metadata=attrs.get("Metadata", ""),
    )
    for tag in attrs.get("Tags", []):
        TAGGED_OBJECTS.setdefault(tag, []).append(tagged_object)


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

    tagged_object: TaggedObject = TaggedObject(
        path_name=pawn.PathName(pawn),
        uclass=pawn.Class.Name,
        tags=attrs.get("Tags", []),
        metadata=attrs.get("Metadata", ""),
    )
    for tag in attrs.get("Tags", []):
        TAGGED_OBJECTS.setdefault(tag, []).append(tagged_object)
