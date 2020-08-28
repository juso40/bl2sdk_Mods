import unrealsdk
from unrealsdk import *

from . import logging


@logging.log_all_calls(logging.call_logger)
class HookManager:

    def __init__(self, objects):
        self.call_order = sorted(objects.items())

    def Enable(self):
        def EndLoad(caller: UObject, function: UFunction, params: FStruct) -> bool:
            for _, obj in self.call_order:
                func = getattr(obj, "on_end_load")
                func()
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie", "EndLoading",
                               EndLoad)

    def Disable(self):
        pass
