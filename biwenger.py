# Source: https://stackoverflow.com/questions/59444927/html-request-for-biwenger-in-python

import re
import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup

from player import Player, get_position
from team import Team


def get_worldcup_data():

    all_data_url = 'https://cf.biwenger.com/api/v2/competitions/world-cup/data?lang=en&score=1&callback=jsonp_xxx'

    response = requests.get(all_data_url)
    data = json.loads(re.findall(r'jsonp_xxx\((.*)\)', response.text)[0])

    worldcup_teams = get_teams_worldcup_data(data)
    worldcup_players = get_players_worldcup_data(data)

    return worldcup_teams, worldcup_players


def get_teams_worldcup_data(data):

    worldcup_teams_db = []
    worldcup_teams = data['data']['teams']
    for worldcup_team_id in worldcup_teams:
        worldcup_team = worldcup_teams[str(worldcup_team_id)]

        team_name = worldcup_team["name"]
        team_next_opponent = get_next_opponent(worldcup_team_id, worldcup_teams)
        team_elo = 0

        new_team = Team(
            team_name,
            team_next_opponent,
            team_elo
        )
        worldcup_teams_db.append(new_team)

    return worldcup_teams_db


def get_next_opponent(team_id, teams):
    my_team = teams[str(team_id)]

    next_team_home_id = my_team["nextGames"][0]["home"]["id"]
    next_team_away_id = my_team["nextGames"][0]["away"]["id"]

    if team_id != next_team_home_id:
        next_team = teams[str(next_team_home_id)]
    else:
        next_team = teams[str(next_team_away_id)]

    return next_team


def get_players_worldcup_data(data):

    worldcup_players_db = []
    worldcup_teams = data['data']['teams']
    worldcup_players = data['data']['players']
    for worldcup_player_id in worldcup_players:
        worldcup_player = worldcup_players[str(worldcup_player_id)]

        pprint(worldcup_player)
        player_name = worldcup_player["name"]
        player_group = worldcup_player["position"]
        player_price = worldcup_player["fantasyPrice"]/1000000
        player_status = worldcup_player["status"]
        player_price_trend = worldcup_player["priceIncrement"]
        player_fitness = worldcup_player["fitness"]

        player_team_id = str(worldcup_player["teamID"])
        if player_team_id == "None":
            player_team = "None"
        else:
            player_team = worldcup_teams[player_team_id]["name"]

        new_player = Player(
            player_name,
            get_position(player_group),
            player_price,
            0,
            player_team,
            player_status,
            player_price_trend,
            player_fitness
        )
        worldcup_players_db.append(new_player)

    return worldcup_players_db

# user_data_url = 'https://biwenger.as.com/api/v2/user/16728?fields=*,account(id),players(id,owner),lineups(round,points,count,position),league(id,name,competition,mode,scoreID),market,seasons,offers,lastPositions'
# all_data_url = 'https://cf.biwenger.com/api/v2/competitions/world-cup/data?lang=en&score=1&callback=jsonp_xxx' # <--- check @αԋɱҽԃ αмєяιcαη answer, it's possible to do it without callback= parameter
#
# response = requests.get(all_data_url)
# data = json.loads( re.findall(r'jsonp_xxx\((.*)\)', response.text)[0] )

# user_data = requests.get(user_data_url).json()

# pprint(user_data)  # <-- uncomment this to see user data
# pprint(data)       # <-- uncomment this to see data about all players
#
# pprint(data["data"]["players"])

# for teams in data['data']['teams']:
#     pprint(data['data']['teams'][str(teams)])
#     print('-' * 80)
