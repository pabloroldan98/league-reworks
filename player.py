
class Player:
    def __init__(
            self,
            name: str,
            position: str,
            price: float,
            value: float,
            country: str,
            status: str,
            price_trend: float,
            fitness: list
    ):
        self.name = name
        self.position = position
        self.price = price
        self.value = value
        self.country = country
        self.status = status
        self.price_trend = price_trend
        self.fitness = fitness

    def __str__(self):
        return f"({self.name}, {self.position}, {self.price}, {self.value}, {self.country})"

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        if pos not in ["GK", "DEF", "MID", "ATT"]:
            raise ValueError("Sorry, that's not a valid position")
        self._position = pos

    def get_group(self):
        if self.position == "GK":
            group = 1
        elif self.position == "DEF":
            group = 2
        elif self.position == "MID":
            group = 3
        else:
            group = 4
        return group


def get_position(group):
    if group == 1:
        position = "GK"
    elif group == 2:
        position = "DEF"
    elif group == 3:
        position = "MID"
    else:
        position = "ATT"
    return position
