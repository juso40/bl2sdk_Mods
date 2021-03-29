from typing import List, Tuple

import unrealsdk

from . import weapon_helper, item_helper
from .. import bl2tools

weapon_data: dict = weapon_helper.data
item_data: dict = item_helper.data
item_classes: List[str] = item_helper.classes

player_inventory: List[unrealsdk.UObject] = []
player_inventory_readable: List[str] = []


def update_inventory() -> None:
    global player_inventory
    global player_inventory_readable
    inv_manager: unrealsdk.UObject = bl2tools.get_player_controller().GetPawnInventoryManager()
    if not inv_manager:
        return

    player_inventory = [x for x in inv_manager.Backpack if x]
    player_inventory_readable = [f"{x.GetHumanReadableName()}##{i}" for i, x in enumerate(player_inventory)]
