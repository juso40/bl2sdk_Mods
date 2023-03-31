import json
import os.path
from os import listdir
from os.path import isfile, join

import unrealsdk  # type: ignore

from Mods.ModMenu import Options

from ..effects import all_options  # noqa: TID252

# get the name of all .json files in this folder
json_files = [
    f.replace(".json", "")
    for f in listdir(__path__[0])  # type: ignore
    if isfile(join(__path__[0], f)) and f.endswith(".json")  # type: ignore
]
settings_json_path = join(__path__[0], "..", "settings.json")  # type: ignore
presets_path = __path__[0]  # type: ignore


def _preset_changed(option: Options.Value, new_value):
    if option.CurrentValue == "Custom":  # Save the users Custom preset
        try:
            with open(settings_json_path, "r") as f:
                settings = json.load(f)  # Get the old settings
                with open(os.path.join(presets_path, "Custom.json"), "w") as out:
                    json.dump(
                        settings, out, indent=4
                    )  # write them to the preset Custom.json file
        except FileNotFoundError:
            pass  # If the settings.json file doesn't exist, don't do anything
    with open(os.path.join(presets_path, f"{new_value}.json"), "r") as f:
        settings = json.load(f)
        with open(settings_json_path, "w") as out:
            json.dump(settings, out, indent=4)

        def _callback_rec(option: Options.Base, new_value):
            if isinstance(option, Options.Value):
                option.CurrentValue = new_value
                option.Callback(option, new_value)  # type: ignore
            elif isinstance(option, Options.Nested):
                for child in option.Children:
                    _callback_rec(child, new_value[child.Caption])

        for _option in all_options:
            _callback_rec(_option, settings["Options"][_option.Caption])


_presets_spinner = Options.Spinner(
    Caption="Preset",
    Description="Select a preset to load",
    StartingValue="Custom",
    Choices=json_files,
)
_presets_spinner.Callback = _preset_changed  # type: ignore

presets = [_presets_spinner]
PresetsOptions = Options.Nested(
    Caption="Presets", Description="Various Presets", Children=presets
)
