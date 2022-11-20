class Player:
    def __init__(
            self,
            name: str,
            position: str,
            price: float,
            value: float,
            country: str
    ):
        self.name = name
        self.position = position
        self.price = price
        self.value = value
        self.country = country

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
            group = 0
        elif self.position == "DEF":
            group = 1
        elif self.position == "MID":
            group = 2
        else:
            group = 3
        return group
