class Player:
    def __init__(
            self,
            name: str,
            position: str,
            price: float,
            value: float
    ):
        self.name = name
        self.position = position
        self.price = price
        self.value = value

    def __str__(self):
        return f"({self.name}, {self.position}, {self.price}, {self.value})"

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        if pos not in ["GK", "DEF", "MID", "ATT"]:
            raise ValueError("Sorry, that's not a valid position")
        self._position = pos
