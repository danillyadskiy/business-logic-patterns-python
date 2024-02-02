from repositories.repository import Repository
from domain.ticket import Ticket


class Client:
    def __init__(self) -> None:
        self.__repository = Repository()

    def execute(self) -> None:
        ticket_id = 1

        # Begin transaction

        # Do some logic with ticket
        ticket = Ticket()
        ticket.initialize(ticket_id)
        ticket.open()
        ticket.add_description("Some description 1")
        ticket.close()
        ticket.reopen()
        ticket.add_description("Some description 2")
        ticket.close()

        # Finish transaction
        self.__repository.save(ticket)

        # Show results
        repository_ticket = self.__repository.load(ticket_id)

        print(f"ticket-id: {repository_ticket.id}")
        print(f"ticket-version: {repository_ticket.version}")
        print(f"ticket-is-open: {repository_ticket.is_open}")
        print(f"ticket-description: {repository_ticket.description}")


client = Client()
client.execute()
