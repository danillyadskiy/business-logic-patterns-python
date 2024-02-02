from domain.i_repository import IRepository
from domain.ticket import Ticket


class Repository(IRepository):
    def __init__(self) -> None:
        self.__tickets = []

    def load(self, id: int) -> Ticket:
        return [ticket for ticket in self.__tickets if ticket.id == id][0]

    def save(self, ticket: Ticket) -> None:
        self.__tickets.append(ticket)
