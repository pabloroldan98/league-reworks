
class Team:
    def __init__(
            self,
            name: str,
            next_opponent,
            elo: float
    ):
        self.name = name
        self.next_opponent = next_opponent
        self.elo = elo

    def __str__(self):
        return f"({self.name}, {self.elo})"
