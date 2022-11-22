from biwenger import get_worldcup_data
from group_knapsack import best_full_teams
from player import Player
from OLD_group_knapsack import best_squads, best_teams

playersDB = [
    Player("Mendy", "GK", 20, 6.8, "SEN", "ok", 0, []),
    Player("Matt Turner", "GK", 11, 7.4, "USA", "ok", 0, []),
    Player("Szczesny", "GK", 19, 7.4, "POL", "ok", 0, []),
    Player("Schmeichel", "GK", 12, 7.2, "DIN", "ok", 0, []),
    Player("Keylor Navas", "GK", 16, 7.5, "COS", "ok", 0, []),
    Player("Neuer", "GK", 22, 7.5, "ALE", "ok", 0, []),
    Player("Livakovic", "GK", 17, 7.3, "CRO", "ok", 0, []),
    Player("Allison", "GK", 27, 7.4, "BRA", "ok", 0, []),
    Player("Onana", "GK", 16, 7.1, "CAM", "ok", 0, []),

    Player("Blind", "DEF", 20, 7, "HOL", "ok", 0, []),
    Player("Van Dijk", "DEF", 31, 7.1, "HOL", "ok", 0, []),
    Player("Shaw", "DEF", 21, 7.2, "ING", "ok", 0, []),
    Player("Stones", "DEF", 25, 7.1, "ING", "ok", 0, []),
    Player("Otamendi", "DEF", 20, 7.3, "ARG", "ok", 0, []),
    Player("Rubén Días", "DEF", 31, 7.1, "POR", "ok", 0, []),
    Player("Laporte", "DEF", 23, 7.2, "ESP", "ok", 0, []),
    Player("Mahele", "DEF", 21, 6.5, "DIN", "ok", 0, []),
    Player("Nuno", "DEF", 24, 7.1, "POR", "ok", 0, []),

    Player("Caicedo", "MID", 19, 7.1, "ECU", "ok", 0, []),
    Player("De Jong", "MID", 44, 7.3, "HOL", "ok", 0, []),
    Player("Bellingham", "MID", 32, 7.5, "ING", "ok", 0, []),
    Player("Foden", "MID", 37, 7.2, "ING", "ok", 0, []),
    Player("De Paul", "MID", 27, 7.4, "ARG", "ok", 0, []),
    Player("Eriksen", "MID", 25, 7.5, "DIN", "ok", 0, []),
    Player("De Bruyne", "MID", 38, 8, "BEL", "ok", 0, []),
    Player("Tielemans", "MID", 24, 7.3, "BEL", "ok", 0, []),
    Player("Modric", "MID", 22, 7.2, "CRO", "ok", 0, []),
    Player("Perisic", "MID", 25, 6.9, "CRO", "ok", 0, []),
    Player("Bruno Fernandes", "MID", 37, 7.8, "POR", "ok", 0, []),
    Player("Pedri", "MID", 31, 7.6, "ESP", "ok", 0, []),
    Player("Busquets", "MID", 21, 7.1, "ESP", "ok", 0, []),
    Player("Havertz", "MID", 30, 6.9, "ALE", "ok", 0, []),
    Player("Kimmich", "MID", 38, 7.6, "ALE", "ok", 0, []),
    Player("Gundogan", "MID", 28, 7.1, "ALE", "ok", 0, []),
    Player("Hojbjerg", "MID", 29, 6.8, "DIN", "ok", 0, []),
    Player("Valverde", "MID", 29, 7.8, "URU", "ok", 0, []),
    Player("Gueye", "MID", 19, 7, "SEN", "ok", 0, []),

    Player("Mbappe", "ATT", 75, 7.5, "FRA", "ok", 0, []),
    #    Player("Lewandowsik", "ATT", 51, 0, "POL", "ok", 0, []),
    Player("Messi", "ATT", 51, 8.2, "ARG", "ok", 0, []),
    Player("Kane", "ATT", 50, 7.7, "ING", "ok", 0, []),
    Player("Neymar", "ATT", 50, 7.5, "BRA", "ok", 0, []),
    #    Player("Depay", "ATT", 46, 0, "HOL", "ok", 0, []),
    #    Player("Benzema", "ATT", 41, 0, "FRA", "ok", 0, []),
    #    Player("Lukaku", "ATT", 40, 0, "BEL", "ok", 0, []),
    #    Player("Lautaro", "ATT", 40, 0, "ARG", "ok", 0, []),
    #    Player("Vlahovic", "ATT", 36, 0, "SER", "ok", 0, []),
    #    Player("Sterling", "ATT", 34, 0, "ING", "ok", 0, []),
    #    Player("Dani Olmo", "ATT", 34, 0, "ESP", "ok", 0, []),
    #    Player("Jonathan David", "ATT", 33, 0, "CAN", "ok", 0, []),
    Player("Gakpo", "ATT", 33, 7.4, "HOL", "ok", 0, []),
    Player("Griezmann", "ATT", 31, 7.7, "FRA", "ok", 0, []),
    #    Player("Morata", "ATT", 31, 0, "ESP", "ok", 0, []),
    #    Player("CR7", "ATT", 31, 0, "POR", "ok", 0, []),
    Player("Raphinha", "ATT", 31, 7.4, "BRA", "ok", 0, []),
    Player("Di María", "ATT", 22, 7.4, "ARG", "ok", 0, []),
    Player("Luis Suárez", "ATT", 22, 6.8, "URU", "ok", 0, []),
    Player("Valencia", "ATT", 16, 7.3, "ECU", "ok", 0, []),

]

possible_formations = [
    [3, 4, 3],
    [3, 5, 2],
    [4, 3, 3],
    [4, 4, 2],
    [4, 5, 1],
    [5, 3, 2],
    [5, 4, 1],
]


all_teams, all_players = get_worldcup_data()

best_full_teams(playersDB, possible_formations, 300)


# best_teams(playerDB, possible_formations, 300)

# best_squads(playerDB, possible_formations, 300)


# newlist = sorted(playerDB, key=lambda x: x.value/x.price, reverse=True)
# for player in newlist:
#     print(player)

# newlist = sorted(playerDB, key=lambda x: x.get_group())
# for player in newlist:
#     print(player)
#
#
# attrs = [o.name for o in playerDB]
#
# for playerName in attrs:
#     print(playerName)




