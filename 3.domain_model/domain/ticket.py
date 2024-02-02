class Ticket:
    def __init__(self) -> None:
        self.__id = 0
        self.__version = 0
        self.__is_open = False
        self.__description = ""

    @property
    def id(self) -> int:
        return self.__id

    @property
    def version(self) -> int:
        return self.__version

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @property
    def description(self) -> str:
        return self.__description

    def initialize(self, id: int) -> None:
        self.__id = id
        self.__version = 0

    def open(self) -> None:
        self.__is_open = True
        self.__version += 1

    def add_description(self, description: str) -> None:
        self.__description = description
        self.__version += 1

    def close(self) -> None:
        self.__is_open = False
        self.__version += 1

    def reopen(self) -> None:
        self.__is_open = True
        self.__version += 1
