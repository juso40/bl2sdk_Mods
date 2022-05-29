from typing import List

from .stat import Stat

import importlib
import os

# import all folders in this directory
for f in os.listdir(os.path.dirname(__file__)):
    if os.path.isdir(os.path.join(os.path.dirname(__file__), f)):
        importlib.import_module(".{}".format(f), package=__package__)

__all__: List[str] = ["StatManagerInstance"]


class StatManager:
    stats_dict_key = "Stats"

    def load_stats(self, save_dict: dict) -> None:
        stats_dict = save_dict.get(self.stats_dict_key, {})
        for stat in Stat.stats:
            stat.load_stat(stats_dict)

    def save_stats(self, save_dict: dict) -> None:
        stats_dict = save_dict.get(self.stats_dict_key, {})
        for stat in Stat.stats:
            stat.save_stat(stats_dict)
        save_dict[self.stats_dict_key] = stats_dict

    def get_presentable_stats(self) -> str:
        return "\n".join(stat.readable_stat_run for stat in Stat.stats if stat.name)

    def get_presentable_stats_total(self) -> str:
        return "\n".join(stat.readable_stat_total for stat in Stat.stats if stat.name)

    def on_death(self) -> None:
        for stat in Stat.stats:
            stat.on_death()

    def register_hooks(self) -> None:
        for stat in Stat.stats:
            stat.register_hooks()

    def remove_hooks(self) -> None:
        for stat in Stat.stats:
            stat.remove_hooks()


StatManagerInstance: StatManager = StatManager()
