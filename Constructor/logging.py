from unrealsdk import *
import unrealsdk


class Logger:
    def __init__(self, level, log_calls):
        self.level = level
        self.log_calls = log_calls
        self.levels = ["verbose", "debug", "info", "error"]

    def verbose(self, log):
        if self.level != self.levels[0]:
            return
        unrealsdk.Log(f"[VERBOSE] {log}")

    def debug(self, log):
        if self.level not in self.levels[:2]:
            return
        unrealsdk.Log(f"[DEBUG] {log}")

    def info(self, log):
        if self.level not in self.levels[:3]:
            return
        unrealsdk.Log(f"[INFO] {log}")

    def error(self, log):
        if self.level not in self.levels:
            return
        unrealsdk.Log(f"[ERROR] {log}")

    def custom(self, log, level):
        level_indx = self.levels.index(level)
        if self.level not in self.levels[:level_indx + 1]:
            return
        unrealsdk.Log(log)


logger = None  # type: Logger


def call_logger(func):
    def wrapper(*args, **kwargs):
        if not logger.log_calls:
            return func(*args, **kwargs)

        _cls = args[0].__class__.__name__
        logger.custom(f"*** Called: {_cls}.{func.__name__} ***", "debug")
        res = func(*args, **kwargs)
        logger.custom(f"*** End function  ***", "debug")
        return res

    return wrapper


def log_all_calls(decorator):
    def decorate(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                setattr(cls, name, decorator(obj))
        return cls

    return decorate
