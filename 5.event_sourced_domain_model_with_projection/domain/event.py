from abc import ABC


class Event(ABC):
    def __init__(self, id: int) -> None:
        self.__id = id

    @property
    def id(self) -> int:
        return self.__id
