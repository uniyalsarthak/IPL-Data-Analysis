import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
data = pd.read_csv("C:/Users/HP/Downloads/archive/ipl2024.csv")
data = data.iloc[:-4]
# Initialize a dictionary to track team stats
team_stats = {}

# Process each match
for index, row in data.iterrows():
    # Initialize stats for team1 if not already
    if row['team1'] not in team_stats:
        team_stats[row['team1']] = {'matches': 0, 'wins': 0, 'losses': 0, 'no_result': 0, 'points': 0}
    
    # Initialize stats for team2 if not already
    if row['team2'] not in team_stats:
        team_stats[row['team2']] = {'matches': 0, 'wins': 0, 'losses': 0, 'no_result': 0, 'points': 0}

    # Both teams played a match
    team_stats[row['team1']]['matches'] += 1
    team_stats[row['team2']]['matches'] += 1

    # Handling match result
    if row['winner'] == 'Abandoned':
        team_stats[row['team1']]['no_result'] += 1
        team_stats[row['team2']]['no_result'] += 1
        team_stats[row['team1']]['points'] += 1
        team_stats[row['team2']]['points'] += 1
    elif row['winner'] == row['team1']:
        team_stats[row['team1']]['wins'] += 1
        team_stats[row['team1']]['points'] += 2
        team_stats[row['team2']]['losses'] += 1
    elif row['winner'] == row['team2']:
        team_stats[row['team2']]['wins'] += 1
        team_stats[row['team2']]['points'] += 2
        team_stats[row['team1']]['losses'] += 1

# Convert the team stats dictionary to a DataFrame
points_table = pd.DataFrame(team_stats).T
points_table = points_table[['matches', 'wins', 'losses', 'no_result', 'points']]

# Sort the points table based on points (and wins)
points_table = points_table.sort_values(by=['points', 'wins'], ascending=False)

# Reset index and display the points table
points_table.reset_index(inplace=True)
points_table.rename(columns={'index': 'Team'}, inplace=True)

# Create a bar plot for the points table
plt.figure(figsize=(8, 5))
sns.barplot(x='points', y='Team', data=points_table, palette='coolwarm')

# Add labels to the bars
for index, value in enumerate(points_table['points']):
    plt.text(value + 0.1, index, str(value), color='black', ha="left", va="center", fontweight='bold')

# Customize the plot
plt.xlabel('Points', fontsize=14, fontweight='bold')
plt.ylabel('Team', fontsize=14, fontweight='bold')
plt.title('IPL 2024 Points Table', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
