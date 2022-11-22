from group_knapsack import best_full_teams
from player import Player
from OLD_group_knapsack import best_squads, best_teams

playerDB = [
    Player("Mendy", "GK", 20, 6.8, "SEN"),
    Player("Matt Turner", "GK", 11, 7.4, "USA"),
    Player("Szczesny", "GK", 19, 7.4, "POL"),
    Player("Schmeichel", "GK", 12, 7.2, "DIN"),
    Player("Keylor Navas", "GK", 16, 7.5, "COS"),
    Player("Neuer", "GK", 22, 7.5, "ALE"),
    Player("Livakovic", "GK", 17, 7.3, "CRO"),
    Player("Allison", "GK", 27, 7.4, "BRA"),
    Player("Onana", "GK", 16, 7.1, "CAM"),

    Player("Blind", "DEF", 20, 7, "HOL"),
    Player("Van Dijk", "DEF", 31, 7.1, "HOL"),
    Player("Shaw", "DEF", 21, 7.2, "ING"),
    Player("Stones", "DEF", 25, 7.1, "ING"),
    Player("Otamendi", "DEF", 20, 7.3, "ARG"),
    Player("Rubén Días", "DEF", 31, 7.1, "POR"),
    Player("Laporte", "DEF", 23, 7.2, "ESP"),
    Player("Mahele", "DEF", 21, 6.5, "DIN"),
    Player("Nuno", "DEF", 24, 7.1, "POR"),

    Player("Caicedo", "MID", 19, 7.1, "ECU"),
    Player("De Jong", "MID", 44, 7.3, "HOL"),
    Player("Bellingham", "MID", 32, 7.5, "ING"),
    Player("Foden", "MID", 37, 7.2, "ING"),
    Player("De Paul", "MID", 27, 7.4, "ARG"),
    Player("Eriksen", "MID", 25, 7.5, "DIN"),
    Player("De Bruyne", "MID", 38, 8, "BEL"),
    Player("Tielemans", "MID", 24, 7.3, "BEL"),
    Player("Modric", "MID", 22, 7.2, "CRO"),
    Player("Perisic", "MID", 25, 6.9, "CRO"),
    Player("Bruno Fernandes", "MID", 37, 7.8, "POR"),
    Player("Pedri", "MID", 31, 7.6, "ESP"),
    Player("Busquets", "MID", 21, 7.1, "ESP"),
    Player("Havertz", "MID", 30, 6.9, "ALE"),
    Player("Kimmich", "MID", 38, 7.6, "ALE"),
    Player("Gundogan", "MID", 28, 7.1, "ALE"),
    Player("Hojbjerg", "MID", 29, 6.8, "DIN"),
    Player("Valverde", "MID", 29, 7.8, "URU"),
    Player("Gueye", "MID", 19, 7, "SEN"),

    Player("Mbappe", "ATT", 75, 7.5, "FRA"),
    #    Player("Lewandowsik", "ATT", 51, 0, "POL"),
    Player("Messi", "ATT", 51, 8.2, "ARG"),
    Player("Kane", "ATT", 50, 7.7, "ING"),
    Player("Neymar", "ATT", 50, 7.5, "BRA"),
    #    Player("Depay", "ATT", 46, 0, "HOL"),
    #    Player("Benzema", "ATT", 41, 0, "FRA"),
    #    Player("Lukaku", "ATT", 40, 0, "BEL"),
    #    Player("Lautaro", "ATT", 40, 0, "ARG"),
    #    Player("Vlahovic", "ATT", 36, 0, "SER"),
    #    Player("Sterling", "ATT", 34, 0, "ING"),
    #    Player("Dani Olmo", "ATT", 34, 0, "ESP"),
    #    Player("Jonathan David", "ATT", 33, 0, "CAN"),
    Player("Gakpo", "ATT", 33, 7.4, "HOL"),
    Player("Griezmann", "ATT", 31, 7.7, "FRA"),
    #    Player("Morata", "ATT", 31, 0, "ESP"),
    #    Player("CR7", "ATT", 31, 0, "POR"),
    Player("Raphinha", "ATT", 31, 7.4, "BRA"),
    Player("Di María", "ATT", 22, 7.4, "ARG"),
    Player("Luis Suárez", "ATT", 22, 6.8, "URU"),
    Player("Valencia", "ATT", 16, 7.3, "ECU"),

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


best_full_teams(playerDB, possible_formations, 300)


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




