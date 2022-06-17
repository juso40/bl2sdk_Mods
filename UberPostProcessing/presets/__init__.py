import os.path
from os import listdir
from os.path import isfile, join
import json

from ...ModMenu import Options

import unrealsdk


from ..effects import all_options

# get the name of all .json files in this folder
json_files = [
    f.replace(".json", "") for f in listdir(__path__[0]) if isfile(join(__path__[0], f)) and f.endswith(".json")
]
unrealsdk.Log(json_files)
settings_json_path = join(__path__[0], "..", "settings.json")
presets_path = __path__[0]


def _preset_changed(option: Options.Value, new_value):
    unrealsdk.Log(f"{option.Caption} changed to {new_value}")
    if option.CurrentValue == "Custom":  # Save the users Custom preset
        with open(settings_json_path, "r") as f:
            settings = json.load(f)  # Get the old settings
            with open(os.path.join(presets_path,  "Custom.json"), "w") as out:
                json.dump(settings, out, indent=4)  # write them to the preset Custom.json file
    with open(os.path.join(presets_path, f"{new_value}.json"), "r") as f:
        settings = json.load(f)
        with open(settings_json_path, "w") as out:
            json.dump(settings, out, indent=4)

        def _callback_rec(option: Options.Value, new_value):
            if isinstance(option, Options.Value):
                option.CurrentValue = new_value
                option.Callback(option, new_value)
            elif isinstance(option, Options.Nested):
                for child in option.Children:
                    _callback_rec(child, new_value[child.Caption])
        for option in all_options:
            _callback_rec(option, settings["Options"][option.Caption])


_presets_spinner = Options.Spinner(
    Caption="Preset", Description="Select a preset to load", StartingValue="Custom", Choices=json_files
)
_presets_spinner.Callback = _preset_changed

presets = [_presets_spinner]
PresetsOptions = Options.Nested(Caption="Presets", Description="Various Presets", Children=presets)
