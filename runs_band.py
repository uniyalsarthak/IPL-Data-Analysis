import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/HP/Downloads/archive/ipl2024.csv")
# countrun=data[(data['first_score']>=150 )& (data['decision']=='Bat')].shape[0]
# print(countrun)

graph=sns.displot(
    data=data,
    x='first_score',
    bins=[0, 100, 150, 200,300],  # You can adjust the max bin if scores go above 300
    color='mediumseagreen',  # Nice green color
    aspect=1.2
)
ax=graph.ax
for patch in ax.patches:
    height = patch.get_height()
    x = patch.get_x() + patch.get_width() / 2
    ax.text(x, height + 1, int(height), ha='center', va='bottom', fontsize=10)



# Add labels and title
ax.set_xlabel('First Innings Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Matches', fontsize=12, fontweight='bold')
ax.set_title('Distribution of First Innings Scores',fontsize=14, fontweight='bold')
plt.xticks([100, 150, 200,300])  # Optional: adjust based on your data
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
