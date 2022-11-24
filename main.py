
# Look at: https://stackoverflow.com/questions/74503207/knapsack-with-specific-amount-of-items-from-different-groups

from biwenger import get_worldcup_data
from group_knapsack import best_full_teams, best_transfers
from player import Player
from OLD_group_knapsack import best_squads, best_teams

playersDB = [
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
    Player("Lewandowsik", "ATT", 51, 0, "POL"),
    Player("Messi", "ATT", 51, 8.2, "ARG"),
    Player("Kane", "ATT", 50, 7.7, "ING"),
    Player("Neymar", "ATT", 50, 7.5, "BRA"),
    Player("Depay", "ATT", 46, 0, "HOL"),
    Player("Benzema", "ATT", 41, 0, "FRA"),
    Player("Lukaku", "ATT", 40, 0, "BEL"),
    Player("Lautaro", "ATT", 40, 0, "ARG"),
    Player("Vlahovic", "ATT", 36, 0, "SER"),
    Player("Sterling", "ATT", 34, 0, "ING"),
    Player("Dani Olmo", "ATT", 34, 0, "ESP"),
    Player("Jonathan David", "ATT", 33, 0, "CAN"),
    Player("Gakpo", "ATT", 33, 7.4, "HOL"),
    Player("Griezmann", "ATT", 31, 7.7, "FRA"),
    Player("Morata", "ATT", 31, 0, "ESP"),
    Player("CR7", "ATT", 31, 0, "POR"),
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

my_team = [
    Player("Matt Turner", "GK", 11, 7.4, "USA"),

    Player("Blind", "DEF", 20, 7, "HOL"),
    Player("Shaw", "DEF", 21, 7.2, "ING"),
    Player("Otamendi", "DEF", 20, 7.3, "ARG"),

    Player("Caicedo", "MID", 19, 7.1, "ECU"),
    Player("De Bruyne", "MID", 38, 8, "BEL"),
    Player("Bruno Fernandes", "MID", 37, 7.8, "POR"),
    Player("Valverde", "MID", 29, 7.8, "URU"),

    Player("Messi", "ATT", 51, 8.2, "ARG"),
    Player("Griezmann", "ATT", 31, 7.7, "FRA"),
    Player("Di María", "ATT", 22, 7.4, "ARG"),
]

players_manual_boosts = [
    Player("Al-Haydos", penalty_boost=0.7, strategy_boost=0.1),
    Player("Afif", penalty_boost=0, strategy_boost=0.1),

    Player("Enner Valencia", penalty_boost=0.7, strategy_boost=0),
    Player("Estupiñán", penalty_boost=0, strategy_boost=0.1),
    Player("Ángel Mena", penalty_boost=0, strategy_boost=0.1),

    Player("Depay", penalty_boost=0.7, strategy_boost=0.1),
    Player("Berghuis", penalty_boost=0, strategy_boost=0.1),

    Player("Sadio Mane", penalty_boost=0.7, strategy_boost=0.1),
    Player("Boulaye Dia", penalty_boost=0.35, strategy_boost=0),
    Player("Ismaila Sarr", penalty_boost=0.35, strategy_boost=0),
    Player("Idrissa Gueye", penalty_boost=0, strategy_boost=0.1),

    Player("Harry Kane", penalty_boost=0.7, strategy_boost=0),
    Player("Arnold", penalty_boost=0, strategy_boost=0.1),
    Player("Trippier", penalty_boost=0, strategy_boost=0.1),

    Player("Gareth Bale", penalty_boost=0.7, strategy_boost=0.1),
    Player("Harry Wilson", penalty_boost=0, strategy_boost=0.1),

    Player("Pulisic", penalty_boost=0.7, strategy_boost=0.1),
    Player("Reyna", penalty_boost=0, strategy_boost=0.1),

    Player("Taremi", penalty_boost=0.7, strategy_boost=0),
    Player("Sholizadeh", penalty_boost=0, strategy_boost=0.1),
    Player("Jahanbaksh", penalty_boost=0, strategy_boost=0.1),

    Player("Messi", penalty_boost=0.7, strategy_boost=0.1),
    Player("Di María", penalty_boost=0, strategy_boost=0.1),

    Player("Lewandowski", penalty_boost=0.7, strategy_boost=0.1),
    Player("Zielinski", penalty_boost=0, strategy_boost=0.1),

    Player("Al-Faraj", penalty_boost=0.7, strategy_boost=0.1),
    Player("Al-Dawsari", penalty_boost=0, strategy_boost=0.1),

    Player("Raúl Jiménez", penalty_boost=0.7, strategy_boost=0),
    Player("Héctor Herrera", penalty_boost=0, strategy_boost=0.1),
    Player("Guardado", penalty_boost=0, strategy_boost=0.1),

    Player("Mbappe", penalty_boost=0.7, strategy_boost=0),
    Player("Griezmann", penalty_boost=0, strategy_boost=0.1),
    Player("Theo Hernández", penalty_boost=0, strategy_boost=0.1),

    Player("Jamie Maclaren", penalty_boost=0.7, strategy_boost=0),
    Player("Aaron Moy", penalty_boost=0, strategy_boost=0.1),
    Player("Hrustic", penalty_boost=0, strategy_boost=0.1),

    Player("Eriksen", penalty_boost=0.7, strategy_boost=0.1),
    Player("Braithwaite", penalty_boost=0, strategy_boost=0.1),

    Player("Khazri", penalty_boost=0.7, strategy_boost=0.1),
    Player("Laïdouni", penalty_boost=0, strategy_boost=0.1),

    Player("Morata", penalty_boost=0.7, strategy_boost=0),
    Player("Ferrán Torres", penalty_boost=0.4, strategy_boost=0),
    Player("Pablo Sarabia", penalty_boost=0, strategy_boost=0.1),
    Player("Koke", penalty_boost=0, strategy_boost=0.1),

    Player("Celso Borges", penalty_boost=0.7, strategy_boost=0.1),
    Player("Joel Campbell", penalty_boost=0, strategy_boost=0.1),

    Player("Gundogan", penalty_boost=0.7, strategy_boost=0.1),
    Player("Kimmich", penalty_boost=0, strategy_boost=0.1),

    Player("Lukaku", penalty_boost=0.7, strategy_boost=0),
    Player("Eden Hazard", penalty_boost=0.5, strategy_boost=0),
    Player("De Bruyne", penalty_boost=0, strategy_boost=0.1),
    Player("Carrasco", penalty_boost=0, strategy_boost=0.1),

    Player("Cyle Larin", penalty_boost=0.7, strategy_boost=0),
    Player("Alphonso Davies", penalty_boost=0.4, strategy_boost=0.1),
    Player("Eustáquio", penalty_boost=0, strategy_boost=0.1),

    Player("Modric", penalty_boost=0.7, strategy_boost=0.1),
    Player("Brozovic", penalty_boost=0, strategy_boost=0.1),

    Player("Boufal", penalty_boost=0.7, strategy_boost=0),
    Player("Ziyech", penalty_boost=0.35, strategy_boost=0.1),
    Player("Achraf Hakimi", penalty_boost=0, strategy_boost=0.1),

    Player("Neymar", penalty_boost=0.7, strategy_boost=0.1),
    Player("Casemiro", penalty_boost=0, strategy_boost=0.1),
    Player("Raphinha", penalty_boost=0, strategy_boost=0.1),

    Player("Ricardo Rodríguez", penalty_boost=0.7, strategy_boost=0.1),
    Player("Shaquiri", penalty_boost=0, strategy_boost=0.1),

    Player("Aboubakar", penalty_boost=0.7, strategy_boost=0),
    Player("Ngamaleu", penalty_boost=0.3, strategy_boost=0.1),
    Player("Ekambi", penalty_boost=0, strategy_boost=0.1),
    Player("Choupo-Moting", penalty_boost=0.3, strategy_boost=0),

    Player("Tadic", penalty_boost=0.7, strategy_boost=0.05),
    Player("Milinkovic-Savic", penalty_boost=0, strategy_boost=0.1),

    Player("Cristiano Ronaldo", penalty_boost=0.7, strategy_boost=0.1),
    Player("Bernardo Silva", penalty_boost=0, strategy_boost=0.1),
    Player("Bruno Fernandes", penalty_boost=0, strategy_boost=0.1),

    Player("Thomas Partey", penalty_boost=0.2, strategy_boost=0.1),
    Player("Jordan Ayew", penalty_boost=0.2, strategy_boost=0.1),
    Player("Iñaki Williams", penalty_boost=0.2, strategy_boost=0),

    Player("Luis Suárez", penalty_boost=0.7, strategy_boost=0),
    Player("Cavani", penalty_boost=0.5, strategy_boost=0),
    Player("De Arrascaeta", penalty_boost=0, strategy_boost=0.1),
    Player("Fede Valverde", penalty_boost=0, strategy_boost=0.1),

]

# best_transfers(my_team, playersDB, 4, n_results=50)

# all_teams, all_players = get_worldcup_data()
#
# max_elo = all_teams[0].elo
# for team in all_teams:
#     elo_dif = max_elo - team.elo
#     print(team)
#     print(elo_dif)
#
# for player in all_players:
#     print(player)

# best_full_teams(playersDB, possible_formations, 300)


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


