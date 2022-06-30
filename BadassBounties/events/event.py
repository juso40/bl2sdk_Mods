from abc import ABC, abstractmethod


class Event(ABC):
    """Base class for events"""

    def __init__(self):
        """

        :rtype: object
        """
        self._handlers = []

    def add(self, handler) -> None:
        self._handlers.append(handler)

    def remove(self, handler) -> None:
        try:
            self._handlers.remove(handler)
        except ValueError:
            pass

    @abstractmethod
    def register_hooks(self):
        pass

    @abstractmethod
    def remove_hooks(self):
        pass
