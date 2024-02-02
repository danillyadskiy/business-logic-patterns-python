from database import Database
from ticket import Ticket


class Client:
    def __init__(self) -> None:
        self.__database = Database()

    def execute(self) -> None:
        ticket_details = {
            "id": 1,
            "version": 0,
            "is_open": False,
        }

        # Begin transaction
        self.__database.start_transaction()

        # Do some logic with ticket
        ticket = Ticket()
        ticket.id = ticket_details["id"]
        ticket.version = ticket_details["version"]
        ticket.is_open = ticket_details["is_open"]
        ticket.save()

        # Finish transaction
        self.__database.commit()

        # Show results
        print(f"ticket-id: {ticket.id}")
        print(f"ticket-version: {ticket.version}")
        print(f"ticket-is-open: {ticket.is_open}")


client = Client()
client.execute()
