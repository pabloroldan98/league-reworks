import pandas as pd
import os
from collections import defaultdict


pd.set_option('display.max_rows', 500)  # or None to display all rows
pd.set_option('display.max_columns', 100)  # or None to display all columns



# Columns to keep
columns_to_keep = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']


# List all the elements in the folder
directory = "./data/LaLiga"

files = os.listdir(directory)
# files = ['SP1 (1).csv', 'SP1 (10).csv', 'SP1 (11).csv', 'SP1 (12).csv', 'SP1 (13).csv', 'SP1 (14).csv', 'SP1 (15).csv', 'SP1 (16).csv', 'SP1 (17).csv', 'SP1 (18).csv', 'SP1 (19).csv', 'SP1 (2).csv', 'SP1 (20).csv', 'SP1 (21).csv', 'SP1 (22).csv', 'SP1 (23).csv', 'SP1 (24).csv', 'SP1 (25).csv', 'SP1 (26).csv', 'SP1 (27).csv', 'SP1 (28).csv', 'SP1 (29).csv', 'SP1 (3).csv', 'SP1 (30).csv', 'SP1 (4).csv', 'SP1 (5).csv', 'SP1 (6).csv', 'SP1 (7).csv', 'SP1 (8).csv', 'SP1 (9).csv', 'SP1.csv']


# Empty list to hold dataframes
dfs = []
for file in files:
    # Construct file path
    file_path = os.path.join(directory, file)
    # Read the CSV file
    df = pd.read_csv(file_path, usecols=columns_to_keep)
    # Extract the year from the first row's Date column, and create the "Season" column
    first_date = pd.to_datetime(df.loc[0, 'Date'], dayfirst=True)
    season_year = first_date.year if first_date.month >= 8 else first_date.year - 1
    df['Season'] = f"{season_year}/{season_year+1}"
    # Reorder columns to have "Season" at the beginning
    df = df[['Season'] + columns_to_keep]
    # Append to the list
    dfs.append(df)

# Concatenate all dataframes into one
laliga_matches_df = pd.concat(dfs, ignore_index=True)
laliga_matches_df.insert(0, 'League', 'LaLiga')
laliga_matches_df = laliga_matches_df.sort_values(by=["League", "Season"], ascending=False).reset_index(drop=True)
# print(laliga_matches_df)



league_matches_df = pd.concat([laliga_matches_df], ignore_index=True)



# Initialize a defaultdict to keep track of scores and goals, now including league
team_stats = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'points': 0, 'goals_scored': 0, 'goals_against': 0, 'goal_difference': 0})))

# Iterate through each row to calculate scores and goals, including league
for index, row in league_matches_df.iterrows():
    league = row['League']
    season = row['Season']
    home_team, away_team = row['HomeTeam'], row['AwayTeam']
    home_team_goals, away_team_goals = row['FTHG'], row['FTAG']
    result = row['FTR']

    # Update goals scored and against, now considering league
    team_stats[league][home_team][season]['goals_scored'] += home_team_goals
    team_stats[league][home_team][season]['goals_against'] += away_team_goals
    team_stats[league][away_team][season]['goals_scored'] += away_team_goals
    team_stats[league][away_team][season]['goals_against'] += home_team_goals

    # Update points based on match result
    if result == 'H':  # Home win
        team_stats[league][home_team][season]['points'] += 3
    elif result == 'A':  # Away win
        team_stats[league][away_team][season]['points'] += 3
    elif result == 'D':  # Draw
        team_stats[league][home_team][season]['points'] += 1
        team_stats[league][away_team][season]['points'] += 1

# Convert the nested defaultdict to a DataFrame, including league
data = []
for league, teams in team_stats.items():
    for team, seasons in teams.items():
        for season, stats in seasons.items():
            stats['goal_difference'] = stats['goals_scored'] - stats['goals_against']
            data.append({'League': league, 'Team': team, 'Season': season, **stats})

league_stats_df = pd.DataFrame(data)

# Assign positions within each league and season based on points, goal difference, etc.
league_stats_df['position'] = league_stats_df.sort_values(
    by=['League', 'Season', 'points', 'goal_difference', 'goals_scored', 'goals_against'],
    ascending=[True, True, False, False, False, True]
).groupby(['League', 'Season']).cumcount() + 1

# Ensure the final DataFrame is sorted by League, Season, and Position
league_default_results_df = league_stats_df.sort_values(by=['League', 'Season', 'position'], ascending=[True, False, True]).reset_index(drop=True)

# Select and order the columns as needed
league_default_results_df = league_default_results_df[['League', 'Team', 'Season', 'position', 'points']]#, 'goals_scored', 'goals_against', 'goal_difference']]


# Initialize a defaultdict to keep track of scores and goals, now including league
team_stats = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'points': 0, 'goals_scored': 0, 'goals_against': 0, 'goal_difference': 0})))

# Iterate through each row to calculate scores and goals, including league
for index, row in league_matches_df.iterrows():
    league = row['League']
    season = row['Season']
    home_team, away_team = row['HomeTeam'], row['AwayTeam']
    home_team_goals, away_team_goals = row['FTHG'], row['FTAG']
    result = row['FTR']

    # Update goals scored and against, now considering league
    team_stats[league][home_team][season]['goals_scored'] += home_team_goals
    team_stats[league][home_team][season]['goals_against'] += away_team_goals
    team_stats[league][away_team][season]['goals_scored'] += away_team_goals
    team_stats[league][away_team][season]['goals_against'] += home_team_goals

    # Update points based on match result
    if result == 'H':  # Home win
        team_stats[league][home_team][season]['points'] += 3
    elif result == 'A':  # Away win
        team_stats[league][away_team][season]['points'] += 3
    elif result == 'D':  # Draw
        team_stats[league][home_team][season]['points'] += min(1 * 0.5 * home_team_goals, 1.5)
        team_stats[league][away_team][season]['points'] += min(1 * 0.5 * away_team_goals, 1.5)

# Convert the nested defaultdict to a DataFrame, including league
data = []
for league, teams in team_stats.items():
    for team, seasons in teams.items():
        for season, stats in seasons.items():
            stats['goal_difference'] = stats['goals_scored'] - stats['goals_against']
            data.append({'League': league, 'Team': team, 'Season': season, **stats})

league_stats_df = pd.DataFrame(data)

# Assign positions within each league and season based on points, goal difference, etc.
league_stats_df['position'] = league_stats_df.sort_values(
    by=['League', 'Season', 'points', 'goal_difference', 'goals_scored', 'goals_against'],
    ascending=[True, True, False, False, False, True]
).groupby(['League', 'Season']).cumcount() + 1

# Ensure the final DataFrame is sorted by League, Season, and Position
league_modified_results_df = league_stats_df.sort_values(by=['League', 'Season', 'position'], ascending=[True, False, True]).reset_index(drop=True)

# Select and order the columns as needed
league_modified_results_df = league_modified_results_df[['League', 'Team', 'Season', 'position', 'points']]#, 'goals_scored', 'goals_against', 'goal_difference']]


league_results_df = pd.merge(league_default_results_df, league_modified_results_df, on=['League', 'Team', 'Season'], suffixes=["_default", "_modified"])


print(
    league_results_df[
        ((league_results_df["position_modified"] == 1) |
        (league_results_df["position_default"] == 1)) &
        (league_results_df["position_default"] != league_results_df["position_modified"])
    ][["League", "Team", "Season", "position_default", "position_modified", "points_default", "points_modified"]]
)
