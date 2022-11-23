import pandas as pd


def get_teams_elos():
    teams_elos_url = "https://www.eloratings.net/World.tsv"
    teams_elos_df = pd.read_table(teams_elos_url, sep="\t", header=None, na_filter=False)[[2, 3]]
    teams_elos_dict = dict(teams_elos_df.values)

    teams_alias_url = "https://www.eloratings.net/en.teams.tsv"
    teams_alias_df = pd.read_table(teams_alias_url, sep="\t", header=None, names=range(10), na_filter=False)[[0, 1]]
    teams_alias_dict = dict(teams_alias_df.values)

    full_teams_elos = dict()
    for team_short, team_elo in teams_elos_dict.items():
        team_name = teams_alias_dict[str(team_short)]
        full_teams_elos[str(team_name)] = team_elo

    return full_teams_elos, teams_elos_dict


