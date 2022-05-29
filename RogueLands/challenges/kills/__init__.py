from .base import KillChallenge

import importlib
import os

# import all files in this module
for f in os.listdir(os.path.dirname(__file__)):
    if f.endswith(".py") and not f == "__init__.py":
        importlib.import_module(".{}".format(f[:-3]), package=__package__)
