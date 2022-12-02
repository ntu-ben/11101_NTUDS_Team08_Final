import numpy as np
import pandas as pd
import pickle

path = './test_users_not_in_train.txt'
f = open(path, 'w')

# Read csv
test_df = pd.read_csv('../Data/test_hash.csv')
train_df = pd.read_csv('../Data/train_ver2.csv')

# Build Dictionary (key:date, value:user_num)
user_first_observation_month = {}
for i in train_df['fecha_dato'].unique():
    user_first_observation_month.update({i: 0})


for i in test_df['ncodpers']:
    if(i%100 == 1):
        print(i)
        
    ans = train_df.loc[train_df['ncodpers'] == i]
    
    if(ans.empty):
        f.write(str(i)+"\n")
    else:
        user_first_observation_month[ ans.iloc[[0]]['fecha_dato'].to_string().split()[1] ] += 1


# Save dictionary
with open("result.pickle", "wb") as file:
    pickle.dump(user_first_observation_month, file, pickle.HIGHEST_PROTOCOL)


f.close()