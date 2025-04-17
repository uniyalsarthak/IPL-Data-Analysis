import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
data = pd.read_csv("C:/Users/HP/Downloads/archive/ipl2024.csv")

# Count how many times a team got all out in the first innings
first_innings_all_out = data[data['first_wkts'] == 10].shape[0]

# Count how many times a team got all out in the second innings
second_innings_all_out = data[data['second_wkts'] == 10].shape[0]

# Prepare data for plotting
all_out_data = pd.DataFrame({
    'Innings': ['First Innings', 'Second Innings'],
    'All Out Count': [first_innings_all_out, second_innings_all_out]
})

# Plot the bar chart
plt.figure(figsize=(7, 5))
sns.barplot(x='Innings', y='All Out Count', data=all_out_data, palette='muted')

# Add labels on top of the bars
for index, value in enumerate(all_out_data['All Out Count']):
    plt.text(index, value + 0.1, str(value), ha='center', va='bottom', fontsize=12, fontweight='bold')

# Customize the plot
plt.xlabel('Innings', fontsize=14, fontweight='bold')
plt.ylabel('Number of All Outs', fontsize=14, fontweight='bold')
plt.title('All Outs in IPL 2024 ', fontsize=16, fontweight='bold')

# Show the plot
sns.despine()  # remove top/right borders
plt.tight_layout()
plt.show()
