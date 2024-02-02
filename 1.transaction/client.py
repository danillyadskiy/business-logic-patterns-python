from database import Database
from file import File


class Client:
    def __init__(self) -> None:
        self.__database = Database()
        self.__file = File()

    def execute(self) -> None:
        # Begin transaction
        self.__database.start_transaction()

        # Do some logic with ticket
        ticket = self.__database.load()
        ticket_info = self.__file.load()

        self.__file.write(ticket_info)
        self.__database.close(ticket)

        # Finish transaction
        self.__database.commit()

        # Show results
        print(f"ticket: {ticket}")
        print(f"ticket-info: {ticket_info}")


client = Client()
client.execute()
