from typing import Union, Any

import unrealsdk

import random


def get_player_controller() -> unrealsdk.UObject:
    """
    Get the current WillowPlayerController Object.
    :return: WillowPlayerController
    """
    return unrealsdk.GetEngine().GamePlayers[0].Actor


def get_obj_path_name(uobject: unrealsdk.UObject) -> str:
    """
    Get the full correct name of the provided object.
    :param uobject: UObject
    :return: String of the Path Name
    """
    if uobject:
        return uobject.PathName(uobject)
    else:
        return "None"


def console_command(command: str, bWriteToLog: bool = False) -> None:
    """
    Executes a normal console command
    :param command: String, the command to execute.
    :param bWriteToLog: Bool, write to Log
    :return: None
    """
    get_player_controller().ConsoleCommand(command, bWriteToLog)


def obj_is_in_class(obj: unrealsdk.UObject, in_class: str) -> bool:
    """
    Compares the given Objects class with the given class.
    :param obj: UObject
    :param in_class: String, the Class to compare with
    :return: Bool, whether it's in the Class.
    """
    return bool(obj.Class == unrealsdk.FindClass(in_class))


def get_weapon_holding():
    """
    Get the weapon the WillowPlayerPawn is currently holding.
    :return: WillowWeapon
    """
    return unrealsdk.GetEngine().GamePlayers[0].Actor.Pawn.Weapon


def get_world_info() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GetCurrentWorldInfo()


def choice(seq) -> Union[Any, None]:
    """Return a random element from the sequence seq. If seq is empty, return None."""
    if not seq:
        return None
    return random.choice(seq)
