from domain.event import Event


class TicketDescriptionAdded(Event):
    def __init__(self, id: int, description: str) -> None:
        super().__init__(id)

        self.__description = description

    @property
    def description(self) -> str:
        return self.__description
