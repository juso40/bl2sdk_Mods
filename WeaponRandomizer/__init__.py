from random import choice
from typing import Any, Iterable

import unrealsdk  # type: ignore

from Mods.ModMenu import EnabledSaveType, OptionManager, Options, RegisterMod, SDKMod, Keybind


def path_name(obj: unrealsdk.UObject) -> str:
    return obj.PathName(obj) if obj else "None"


mode = Options.Spinner(
    Caption="Mode",
    Description="Change the way your random gun gets generated.",
    StartingValue="Balanced",
    Choices=["Balanced", "Mayhem"],
)
on_timer = Options.Boolean(
    Caption="On Timer",
    Description="If enabled, your weapon gets changed every x seconds.",
    StartingValue=True,
)
timer = Options.Slider(
    Caption="Timer",
    Description="Time in seconds between a new weapon gets generated.",
    StartingValue=15,
    MinValue=5,
    MaxValue=120,
    Increment=1,
)
keybind = Keybind(Name="Randomize Weapon", Key="B", OnPress=lambda: RandoInstance.change_weapon())


class Rando(SDKMod):
    Name = "Weapon Randomizer"
    Description = f"Changes your Weapon every {timer.CurrentValue} seconds or when you press '{keybind.Key}'."
    Author = "juso"
    Version = "1.0"
    SaveEnabledState = EnabledSaveType.LoadWithSettings

    Options = [mode, on_timer, timer]
    Keybinds = [keybind]

    def __init__(self) -> None:
        self.mayhem: bool = False
        self.old_gun: unrealsdk.UObject = None
        self.clock: float = 0.0
        self.WeaponParts = []
        self.WeaponTypeDefinition = []
        self.BalanceDefinition = []
        self.ManufacturerDefinition = []
        self.BodyPartDefinition = []
        self.GripPartDefinition = []
        self.BarrelPartDefinition = []
        self.SightPartDefinition = []
        self.StockPartDefinition = []
        self.ElementalPartDefinition = []
        self.Accessory1PartDefinition = []
        self.Accessory2PartDefinition = []
        self.MaterialPartDefinition = []
        self.PrefixPartDefinition = []
        self.TitlePartDefinition = []
        self.types = ("pistol", "sniper", "launcher", "shotgun", "smg", "assault")

    def Enable(self) -> None:  # noqa: N802
        unrealsdk.RegisterHook("WillowGame.WillowGameViewportClient.Tick", "WeaponRandoTick", on_tick)
        self.populate_lists()

    def Disable(self) -> None:  # noqa: N802
        unrealsdk.RemoveHook("WillowGame.WillowGameViewportClient.Tick", "WeaponRandoTick")

    def ModOptionChanged(self, option: OptionManager.Options.Base, new_val: Any) -> None:  # noqa: N802, ANN401
        if option is mode:
            self.mayhem = new_val == "Mayhem"

    def populate_lists(self) -> None:
        self.WeaponParts = unrealsdk.FindAll("WeaponPartDefinition")

        self.WeaponTypeDefinition = unrealsdk.FindAll("WeaponTypeDefinition")
        self.BalanceDefinition = unrealsdk.FindAll("WeaponBalanceDefinition")
        self.ManufacturerDefinition = unrealsdk.FindAll("ManufacturerDefinition")
        self.BodyPartDefinition = [x for x in self.WeaponParts if ".body." in path_name(x).lower()]
        self.GripPartDefinition = [x for x in self.WeaponParts if ".grip." in path_name(x).lower()]
        self.BarrelPartDefinition = [x for x in self.WeaponParts if ".barrel." in path_name(x).lower()]
        self.SightPartDefinition = [x for x in self.WeaponParts if ".sight." in path_name(x).lower()]
        self.StockPartDefinition = [x for x in self.WeaponParts if ".stock." in path_name(x).lower()]
        self.ElementalPartDefinition = [x for x in self.WeaponParts if ".elemental." in path_name(x).lower()]
        self.Accessory1PartDefinition = [x for x in self.WeaponParts if ".accessory." in path_name(x).lower()]
        self.Accessory2PartDefinition = [x for x in self.WeaponParts if ".accessory." in path_name(x).lower()]
        self.MaterialPartDefinition = [x for x in self.WeaponParts if ".manufacturermaterials." in path_name(x).lower()]
        self.PrefixPartDefinition = [
            x for x in unrealsdk.FindAll("WeaponNamePartDefinition") if ".prefix" in path_name(x).lower()
        ]
        self.TitlePartDefinition = [
            x for x in unrealsdk.FindAll("WeaponNamePartDefinition") if ".title" in path_name(x).lower()
        ]

    def get_random_def_data(self) -> tuple:
        weapon_type = choice(self.types)

        def choice_c(seq: Iterable, weapon_type: str) -> unrealsdk.UObject:
            parts = [x for x in seq if weapon_type in path_name(x).lower()]
            if parts:
                return choice(parts)
            return None

        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        exp_level = pc.Pawn.GetExpLevel()
        return (
            choice_c(self.WeaponTypeDefinition, weapon_type),
            choice_c(self.BalanceDefinition, weapon_type),
            choice(self.ManufacturerDefinition),
            exp_level,
            choice_c(self.BodyPartDefinition, weapon_type),
            choice_c(self.GripPartDefinition, weapon_type),
            choice_c(self.BarrelPartDefinition, weapon_type),
            choice_c(self.SightPartDefinition, weapon_type),
            choice_c(self.StockPartDefinition, weapon_type),
            choice(self.ElementalPartDefinition),
            choice(self.Accessory1PartDefinition),
            choice(self.Accessory2PartDefinition),
            choice_c(self.MaterialPartDefinition, weapon_type),
            choice(self.PrefixPartDefinition),
            choice(self.TitlePartDefinition),
            exp_level,
            exp_level,
        )

    def get_random_def_data_mayhem(self) -> tuple:
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        exp_level = pc.Pawn.GetExpLevel()
        return (
            choice(self.WeaponTypeDefinition),
            choice(self.BalanceDefinition),
            choice(self.ManufacturerDefinition),
            exp_level,
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.WeaponParts),
            choice(self.PrefixPartDefinition),
            choice(self.TitlePartDefinition),
            exp_level,
            exp_level,
        )

    def change_weapon(self) -> None:
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        pawn_inv_manager = pc.GetPawnInventoryManager()
        if not self.old_gun:
            pass
        else:
            pawn_inv_manager.InventoryUnreadied(pawn_inv_manager.GetWeaponInSlot(1), False)

        willow_weapon = unrealsdk.GetEngine().GetCurrentWorldInfo().Spawn(unrealsdk.FindClass("WillowWeapon"))
        pawn_inv_manager.ChangedWeapon()

        definition_data = self.get_random_def_data_mayhem() if self.mayhem else self.get_random_def_data()

        willow_weapon.InitializeFromDefinitionData(definition_data, pawn_inv_manager.Instigator, True)
        willow_weapon.AdjustWeaponForBeingInBackpack()
        pawn_inv_manager.GiveStoredAmmoBeforeGoingToBackpack(
            definition_data[0].AmmoResource, definition_data[0].StartingAmmoCount
        )
        pawn_inv_manager.AddInventoryToBackpack(willow_weapon)
        pawn_inv_manager.ReadyBackpackInventory(willow_weapon, 1)
        self.old_gun = willow_weapon


RandoInstance = Rando()


def on_tick(
    _caller: unrealsdk.UObject,
    _function: unrealsdk.UFunction,
    params: unrealsdk.FStruct,
) -> bool:
    if not on_timer.CurrentValue:
        return True
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    worldinfo = unrealsdk.GetEngine().GetCurrentWorldInfo()
    if pc.GFxUIManager.WantsPause() or pc.bStatusMenuOpen or worldinfo.GetStreamingPersistentMapName() == "menumap":
        return True
    RandoInstance.clock += params.DeltaTime
    if RandoInstance.clock > timer.CurrentValue:
        RandoInstance.clock = 0.0
        RandoInstance.change_weapon()
    return True


RegisterMod(RandoInstance)
