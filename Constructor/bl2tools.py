import unrealsdk


def get_player_controller():
    """
    Get the current WillowPlayerController Object.
    :return: WillowPlayerController
    """
    return unrealsdk.GetEngine().GamePlayers[0].Actor


def get_obj_path_name(object):
    """
    Get the full correct name of the provided object.
    :param object: UObject
    :return: String of the Path Name
    """
    if object:
        return object.PathName(object)
    else:
        return "None"


def console_command(command, bWriteToLog=False):
    """
    Executes a normal console command
    :param command: String, the command to execute.
    :param bWriteToLog: Bool, write to Log
    :return: None
    """
    get_player_controller().ConsoleCommand(command, bWriteToLog)


def obj_is_in_class(obj, inClass):
    """
    Compares the given Objects class with the given class.
    :param obj: UObject
    :param inClass: String, the Class to compare with
    :return: Bool, whether or not it's in the Class.
    """
    return bool(obj.Class == unrealsdk.FindClass(inClass))


def get_weapon_holding():
    """
    Get the weapon the WillowPlayerPawn is currently holding.
    :return: WillowWeapon
    """
    return unrealsdk.GetEngine().GamePlayers[0].Actor.Pawn.Weapon


def get_world_info():
    return unrealsdk.GetEngine().GetCurrentWorldInfo()
