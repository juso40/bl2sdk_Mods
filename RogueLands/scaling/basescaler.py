from abc import ABC, abstractmethod

import unrealsdk


class BaseScaler(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def register_hooks(self):
        """Will only be called when the player is below lvl 50"""
        pass

    @abstractmethod
    def remove_hooks(self):
        pass

    @staticmethod
    def _get_pc() -> unrealsdk.UObject:
        return unrealsdk.GetEngine().GamePlayers[0].Actor

    @staticmethod
    def _get_player_level() -> int:
        return BaseScaler._get_pc().PlayerReplicationInfo.ExpLevel
