import traceback as tb

from .event import Event

import unrealsdk

__all__ = ["KilledEnemyEventManager"]


class KilledEnemyEvent(Event):
    """
    Event that is triggered when an enemy is killed. Calls all handlers.
    The handlers should be a function that takes the following parameters:

    caller: The UObject that called the function.
    function: The UFunction that was called.
    params: The parameters passed to the function.
    """
    hook: str = "WillowGame.WillowAIPawn.Died"

    def register_hooks(self):
        def on_killed_enemy(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            for handler in self._handlers:
                try:
                    handler(caller, function, params)
                except Exception:
                    unrealsdk.Log(f"[BadassBounties] {tb.format_exc()}")
            return True

        unrealsdk.RegisterHook(self.hook, str(id(self)), on_killed_enemy)

    def remove_hooks(self):
        unrealsdk.RemoveHook(self.hook, str(id(self)))


KilledEnemyEventManager: KilledEnemyEvent = KilledEnemyEvent()
