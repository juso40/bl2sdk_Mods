from . import BaseUnlockable

import unrealsdk


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


def spawn_interactive_object(obj_str: str, xyz: tuple, rot: tuple, pckg: str) -> None:
    pc: unrealsdk.UObject = _get_pc()

    unrealsdk.LoadPackage(pckg)
    io_definition: unrealsdk.UObject = unrealsdk.FindObject("Object", obj_str)

    pop_master: unrealsdk.UObject = unrealsdk.FindAll("WillowPopulationMaster")[-1]

    is_bal_def: bool = io_definition.Class.Name == "InteractiveObjectBalanceDefinition"
    if is_bal_def:
        iobject: unrealsdk.UObject = pop_master.SpawnPopulationControlledActor(
            io_definition.DefaultInteractiveObject.InteractiveObjectClass, None, "", xyz, rot
        )
    else:
        iobject: unrealsdk.UObject = pop_master.SpawnPopulationControlledActor(
            io_definition.InteractiveObjectClass, None, "", xyz, rot
        )

    region_game_stage = max(x.GetGameStage() for x in unrealsdk.FindAll("WillowPlayerPawn") if x.Arms)

    iobject.SetGameStage(region_game_stage)
    iobject.SetExpLevel(region_game_stage)

    if is_bal_def:
        x = io_definition.SelectGradeIndex(region_game_stage, 0)
        iobject.InitializeBalanceDefinitionState(io_definition, x)
        io_definition.SetupInteractiveObjectLoot(iobject, x)
        iobject.InitializeFromDefinition(io_definition.DefaultInteractiveObject, False)

        if iobject.Class.Name == "WillowVendingMachine":
            vending_name = pc.PathName(iobject.InteractiveObjectDefinition).lower()
            markup = unrealsdk.FindObject("AttributeInitializationDefinition",
                                          "GD_Economy.VendingMachine.Init_MarkupCalc_P1")
            iobject.CommerceMarkup.InitializationDefinition = markup
            iobject.FeaturedItemCommerceMarkup.InitializationDefinition = markup
            iobject.InventoryConfigurationName = "Inventory"
            iobject.FeaturedItemConfigurationName = "FeaturedItem"
            item_stage = unrealsdk.FindObject("AttributeInitializationDefinition",
                                              "GD_Population_Shopping.Balance.Init_FeaturedItem_GameStage")
            item_awesome = unrealsdk.FindObject("AttributeInitializationDefinition",
                                                "GD_Population_Shopping.Balance.Init_FeaturedItem_AwesomeLevel")
            iobject.FeaturedItemGameStage.InitializationDefinition = item_stage
            iobject.FeaturedItemAwesomeLevel.InitializationDefinition = item_awesome
            if "health" in vending_name:
                iobject.ShopType = 2
            elif "ammo" in vending_name:
                iobject.ShopType = 1
            elif "weapon" in vending_name:
                iobject.ShopType = 0

            iobject.ResetInventory()
    else:
        iobject.InitializeFromDefinition(io_definition, False)


class VendorUnlockable(BaseUnlockable):
    def __init__(self) -> None:
        super(VendorUnlockable, self).__init__("Vendors in Claptraps Place")

    def unlock(self) -> None:
        def map_load(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            curr_map = unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower()
            unrealsdk.Log(f"Loaded map: {curr_map}")
            if curr_map == "glacial_p":
                self.spawn_vendors()
            return True

        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie",
            str(id(self)),
            map_load
        )

    def lock(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie", str(id(self)))

    def spawn_vendors(self) -> None:
        for name, xyz, rot, pckg in [
            (
                    "GD_Balance_Shopping.VendingMachineGrades.ObjectGrade_VendingMachine_GrenadesAndAmmo",
                    (29017.896, 18389.484, 7544.399),
                    (9165, 21000, 3547),
                    "Sanctuary_P"
            ),
            (
                    "GD_Balance_Shopping.VendingMachineGrades.ObjectGrade_VendingMachine_HealthItems",
                    (27679.570, 18733.379, 7453.479),
                    (1667, 23500, -2153),
                    "Sanctuary_P"

            ),
            (
                    "GD_Balance_Shopping.VendingMachineGrades.ObjectGrade_VendingMachine_Weapons",
                    (28391.813, 20231.332, 7382.040),
                    (4567, -13283, 1147),
                    "Sanctuary_P"

            ),

        ]:
            spawn_interactive_object(name, xyz, rot, pckg)
