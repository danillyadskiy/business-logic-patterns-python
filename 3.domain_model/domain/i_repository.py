from abc import ABC, abstractmethod
from domain.ticket import Ticket


class IRepository(ABC):
    @abstractmethod
    def load(self, id: int) -> Ticket:
        pass

    @abstractmethod
    def save(self, ticket: Ticket) -> None:
        pass
