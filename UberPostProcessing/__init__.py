from typing import Any, List

import unrealsdk  # type: ignore

from Mods.ModMenu import (
    EnabledSaveType,
    Hook,
    ModPriorities,
    ModTypes,
    RegisterMod,
    SDKMod,
)
from Mods.ModMenu import Options as ModOptions

from .effects import all_options, rcon
from .presets import PresetsOptions


class UberPostProcessing(SDKMod):
    Name: str = "UberPostProcessing"
    Author: str = "juso"
    Description: str = (
        "Exposes many different post processing effects to the user."
        "Requires Depth of Field Setting to be enabled."
    )
    Version: str = "1.2"

    Types: ModTypes = ModTypes.Utility
    Priority = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    EnablePostProcessVolume = ModOptions.Boolean(
        Caption="Post Process Volume",
        Description="Most Maps have their own custom Post Process Volume. Disable it to use your own settings.",
        StartingValue=True,
    )
    Options: List[ModOptions.Base] = [EnablePostProcessVolume]

    def __init__(self):
        super().__init__()
        self.Options.append(PresetsOptions)
        self.Options.extend(all_options)

    def Enable(self) -> None:  # noqa: N802
        super().Enable()

        def update_nested(nested_option: ModOptions.Base) -> None:
            if isinstance(nested_option, ModOptions.Value):
                self.ModOptionChanged(nested_option, nested_option.CurrentValue)
            elif isinstance(nested_option, ModOptions.Nested):
                for child in nested_option.Children:
                    update_nested(child)

        for option in self.Options:
            update_nested(option)

    def ModOptionChanged(self, option, new_value: Any) -> None:  # noqa: N802
        if option == self.EnablePostProcessVolume:
            return
        option.Callback(option, new_value)  # type: ignore

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def _map_load(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        rcon(
            "bEnabled",
            str(self.EnablePostProcessVolume.CurrentValue),
            obje="PostProcessVolume",
        )
        return True


RegisterMod(UberPostProcessing())
