import pandas as pd
import os
from collections import defaultdict


pd.set_option('display.max_rows', 500)  # or None to display all rows
pd.set_option('display.max_columns', 100)  # or None to display all columns



# List all the elements in the folder
directory = "./data/LaLiga"

files = os.listdir(directory)
# files = ['SP1 (1).csv', 'SP1 (10).csv', 'SP1 (11).csv', 'SP1 (12).csv', 'SP1 (13).csv', 'SP1 (14).csv', 'SP1 (15).csv', 'SP1 (16).csv', 'SP1 (17).csv', 'SP1 (18).csv', 'SP1 (19).csv', 'SP1 (2).csv', 'SP1 (20).csv', 'SP1 (21).csv', 'SP1 (22).csv', 'SP1 (23).csv', 'SP1 (24).csv', 'SP1 (25).csv', 'SP1 (26).csv', 'SP1 (27).csv', 'SP1 (28).csv', 'SP1 (29).csv', 'SP1 (3).csv', 'SP1 (30).csv', 'SP1 (4).csv', 'SP1 (5).csv', 'SP1 (6).csv', 'SP1 (7).csv', 'SP1 (8).csv', 'SP1 (9).csv', 'SP1.csv']

# Columns to keep
columns_to_keep = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']

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
laliga_matches_df = laliga_matches_df.sort_values(by="Season", ascending=False).reset_index(drop=True)
# print(laliga_matches_df)

# Initialize a defaultdict to keep track of scores
team_scores = defaultdict(lambda: defaultdict(int))

# Iterate through each row to calculate scores
for index, row in laliga_matches_df.iterrows():
    season = row['Season']
    home_team, away_team = row['HomeTeam'], row['AwayTeam']
    home_team_goals, away_team_goals = row['FTHG'], row['FTAG']
    result = row['FTR']

    if result == 'H':  # Home win
        team_scores[home_team][season] += 3
    elif result == 'A':  # Away win
        team_scores[away_team][season] += 3
    elif result == 'D':  # Draw
        team_scores[home_team][season] += 1
        team_scores[away_team][season] += 1

# Convert defaultdict to DataFrame
laliga_default_results_df = pd.DataFrame.from_dict(team_scores, orient='index').reset_index()
laliga_default_results_df.rename(columns={'index': 'Team'}, inplace=True)

# Rename columns to match the specified format
laliga_default_results_df.columns = ['Team'] + [f"Season_{col}_points" for col in laliga_default_results_df.columns[1:]]

# Sort the teams within each season by their points and assign positions
for season in [col.split('_points')[0] for col in laliga_default_results_df.columns if '_points' in col]:
    season_points_col = f"{season}_points"
    season_position_col = f"{season}_position"

    # Sort the DataFrame by the current season's points in descending order
    season_df_sorted = laliga_default_results_df.sort_values(by=season_points_col, ascending=False)#.reset_index(drop=True)

    # Assign positions, considering NaN values which represent teams without points
    # Teams with NaN points will not get a position (will remain NaN)
    season_df_sorted[season_position_col] = season_df_sorted[season_points_col].rank(method='min', ascending=False,
                                                                                     na_option='keep')

    # Update the original DataFrame with the new positions
    laliga_default_results_df[season_position_col] = season_df_sorted[season_position_col]


# Melt the DataFrame
melted_df = laliga_default_results_df.melt(id_vars=['Team'], var_name='Season_Metric', value_name='Value')

# Extract season and metric type
melted_df['Season'] = melted_df['Season_Metric'].apply(lambda x: x.split('_')[1])
melted_df['Metric'] = melted_df['Season_Metric'].apply(lambda x: x.split('_')[-1])

# Drop the original Season_Metric column as it's no longer needed
melted_df.drop('Season_Metric', axis=1, inplace=True)

# Pivot the table to have separate columns for points and positions
final_df = melted_df.pivot_table(index=['Team', 'Season'], columns='Metric', values='Value').reset_index()

# Rename columns to match your desired output
final_df.columns.name = None  # Remove the categorization name to clean up the DataFrame

laliga_default_results_df = final_df.sort_values(by=["Season", "points"], ascending=False).reset_index(drop=True)



# Initialize a defaultdict to keep track of scores
team_scores = defaultdict(lambda: defaultdict(int))

# Iterate through each row to calculate scores
for index, row in laliga_matches_df.iterrows():
    season = row['Season']
    home_team, away_team = row['HomeTeam'], row['AwayTeam']
    home_team_goals, away_team_goals = row['FTHG'], row['FTAG']
    result = row['FTR']

    if result == 'H':  # Home win
        team_scores[home_team][season] += 3
    elif result == 'A':  # Away win
        team_scores[away_team][season] += 3
    elif result == 'D' and home_team_goals != 0 and away_team_goals != 0:  # Draw
        team_scores[home_team][season] += 1 * 0 * home_team_goals
        team_scores[away_team][season] += 1 * 0 * away_team_goals

# Convert defaultdict to DataFrame
laliga_modified_results_df = pd.DataFrame.from_dict(team_scores, orient='index').reset_index()
laliga_modified_results_df.rename(columns={'index': 'Team'}, inplace=True)

# Rename columns to match the specified format
laliga_modified_results_df.columns = ['Team'] + [f"Season_{col}_points" for col in laliga_modified_results_df.columns[1:]]


# Sort the teams within each season by their points and assign positions
for season in [col.split('_points')[0] for col in laliga_modified_results_df.columns if '_points' in col]:
    season_points_col = f"{season}_points"
    season_position_col = f"{season}_position"

    # Sort the DataFrame by the current season's points in descending order
    season_df_sorted = laliga_modified_results_df.sort_values(by=season_points_col, ascending=False)

    # Assign positions, considering NaN values which represent teams without points
    # Teams with NaN points will not get a position (will remain NaN)
    season_df_sorted[season_position_col] = season_df_sorted[season_points_col].rank(method='min', ascending=False,
                                                                                     na_option='keep')

    # Update the original DataFrame with the new positions
    laliga_modified_results_df[season_position_col] = season_df_sorted[season_position_col]


# Melt the DataFrame
melted_df = laliga_modified_results_df.melt(id_vars=['Team'], var_name='Season_Metric', value_name='Value')

# Extract season and metric type
melted_df['Season'] = melted_df['Season_Metric'].apply(lambda x: x.split('_')[1])
melted_df['Metric'] = melted_df['Season_Metric'].apply(lambda x: x.split('_')[-1])

# Drop the original Season_Metric column as it's no longer needed
melted_df.drop('Season_Metric', axis=1, inplace=True)

# Pivot the table to have separate columns for points and positions
final_df = melted_df.pivot_table(index=['Team', 'Season'], columns='Metric', values='Value').reset_index()

# Rename columns to match your desired output
final_df.columns.name = None  # Remove the categorization name to clean up the DataFrame

laliga_modified_results_df = final_df.sort_values(by=["Season", "points"], ascending=False).reset_index(drop=True)



laliga_results_df = pd.merge(laliga_default_results_df, laliga_modified_results_df, on=['Team', 'Season'], suffixes=["_default", "_modified"])


print(
    laliga_results_df[
        ((laliga_results_df["position_modified"] == 1) |
        (laliga_results_df["position_default"] == 1)) &
        (laliga_results_df["position_default"] != laliga_results_df["position_modified"])
    ][["Team", "Season", "position_default", "position_modified", "points_default", "points_modified"]]
)
