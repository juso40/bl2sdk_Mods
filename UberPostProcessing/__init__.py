from typing import Any

from ..ModMenu import ModPriorities, ModTypes, RegisterMod, SDKMod, Options, EnabledSaveType, Hook

from .effects import all_options, rcon
from .presets import PresetsOptions

import unrealsdk


class UberPostProcessing(SDKMod):
    Name: str = "UberPostProcessing"
    Author: str = "juso"
    Description: str = (
        "Exposes many different post processing effects to the user."
        "Requires Depth of Field Setting to be enabled."
    )
    Version: str = "1.1"

    Types: ModTypes = ModTypes.Utility
    Priority = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    EnablePostProcessVolume = Options.Boolean(
        Caption="Post Process Volume",
        Description="Most Maps have their own custom Post Process Volume. Disable it to use your own settings.",
        StartingValue=True
    )
    Options = [EnablePostProcessVolume]

    def __init__(self):
        super().__init__()
        self.Options.append(PresetsOptions)
        self.Options.extend(all_options)

    def Enable(self) -> None:
        super().Enable()

        def update_nested(nested_option):
            if isinstance(nested_option, Options.Value):
                self.ModOptionChanged(nested_option, nested_option.CurrentValue)
            elif isinstance(nested_option, Options.Nested):
                for child in nested_option.Children:
                    update_nested(child)

        for option in self.Options:
            update_nested(option)

    def ModOptionChanged(self, option, new_value: Any) -> None:
        if option == self.EnablePostProcessVolume:
            return
        option.Callback(option, new_value)

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def _map_load(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        rcon("bEnabled", str(self.EnablePostProcessVolume.CurrentValue), obje="PostProcessVolume")
        return True


RegisterMod(UberPostProcessing())
