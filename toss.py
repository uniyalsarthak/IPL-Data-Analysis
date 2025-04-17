import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/HP/Downloads/archive/ipl2024.csv")
# print(data)




toss_data=data["decision"].value_counts()
toss_x=toss_data.index
toss_y=toss_data.values


# Create a DataFrame for plotting
toss_df = pd.DataFrame({
    'decision': toss_x,
    'count': toss_y
})


plt.figure(figsize=(6, 4))
ax = sns.barplot(data=toss_df, x='decision', y='count', palette="tab10")

# Add text labels on top of bars
for i in range(len(toss_df)):
    ax.text(i, toss_df['count'][i] + 0.5, str(toss_df['count'][i]), ha='center')


plt.title("Toss Decision Counts (Bat vs Field)", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Decision", fontsize=12)
plt.ylabel("Number of Matches", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.ylim(0, toss_df['count'].max() + 5)
sns.despine()  # remove top/right borders
plt.tight_layout()
plt.show()