import pickle
import matplotlib.pyplot as plt 

# Load
with open('result.pickle', 'rb') as f:
    user_first_observation_month = pickle.load(f)



# Plot
plt.figure(figsize=(10,7))
bar = plt.bar(user_first_observation_month.keys(),user_first_observation_month.values())
plt.xticks(rotation=45, ha='right')
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')
plt.show()
