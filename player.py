import copy

import numpy as np
from unidecode import unidecode


class Player:
    def __init__(
            self,
            name: str,
            position: str = "GK",
            price: int = 100000,
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

    def calc_value(self, no_form=False, no_fixtures=False):
        form_coef = (self.standard_price + self.price_trend) / self.standard_price
        elo_coef = self.next_match_elo_dif * 0.0002 + 1  # * 0.1/500 + 1
        if no_form:
            form_coef = 1
        if no_fixtures:
            elo_coef = 1

        predicted_value = ((float(self.sofascore_rating) * float(form_coef)) + float(self.penalty_boost) + float(self.strategy_boost)) * float(elo_coef)
        return predicted_value

    def set_value(self, no_form=False, no_fixtures=False):
        predicted_value = self.calc_value(no_form, no_fixtures)
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


def purge_everything(players_list, nations_to_purge=[]):
    purged_players = purge_injured_players(players_list)
    repurged_players = purge_no_country_players(purged_players)
    rerepurged_players = purge_non_starting_players(repurged_players)
    rererepurged_players = purge_negative_values(rerepurged_players)
    solution = purge_national_teams(rererepurged_players, nations_to_purge)

    return solution


def purge_injured_players(players_list):
    result_players = [player for player in players_list if
                      player.status == "ok"]
    return result_players


def purge_no_country_players(players_list):
    result_players = [player for player in players_list if
                      player.country != "None"]
    return result_players


def purge_non_starting_players(players_list):
    result_players = [player for player in players_list if
                      isinstance(player.fitness[0], int) or isinstance(player.fitness[1], int)]
    return result_players


def purge_negative_values(players_list):
    result_players = [player for player in players_list if
                      player.value > 0]
    return result_players


def purge_national_teams(players_list, nations_to_purge):
    result_players = [player for player in players_list if
                      player.country not in nations_to_purge]
    return result_players


def set_manual_boosts(players_list, manual_boosts):
    result_players = copy.deepcopy(players_list)
    for boosted_player in manual_boosts:
        for player in result_players:
            if boosted_player == player:
                player.penalty_boost = boosted_player.penalty_boost
                player.strategy_boost = boosted_player.strategy_boost
                break
    return result_players


def set_players_elo_dif(players_list, teams_list):
    result_players = copy.deepcopy(players_list)
    clean_players = purge_no_country_players(result_players)
    checked_teams = check_teams(clean_players, teams_list)
    if len(checked_teams) != len(teams_list):
        print("The following teams do NOT match your Databases:")
        for team in teams_list:
            if team.name not in checked_teams:
                print(team.name)
        return checked_teams

    teams_dict = {team.name: team for team in teams_list}

    for player in clean_players:
        player_team = teams_dict[player.country]
        opponent_team = teams_dict[player_team.next_opponent]
        elo_dif = player_team.elo - opponent_team.elo
        player.next_match_elo_dif = elo_dif
    return clean_players


def check_teams(players_list, teams_list):
    count = dict()
    for player in players_list:
        for team in teams_list:
            if player.country == team.name:
                count[player.country] = player.country
    return count


def set_players_sofascore_rating(players_list, players_ratings_list):
    result_players = copy.deepcopy(players_list)
    for rated_players in players_ratings_list:
        for player in result_players:
            if rated_players == player:
                player.sofascore_rating = rated_players.sofascore_rating
                break
    return result_players


def set_players_value(players_list, no_form=False, no_fixtures=False):
    result_players = copy.deepcopy(players_list)
    for player in result_players:
        player.set_value(no_form, no_fixtures)
    return result_players


def set_players_value_to_last_fitness(players_list):
    purged_list = purge_non_starting_players(players_list)
    for player in purged_list:
        if player.fitnesss[0] is None:
            player.value = float(player.fitness[1])
        else:
            player.value = float(player.fitness[0])
    repurged_list = purge_negative_values(purged_list)
    return repurged_list


def set_players_value_to_last_fitness(players_list):
    purged_list = purge_non_starting_players(players_list)
    for player in purged_list:
        if player.fitnesss[0] is None:
            player.value = float(player.fitness[1])
        else:
            player.value = float(player.fitness[0])
    repurged_list = purge_negative_values(purged_list)
    return repurged_list


