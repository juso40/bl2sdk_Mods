from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import unrealsdk  # type: ignore


class ItemDefinition:
    ItemDefinition: str = "ItemDefinition"
    BalanceDefinition: str = "BalanceDefinition"
    ManufacturerDefinition: str = "ManufacturerDefinition"
    ManufacturerGradeIndex: str = "ManufacturerGradeIndex"
    AlphaItemPartDefinition: str = "AlphaItemPartDefinition"
    BetaItemPartDefinition: str = "BetaItemPartDefinition"
    GammaItemPartDefinition: str = "GammaItemPartDefinition"
    DeltaItemPartDefinition: str = "DeltaItemPartDefinition"
    EpsilonItemPartDefinition: str = "EpsilonItemPartDefinition"
    ZetaItemPartDefinition: str = "ZetaItemPartDefinition"
    EtaItemPartDefinition: str = "EtaItemPartDefinition"
    ThetaItemPartDefinition: str = "ThetaItemPartDefinition"
    MaterialItemPartDefinition: str = "MaterialItemPartDefinition"
    PrefixItemNamePartDefinition: str = "PrefixItemNamePartDefinition"
    TitleItemNamePartDefinition: str = "TitleItemNamePartDefinition"
    GameStage: str = "GameStage"

    definitions: Dict[str, List[str]] = {
        "WillowUsableItem": ["UsableItemDefinition"],
        "WillowArtifact": ["ArtifactDefinition"],
        "WillowClassMod": [
            "ClassModDefinition",
            "CrossDLCClassModDefinition",
        ],
        "WillowGrenadeMod": ["GrenadeModDefinition"],
        "WillowMissionItem": ["MissionItemDefinition"],
        "WillowUsableCustomizationItem": ["UsableCustomizationItemDefinition"],
        "WillowShield": ["ShieldDefinition"],
    }


class WeaponDefinition:
    WeaponTypeDefinition: str = "WeaponTypeDefinition"
    BalanceDefinition: str = "BalanceDefinition"
    ManufacturerDefinition: str = "ManufacturerDefinition"
    ManufacturerGradeIndex: str = "ManufacturerGradeIndex"
    BodyPartDefinition: str = "BodyPartDefinition"
    GripPartDefinition: str = "GripPartDefinition"
    BarrelPartDefinition = "BarrelPartDefinition"
    SightPartDefinition: str = "SightPartDefinition"
    StockPartDefinition: str = "StockPartDefinition"
    ElementalPartDefinition: str = "ElementalPartDefinition"
    Accessory1PartDefinition: str = "Accessory1PartDefinition"
    Accessory2PartDefinition: str = "Accessory2PartDefinition"
    MaterialPartDefinition: str = "MaterialPartDefinition"
    PrefixPartDefinition: str = "PrefixPartDefinition"
    TitlePartDefinition: str = "TitlePartDefinition"
    GameStage: str = "GameStage"

    definitions: Dict[str, List[str]] = {
        "WillowWeapon": ["WeaponTypeDefinition"],
    }


@dataclass
class ItemData:
    ItemDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    ItemDefinition_Index: int = -1
    BalanceDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    BalanceDefinition_Index: int = -1
    ManufacturerDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    ManufacturerDefinition_Index: int = -1
    ManufacturerGradeIndex: int = 1
    AlphaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    AlphaItemPartDefinition_Index: int = -1
    BetaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    BetaItemPartDefinition_Index: int = -1
    GammaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    GammaItemPartDefinition_Index: int = -1
    DeltaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    DeltaItemPartDefinition_Index: int = -1
    EpsilonItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    EpsilonItemPartDefinition_Index: int = -1
    ZetaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    ZetaItemPartDefinition_Index: int = -1
    EtaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    EtaItemPartDefinition_Index: int = -1
    ThetaItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    ThetaItemPartDefinition_Index: int = -1
    MaterialItemPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    MaterialItemPartDefinition_Index: int = -1
    PrefixItemNamePartDefinition: Tuple[unrealsdk.UObject] = field(
        default_factory=tuple
    )
    PrefixItemNamePartDefinition_Index: int = -1
    TitleItemNamePartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    TitleItemNamePartDefinition_Index: int = -1
    GameStage: int = 1


@dataclass
class WeaponData:
    WeaponTypeDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    WeaponTypeDefinition_Index: int = -1
    BalanceDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    BalanceDefinition_Index: int = -1
    ManufacturerDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    ManufacturerDefinition_Index: int = -1
    ManufacturerGradeIndex: int = 1
    BodyPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    BodyPartDefinition_Index: int = -1
    GripPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    GripPartDefinition_Index: int = -1
    BarrelPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    BarrelPartDefinition_Index: int = -1
    SightPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    SightPartDefinition_Index: int = -1
    StockPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    StockPartDefinition_Index: int = -1
    ElementalPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    ElementalPartDefinition_Index: int = -1
    Accessory1PartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    Accessory1PartDefinition_Index: int = -1
    Accessory2PartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    Accessory2PartDefinition_Index: int = -1
    MaterialPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    MaterialPartDefinition_Index: int = -1
    PrefixPartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    PrefixPartDefinition_Index: int = -1
    TitlePartDefinition: Tuple[unrealsdk.UObject] = field(default_factory=tuple)
    TitlePartDefinition_Index: int = -1
    GameStage: int = 1
