from ..stat import Stat

import unrealsdk


class CurrencyStat(Stat):
    def __init__(self) -> None:
        self.name = ""
        self.value = 0
        self.total_value = 0

        self.outer_dict_key = "CurrencyStats"

    def currency_changed(self, diff: int, form: int) -> None:
        self.value += diff
        self.total_value += diff

    def register_hooks(self) -> None:
        def on_currency_changed(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            if not caller.IsLocalPlayerController():
                return True

            currency_diff = params.ChangedCurrency.CurrentAmount - params.ChangedCurrency.LastKnownAmount
            currency_form = params.ChangedCurrency.FormOfCurrency
            self.currency_changed(currency_diff, currency_form)

            return True

        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.OnCurrencyChanged",
            str(id(self)),
            on_currency_changed
        )

    def remove_hooks(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.OnCurrencyChanged", str(id(self)))

    def load_stat(self, save_dict: dict) -> None:
        stats = save_dict.get(self.outer_dict_key, {}).get(self.name, {})
        self.value = stats.get("Value", 0)
        self.total_value = stats.get("TotalValue", 0)

    def save_stat(self, save_dict: dict) -> None:
        save_dict[self.outer_dict_key] = save_dict.get("CurrencyStats", {})
