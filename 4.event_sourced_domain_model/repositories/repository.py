from domain.event import Event
from domain.i_repository import IRepository
from domain.ticket import Ticket


class Repository(IRepository):
    def __init__(self) -> None:
        self.__events = []

    def load_events(self, id: int) -> list[Event]:
        return [event for event in self.__events if event.id == id]

    def commit(self, ticket: Ticket) -> None:
        self.__events.extend(ticket.events)
