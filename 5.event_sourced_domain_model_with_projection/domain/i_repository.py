from abc import ABC, abstractmethod

from domain.event import Event
from domain.ticket import Ticket


class IRepository(ABC):
    @abstractmethod
    def load_events(self, id: int) -> list[Event]:
        pass

    @abstractmethod
    def commit(self, ticket: Ticket) -> None:
        pass
