from . import BaseScaler

import unrealsdk


class RewardScaler(BaseScaler):
    def __init__(self):
        super().__init__()

    def register_hooks(self):
        def weapon_scaler(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            pc = caller
            unscaled_data = params.DefinitionData
            scaled = (
                unscaled_data.WeaponTypeDefinition,
                unscaled_data.BalanceDefinition,
                unscaled_data.ManufacturerDefinition,
                pc.PlayerReplicationInfo.ExpLevel,
                unscaled_data.BodyPartDefinition,
                unscaled_data.GripPartDefinition,
                unscaled_data.BarrelPartDefinition,
                unscaled_data.SightPartDefinition,
                unscaled_data.StockPartDefinition,
                unscaled_data.ElementalPartDefinition,
                unscaled_data.Accessory1PartDefinition,
                unscaled_data.Accessory2PartDefinition,
                unscaled_data.MaterialPartDefinition,
                unscaled_data.PrefixPartDefinition,
                unscaled_data.TitlePartDefinition,
                pc.PlayerReplicationInfo.ExpLevel,
                unscaled_data.UniqueId
            )

            unrealsdk.DoInjectedCallNext()
            caller.ReceiveWeaponReward(params.Mission, scaled)
            return False

        def item_scaler(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            pc = caller
            unscaled_data = params.DefinitionData
            scaled = (
                unscaled_data.ItemDefinition,
                unscaled_data.BalanceDefinition,
                unscaled_data.ManufacturerDefinition,
                pc.PlayerReplicationInfo.ExpLevel,
                unscaled_data.AlphaItemPartDefinition,
                unscaled_data.BetaItemPartDefinition,
                unscaled_data.GammaItemPartDefinition,
                unscaled_data.DeltaItemPartDefinition,
                unscaled_data.EpsilonItemPartDefinition,
                unscaled_data.ZetaItemPartDefinition,
                unscaled_data.EtaItemPartDefinition,
                unscaled_data.ThetaItemPartDefinition,
                unscaled_data.MaterialItemPartDefinition,
                unscaled_data.PrefixItemNamePartDefinition,
                unscaled_data.TitleItemNamePartDefinition,
                pc.PlayerReplicationInfo.ExpLevel,
                unscaled_data.UniqueId
            )
            unrealsdk.DoInjectedCallNext()
            caller.ReceiveItemReward(params.Mission, scaled)
            return False

        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ReceiveWeaponReward", str(id(self)), weapon_scaler)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ReceiveItemReward", str(id(self)), item_scaler)

    def remove_hooks(self):
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ReceiveWeaponReward", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ReceiveItemReward", str(id(self)))
