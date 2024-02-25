import re
from typing import Union

import unrealsdk
from unrealsdk import *

from . import bl2tools
from . import logging


def set_cmd(line: str) -> None:
    pattern = re.compile(r"^\s*(set)\s+(\S+)\s+(\S+)\s+\((.*)\)", re.IGNORECASE)  # simple array of objects
    obj = unrealsdk.FindObject("Object", line.split()[1])
    if not obj:
        logging.logger.error(f"Could not find Object: {line}")
        return
    re_line = re.match(pattern, line)
    if re_line:
        try:
            setattr(
                unrealsdk.FindObject("Object", re_line[2]),
                re_line[3],
                [unrealsdk.FindObject("Object", x.strip()) for x in re_line[4].split(",")],
            )
        except Exception as e:
            bl2tools.console_command(line)
            logging.logger.debug(e)
            logging.logger.debug(f"Could not manually parse and set command: {line}")
            logging.logger.debug(
                "The line above was instead set using normal console set command. "
                "Please obj dump and make sure everything is correct.",
            )

    else:
        try:
            attributes = line.split()[2].split(".")
            val = unrealsdk.FindObject("Object", line.split()[3])  # assume our val is an object
            if not val:  # Our val is not an object because FindObject returned None
                try:
                    val = int(line.split()[3])  # try to convert to int
                except ValueError:
                    try:
                        val = float(line.split()[3])  # assume it's a float
                    except ValueError:  # obviously not a float nor object
                        val = line.split()[3]
                        if val.lower() == "true":
                            val = True
                        elif val.lower() == "false":
                            val = False
                        elif val.lower() == "none":
                            val = None
            while len(attributes) > 1:
                attribute = attributes.pop(0)
                if "[" in attribute and "]" in attribute:
                    index = int(attribute[attribute.find("[") + 1 : attribute.find("]")])
                    obj = getattr(obj, attribute[: attribute.find("[")])[index]
                else:
                    obj = getattr(obj, attribute)
            if "[" in attributes[0] and "]" in attributes[0]:
                attribute = attributes[0]
                index = int(attribute[attribute.find("[") + 1 : attribute.find("]")])
                obj = getattr(obj, attribute[: attribute.find("[")])
                obj[index] = val
            else:
                setattr(obj, attributes[0], val)
        except IndexError:
            logging.logger.error(f"IndexError in line:\n->{line}")
        except Exception as e:
            logging.logger.error(e)
            logging.logger.error(f"Could not set using following statement: {line}")


def is_mission_done(required_mission: str) -> bool:
    pc = bl2tools.get_player_controller()
    for Mission in pc.MissionPlaythroughs[pc.GetCurrentPlaythrough()].MissionList:
        if bl2tools.get_obj_path_name(Mission.MissionDef) == required_mission and Mission.Status == 4:
            return True
    return False


def get_current_region_stage() -> int:
    pc = bl2tools.get_player_controller()
    if pc.GetCurrentPlaythrough() != 2:
        will_pop = unrealsdk.FindAll("WillowPopulationOpportunityPoint")[1:]
        pop = unrealsdk.FindAll("PopulationOpportunityPoint")[1:]
        regions = pop if len(pop) > len(will_pop) else will_pop
        region_game_stage = max(pc.GetGameStageFromRegion(x.GameStageRegion) for x in regions if x.GameStageRegion)
    else:
        # op_choice = pc.OverpowerChoiceValue
        region_game_stage = pc.Pawn.GetGameStage()  # (op_choice if op_choice is not None else 0)
    return region_game_stage


def check_conditions(line: str) -> Union[bool, str]:
    """
    Returns True if the conditions failed, returns str if conditions accepted and GroupKey was provided else False.
    :param line:
    :return:
    """
    _ret = False
    conditions = [x.strip() for x in line.split(";")]
    for cond in conditions:
        if cond.startswith("cond_level"):  # check the region_stage is > || < our given cond_level
            cond_lvl = cond.replace("cond_level", "")
            bigger_than = cond_lvl[0] == ">"
            if bigger_than and int(cond_lvl[1:]) > get_current_region_stage():
                # our current region stage is lower than the needed level, change ret value and break
                _ret = True
                break
            elif not bigger_than and int(cond_lvl[1:]) < get_current_region_stage():
                # our current region stage is higher than the needed level, change ret value and break
                _ret = True
                break
        elif cond.startswith("cond_mission_completed"):
            # cond_mission_completed_true only after given mission completion continue
            cond_mission = cond.replace("cond_mission_completed_", "")
            b_after_completion = cond_mission.split("=")[0] == "true"
            if b_after_completion and not is_mission_done(cond_mission.split("=", 1)[1]):
                _ret = True
                break
            elif not b_after_completion and is_mission_done(cond_mission.split("=", 1)[1]):
                _ret = True
                break
        elif cond.startswith("cond_add_random"):
            _ret = cond.split("=", 1)[1]

    return _ret
