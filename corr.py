import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

top_5 = pd.read_csv("top_5.csv", sep = ",")
#print(top_5)

#Pearson correlation
#print(top_5.corr())

sns.heatmap(top_5.corr(), cmap = "YlGnBu", annot = True)
plt.xticks(rotation = 30, ha = 'right')
plt.title("Pearson Correlation")
plt.show()
