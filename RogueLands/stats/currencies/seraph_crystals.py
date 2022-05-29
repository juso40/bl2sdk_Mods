from .base import CurrencyStat


class SeraphCrystalCurrencyStat(CurrencyStat):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Seraph Crystals"


    def currency_changed(self, diff: int, form: int) -> None:
        if form == 2:  # 2 is Seraph Crystal
            super().currency_changed(diff, form)

    def load_stat(self, save_dict: dict) -> None:
        super().load_stat(save_dict)

    def save_stat(self, save_dict: dict) -> None:
        super().save_stat(save_dict)
        save_dict["CurrencyStats"][self.name] = {"Value": self.value, "TotalValue": self.total_value}
