import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


with open('itemSimMatrix_all.pickle', 'rb') as f:
    data = pickle.load(f)
    


corr = [[0 for col in range(24)] for row in range(24)]

for i in data:
    for j in data[i]:
        corr[i][j] = data[i][j]
        #print(data[i][j])
        #print("\n")
#print(corr)
for i in range(24):
    for j in range(24):
        if(i == j):
            corr[i][j] = 1
df = pd.DataFrame(corr)
items = ["ind_ahor_fin_ult1", "ind_aval_fin_ult1", "ind_cco_fin_ult1", "ind_cder_fin_ult1", "ind_cno_fin_ult1", "ind_ctju_fin_ult1", "ind_ctma_fin_ult1", "ind_ctop_fin_ult1", "ind_ctpp_fin_ult1", "ind_deco_fin_ult1", "ind_deme_fin_ult1", "ind_dela_fin_ult1", "ind_ecue_fin_ult1", "ind_fond_fin_ult1", "ind_hip_fin_ult1", "ind_plan_fin_ult1", "ind_pres_fin_ult1", "ind_reca_fin_ult1", "ind_tjcr_fin_ult1", "ind_valo_fin_ult1", "ind_viv_fin_ult1", "ind_nomina_ult1", "ind_nom_pens_ult1", "ind_recibo_ult1"]
df.columns = items
df.index = items
print(df) 

#print(data)
#top_5 = pd.read_csv("top_5.csv", sep = ",")
#print(top_5)

# #Pearson correlation
# #print(top_5.corr())


sns.heatmap(df, cmap = "BuPu", annot = True)
plt.xticks(rotation = 30, ha = 'right')
plt.title("Correlation")
plt.show()