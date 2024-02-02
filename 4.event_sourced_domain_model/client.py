from datetime import datetime

from repositories.repository import Repository
from domain.ticket import Ticket

from domain.events.ticket_opened import TicketOpened
from domain.events.ticket_initialized import TicketInitialized
from domain.events.ticket_description_added import TicketDescriptionAdded
from domain.events.ticket_closed import TicketClosed
from domain.events.ticket_reopened import TicketReopened


class Client:
    def __init__(self) -> None:
        self.__repository = Repository()

    def execute(self) -> None:
        ticket_id = 1

        # Begin transaction
        events = self.__repository.load_events(ticket_id)
        ticket = Ticket(events)

        # Do some logic with ticket
        ticket.initialize(ticket_id)
        ticket.open()
        ticket.add_description("Some description 1")
        ticket.close()
        ticket.reopen()
        ticket.add_description("Some description 2")
        ticket.close()

        # Finish transaction
        self.__repository.commit(ticket)

        # Show results
        repository_events = self.__repository.load_events(ticket_id)
        repository_ticket = Ticket(repository_events)

        for i, event in enumerate(repository_ticket.events):
            if type(event) == TicketInitialized:
                print(f"ticket-id: {event.id}")
                print(f"event-id: {i}")
                print(f"event-type: {type(event).__name__}")
                print(f"timestamp: {datetime.now()}")
                print()
            elif type(event) == TicketOpened:
                print(f"ticket-id: {event.id}")
                print(f"event-id: {i}")
                print(f"event-type: {type(event).__name__}")
                print(f"timestamp: {datetime.now()}")
                print()
            elif type(event) == TicketDescriptionAdded:
                print(f"ticket-id: {event.id}")
                print(f"ticket-description: {event.description}")
                print(f"event-id: {i}")
                print(f"event-type: {type(event).__name__}")
                print(f"timestamp: {datetime.now()}")
                print()
            elif type(event) == TicketClosed:
                print(f"ticket-id: {event.id}")
                print(f"event-id: {i}")
                print(f"event-type: {type(event).__name__}")
                print(f"timestamp: {datetime.now()}")
                print()
            elif type(event) == TicketReopened:
                print(f"ticket-id: {event.id}")
                print(f"event-id: {i}")
                print(f"event-type: {type(event).__name__}")
                print(f"timestamp: {datetime.now()}")
                print()
            else:
                raise Exception("Invalid event", event)


client = Client()
client.execute()
