from datetime import datetime

from repositories.repository import Repository
from domain.ticket import Ticket
from domain.ticket_text_analytics_projection import TicketTextAnalyticsProjection

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
        projection = TicketTextAnalyticsProjection(repository_events)

        print(f"ticket-id: {projection.id}")
        print(f"version: {projection.version}")

        for i, text in enumerate(projection.texts):
            print(f"text {i + 1}: {text}")


client = Client()
client.execute()
