import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
data = pd.read_csv("C:/Users/HP/Downloads/archive/ipl2024.csv")

# Filter successful run chases (chose to field and won)
successful_chases = data[(data['decision'] == 'Field') & (data['winner'] == data['team2'])]

# Create a new column for target runs to be chased
# We assume the target is the first innings score + 1 (since second team chases)
successful_chases['target'] = successful_chases['first_score'] + 1

# Filter only those where target was over 170
filtered_chases = successful_chases[successful_chases['target'] >= 170]

# Define the bins for target ranges
bins = [170, 200, 1000]  # 1000 just to cover any extreme scores above 200
labels = ['170-200', '200+']
filtered_chases['chase_range'] = pd.cut(filtered_chases['target'], bins=bins, labels=labels)

# Count number of successful chases in each range
chase_counts = filtered_chases['chase_range'].value_counts().sort_index()

# Plot histogram using seaborn
plt.figure(figsize=(7, 4))
sns.barplot(x=chase_counts.index, y=chase_counts.values, palette='viridis')

# Add count labels on top of bars
for i, val in enumerate(chase_counts.values):
    plt.text(i, val + 0.2, str(val), ha='center', fontweight='bold', fontsize=12)

# Styling
sns.despine()  # remove top/right borders
plt.xlabel('Target Range (Runs)', fontsize=12, fontweight='bold')
plt.ylabel('Successful Chases', fontsize=12, fontweight='bold')
plt.title('Successful Run Chases', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
