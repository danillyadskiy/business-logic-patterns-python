class Database:
    def start_transaction(self) -> None:
        pass

    def load(self) -> str:
        return "Ticket"

    def close(self, ticket: str) -> None:
        pass

    def commit(self) -> None:
        pass
