from unidecode import unidecode


class Player:
    def __init__(
            self,
            name: str,
            position: str = "GK",
            price: float = 100000,
            value: float = 0,
            country: str = "Spain",
            status: str = "ok",
            standard_price: float = 0,
            price_trend: float = 0,
            fitness: list = [None, None, None, None, None],
            penalty_boost: float = 0,
            strategy_boost: float = 0,
            sofascore_rating: float = 0,
            next_match_elo_dif: float = 0
    ):
        self.name = name
        self.position = position
        self.price = price
        self.value = value
        self.country = country
        self.status = status
        self.standard_price = standard_price
        self.price_trend = price_trend
        self.fitness = fitness
        self.penalty_boost = penalty_boost
        self.strategy_boost = strategy_boost
        self.sofascore_rating = sofascore_rating
        self.next_match_elo_dif = next_match_elo_dif

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

    def has_played_last_match(self):
        if self.fitness[0] is not None:
            return True
        else:
            return False

    def __eq__(self, other_player):
        if unidecode(self.name).lower() in unidecode(other_player.name).lower() \
                or unidecode(other_player.name).lower() in unidecode(self.name).lower():
            return True
        else:
            return False

    def calc_value(self):
        form_coef = (self.standard_price + self.price_trend) / self.standard_price
        elo_coef = self.next_match_elo_dif * 0.0002 + 1  # * 0.1/500 + 1

        predicted_value = ((self.sofascore_rating * form_coef) + self.penalty_boost + self.strategy_boost) * elo_coef
        return predicted_value

    def set_value(self):
        predicted_value = self.calc_value()
        self.value = predicted_value


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

# p1 = Player("Mákĉge")
# p2 = Player("makcge")
#
# print(p1==p2)
