from .basescaler import BaseScaler
from .lootscaler import LootScaler
from .enemyscaler import EnemyScaler
from .environmentscaler import EnvironmentScaler
from .rewardscaler import RewardScaler

__all__ = ["ScalerManagerInstance"]


class ScalerManager:
    def __init__(self):
        self.scalers = [
            LootScaler(),
            EnemyScaler(),
            EnvironmentScaler(),
            RewardScaler()
        ]

    def update(self):
        if BaseScaler._get_player_level() >= 50:
            self.remove_hooks()

    def register_hooks(self):
        if BaseScaler._get_player_level() >= 50:
            self.remove_hooks()
            return

        for scaler in self.scalers:
            scaler.register_hooks()

    def remove_hooks(self):
        for scaler in self.scalers:
            scaler.remove_hooks()


ScalerManagerInstance = ScalerManager()
