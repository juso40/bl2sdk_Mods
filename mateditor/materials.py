from functools import lru_cache
from typing import Dict, List, Optional, Tuple, Union

import unrealsdk  # type: ignore


class Materials:
    selected: Optional["MaterialInstanceConstant"] = None

    @staticmethod
    @lru_cache(maxsize=1)
    def all_materials(search: str) -> List[str]:
        return [
            m.PathName(m)
            for m in unrealsdk.FindAll("MaterialInstanceConstant")
            if search.lower() in m.PathName(m).lower()
        ]

    @staticmethod
    def select(material_name: str) -> bool:
        mat = unrealsdk.FindObject("MaterialInstanceConstant", material_name)
        if mat:
            Materials.selected = MaterialInstanceConstant(mat, material_name)
            return True
        return False


class Texture2D:
    search: str = ""
    index: int = 0

    backup: unrealsdk.UObject = None
    texture_parameter: str = ""

    @staticmethod
    @lru_cache(maxsize=1)
    def all_textures(search: str) -> List[str]:
        return [
            t.PathName(t)
            for t in unrealsdk.FindAll("Texture2D")
            if search.lower() in t.PathName(t).lower()
        ]


class MaterialInstanceConstant:
    def __init__(
        self, material_instance_constant: unrealsdk.UObject, path_name: str = ""
    ) -> None:
        self.material_instance_constant = material_instance_constant
        self.path_name = path_name or material_instance_constant.PathName(
            material_instance_constant
        )
        self.vector_parameters: Dict[str, Tuple[float, float, float, float]] = {}
        self.scalar_parameters: Dict[str, float] = {}
        self.texture_parameters: Dict[str, str] = {}
        self.update_parameters()

    def parents(self) -> List[unrealsdk.UObject]:
        """Index -1 is the root parent. Index 0 is the object itself."""
        parent: unrealsdk.UObject = self.material_instance_constant
        parents: List[unrealsdk.UObject] = [parent]
        while parent.Parent:
            parent = parent.Parent
            parents.append(parent)
        return parents

    def update_vector_parameters(self) -> None:
        parents = self.parents()

        for expression in parents[-1].Expressions:
            if (
                expression
                and expression.Class.Name == "MaterialExpressionVectorParameter"
            ):
                # Just add any default value for now. Most skins overwrite them anyway.
                self.vector_parameters[expression.ParameterName] = (1.0, 1.0, 1.0, 1.0)

        # Walk from root to our material and update all VectorParameters
        for material in parents[:-1]:
            for param in material.VectorParameterValues:
                p_val = param.ParameterValue
                self.vector_parameters[param.ParameterName] = (
                    p_val.R,
                    p_val.G,
                    p_val.B,
                    p_val.A,
                )

    def update_scalar_parameters(self) -> None:
        parents = self.parents()

        for expression in parents[-1].Expressions:
            if (
                expression
                and expression.Class.Name == "MaterialExpressionScalarParameter"
            ):
                # Just add any default value for now. Most skins overwrite them anyway.
                self.scalar_parameters[expression.ParameterName] = 1.0

        # Walk from root to our material and update all ScalarParameters
        for material in parents[:-1]:
            for param in material.ScalarParameterValues:
                self.scalar_parameters[param.ParameterName] = param.ParameterValue

    def update_texture_parameters(self) -> None:
        parents = self.parents()

        for expression in parents[-1].Expressions:
            if (
                expression
                and expression.Class.Name
                == "MaterialExpressionTextureSampleParameter2D"
            ):
                # Just add any default value for now. Most skins overwrite them anyway.
                self.texture_parameters[expression.ParameterName] = ""

        # Walk from root to our material and update all TextureParameters
        for material in parents[:-1]:
            for param in material.TextureParameterValues:
                self.texture_parameters[param.ParameterName] = param.ParameterValue

    def update_parameters(self) -> None:
        self.vector_parameters = {}
        self.scalar_parameters = {}
        self.texture_parameters = {}
        self.update_vector_parameters()
        self.update_scalar_parameters()
        self.update_texture_parameters()

    def set_texture_parameter_value(
        self, parameter_name: str, parameter_value: Union[str, unrealsdk.UObject]
    ) -> None:
        if not Materials.selected:
            return
        if isinstance(parameter_value, str):
            parameter_value = unrealsdk.FindObject("Texture2D", parameter_value)
        Materials.selected.material_instance_constant.SetTextureParameterValue(
            parameter_name, parameter_value
        )

    def get_texture_parameter_value(self, parameter_name: str) -> unrealsdk.UObject:
        if not Materials.selected:
            return
        return Materials.selected.material_instance_constant.GetTextureParameterValue(
            parameter_name
        )

    def set_vector_parameter_value(
        self, parameter_name: str, parameter_value: Tuple[float, float, float, float]
    ) -> None:
        if not Materials.selected:
            return
        Materials.selected.material_instance_constant.SetVectorParameterValue(
            parameter_name, parameter_value
        )

    def set_scalar_parameter_value(
        self, parameter_name: str, parameter_value: float
    ) -> None:
        if not Materials.selected:
            return
        Materials.selected.material_instance_constant.SetScalarParameterValue(
            parameter_name, parameter_value
        )
