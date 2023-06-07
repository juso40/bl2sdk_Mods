from typing import Any

import unrealsdk  # type: ignore

from Mods.ModMenu import EnabledSaveType, Hook, HookManager, RegisterMod, SDKMod
from Mods.ModMenu import Options as ModOptions

CrosshairSettings = ModOptions.Nested(
    "Custom Crosshair",
    "Static Custom Crosshair, requires optional dependencies 'coroutines' and 'CanvasLIB'",
    Children=[],
)

try:
    from .crosshair import option_changed, options

    CrosshairSettings.Children = options
except ImportError as e:

    def enable():
        return None

    def disable():
        return None

    def option_changed(option, new_value):
        return None

    CrosshairSettings.Children = [ModOptions.Hidden("Foo", "Bar")]


class Crosshair(SDKMod):
    Name = "No Crosshair"
    Description = "Removes the crosshairs."
    Author = "juso"
    Version = "1.1"
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    Options = [CrosshairSettings]

    def __init__(self) -> None:
        super().__init__()
        self.zoomed: bool = False

    def Enable(self) -> None:  # noqa: N802
        def update_nested(nested_option: ModOptions.Base) -> None:
            if isinstance(nested_option, ModOptions.Value):
                self.ModOptionChanged(nested_option, nested_option.CurrentValue)
            elif isinstance(nested_option, ModOptions.Nested):
                for child in nested_option.Children:
                    update_nested(child)

        for option in self.Options:
            update_nested(option)
        HookManager.RegisterHooks(self)

    @Hook("WillowGame.WillowWeapon.Active.BeginState")
    def disable_crosshair(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if not self.zoomed:
            caller.bCrosshairEnabled = False
            caller.bSuppressCrosshair = True
        else:
            caller.bCrosshairEnabled = True
            caller.bSuppressCrosshair = False
        return True

    @Hook("WillowGame.WillowWeapon.SetZoomState")
    def handle_zooming(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if params.NewZoomState == 2:
            self.zoomed = True
            caller.bCrosshairEnabled = True
            caller.bSuppressCrosshair = False
        else:
            self.zoomed = False
            caller.bCrosshairEnabled = False
            caller.bSuppressCrosshair = True
        return True

    def ModOptionChanged(  # noqa: N802
        self, option: ModOptions.Base, new_value: Any
    ) -> None:
        option_changed(option, new_value)


CrosshairInstance = Crosshair()
RegisterMod(CrosshairInstance)
