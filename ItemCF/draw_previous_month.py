import pickle
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


with open('previous_month.pickle', 'rb') as f:
    data = pickle.load(f)

df = pd.DataFrame(data)
df = df.transpose()
# df.drop(index=df.index[0], 
#         axis=0, 
#         inplace=True)
sns.lineplot(data = df)
plt.xticks(rotation = 30, ha = 'right')
plt.show()