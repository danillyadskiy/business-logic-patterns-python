from domain.event import Event
from domain.ticket_state import TicketState

from domain.events.ticket_opened import TicketOpened
from domain.events.ticket_initialized import TicketInitialized
from domain.events.ticket_description_added import TicketDescriptionAdded
from domain.events.ticket_closed import TicketClosed
from domain.events.ticket_reopened import TicketReopened


class Ticket:
    def __init__(self, events: list[Event]) -> None:
        self.__state = TicketState()
        self.__events = []
        self.__add_events(events)

    @property
    def state(self):
        return self.__state

    @property
    def events(self):
        return self.__events

    def initialize(self, id: int) -> None:
        event = TicketInitialized(id)
        self.__add_event(event)

    def open(self) -> None:
        event = TicketOpened(self.__state.id)
        self.__add_event(event)

    def add_description(self, description: str) -> None:
        event = TicketDescriptionAdded(self.__state.id, description)
        self.__add_event(event)

    def close(self) -> None:
        event = TicketClosed(self.__state.id)
        self.__add_event(event)

    def reopen(self) -> None:
        event = TicketReopened(self.__state.id)
        self.__add_event(event)

    def __add_events(self, events: list[Event]) -> None:
        for event in events:
            self.__add_event(event)

    def __add_event(self, event: Event) -> None:
        self.__events.append(event)
        self.__state.apply(event)
