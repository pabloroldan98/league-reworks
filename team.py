from unidecode import unidecode


class Team:
    def __init__(
            self,
            name: str,
            next_opponent: str,
            elo: float
    ):
        self.name = name
        self.next_opponent = next_opponent
        self.elo = elo

    def __str__(self):
        return f"({self.name}, {self.elo})"

    def __eq__(self, other_player):
        if unidecode(self.name).lower() in unidecode(other_player.name).lower() \
                or unidecode(other_player.name).lower() in unidecode(self.name).lower():
            return True
        else:
            return False
