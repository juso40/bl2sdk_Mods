from pathlib import Path

import unrealsdk  # type: ignore

# The path to the Binaries folder of the game
PATH = Path(__file__).parent.parent.parent


class BLCMExport:
    file_name: str = "Skin"

    @staticmethod
    def save_to_file(path: Path, material: unrealsdk.UObject) -> None:
        with open(str(path.absolute()), "w") as fp:
            if not material:
                return
            obj_name: str = material.PathName(material)

            # We only need to store the VectorParameterValues on our selected material
            # as the other parameters are stored in the parent materials if not changed
            set_vector: str = "("
            if not material.VectorParameterValues:
                set_vector = "# No VectorParameterValues were set on this MaterialInstanceConstant."
            for param in material.VectorParameterValues:
                rgba = param.ParameterValue
                r, g, b, a = rgba.R, rgba.G, rgba.B, rgba.A
                set_vector += (
                    f"(ParameterName={param.ParameterName},"
                    f"ParameterValue=(R={r:.5f},G={g:.5f},B={b:.5f},A={a:.5f})),"
                )
            fp.write(f"set {obj_name} VectorParameterValues {set_vector[:-1]})\n")

            set_texture: str = "("
            if not material.TextureParameterValues:
                set_texture = "# No TextureParameterValues were set on this MaterialInstanceConstant."
            for param in material.TextureParameterValues:
                set_texture += (
                    f"(ParameterName={param.ParameterName}, "
                    f"ParameterValue=Texture2D'{material.PathName(param.ParameterValue)}'),"
                )
            fp.write(f"set {obj_name} TextureParameterValues {set_texture[:-1]})\n")

            set_scalar: str = "("
            if not material.ScalarParameterValues:
                set_scalar = "# No ScalarParameterValues were set on this MaterialInstanceConstant."
            for param in material.ScalarParameterValues:
                set_scalar += f"(ParameterName={param.ParameterName},ParameterValue={param.ParameterValue}),"
            fp.write(f"set {obj_name} ScalarParameterValues {set_scalar[:-1]})\n")
