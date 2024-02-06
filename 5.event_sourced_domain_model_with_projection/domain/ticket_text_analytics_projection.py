from domain.event import Event

from domain.events.ticket_opened import TicketOpened
from domain.events.ticket_initialized import TicketInitialized
from domain.events.ticket_description_added import TicketDescriptionAdded
from domain.events.ticket_closed import TicketClosed
from domain.events.ticket_reopened import TicketReopened


class TicketTextAnalyticsProjection:
    def __init__(self, events: list[Event]) -> None:
        self.__id = 0
        self.__version = 0
        self.__texts = []

        for event in events:
            self.__apply(event)


    @property
    def id(self) -> int:
        return self.__id

    @property
    def version(self) -> int:
        return self.__version

    @property
    def texts(self) -> list[str]:
        return self.__texts

    def __initialize(self, event: TicketInitialized) -> None:
        self.__id = event.id
        self.__version = 0

    def __open(self, event: TicketOpened) -> None:
        self.__version += 1

    def __add_description(self, event: TicketDescriptionAdded) -> None:
        self.__texts.append(event.description)
        self.__version += 1

    def __close(self, event: TicketClosed) -> None:
        self.__version += 1

    def __reopen(self, event: TicketReopened) -> None:
        self.__version += 1

    def __apply(self, event: Event) -> None:
        if type(event) == TicketInitialized:
            self.__initialize(event)
        elif type(event) == TicketOpened:
            self.__open(event)
        elif type(event) == TicketDescriptionAdded:
            self.__add_description(event)
        elif type(event) == TicketClosed:
            self.__close(event)
        elif type(event) == TicketReopened:
            self.__reopen(event)
        else:
            raise Exception("Invalid event", event)



