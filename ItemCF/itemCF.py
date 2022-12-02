import math
import random
import pandas as pd
import pickle
from collections import defaultdict
from operator import itemgetter

def LoadData(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        return PreProcessData(lines)

def CreateCandidate(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        candidate = set()
        for i in range(1, len(lines)):
            line = lines[i]
            candidate.add(int(line))

        return candidate

def PreProcessData(originData):
    """
    建立Session-Item表，結構如下：
        {"Session1": [ ItemID1, ItemID2, ItemID3,... ]
         "Session2": [ ItemID5, ItemID6, ItemID7,... ]
        }
    """
    trainData = dict()
    for i in range(1, len(originData)):
        line = originData[i].split(',')
        session_id = int(line[1])
        item_id = int(line[2])
        date = line[0]
        if trainData.get(session_id) is not None:
            trainData[session_id].append(item_id)
            # if(date == '2015-06-28'):
            #     trainData[session_id].append(item_id)
        else:
            trainData.setdefault(session_id, [])
            trainData[session_id].append(item_id)
            # if(date == '2015-06-28'):
            #     trainData[session_id].append(item_id)

    return trainData


class ItemCF(object):
    """ Item based Collaborative Filtering Algorithm Implementation"""
    def __init__(self, trainData, last_monthData, similarity="cosine", norm=True):
        self._trainData = trainData
        self._lastMonthData = last_monthData
        self._similarity = similarity
        self._isNorm = norm
        self._itemSimMatrix = dict() # 物品相似度矩阵
        """
        self._itemSimMatrix
        { itemID1: { relatedItemID1 : similarity, relatedItemID2 : similarity, ...}
          itemID2: { relatedItemID1 : similarity, relatedItemID2 : similarity, ...}
          ...
        }
        """

    def similarity(self):
        N = defaultdict(int) #记录每个物品的喜爱人数
        for user, items in self._trainData.items():
            #每個物品的喜愛人數不算單個session中重複的
            itemset = set(items)
            for i in itemset:
                N[i] += 1
            
            for i in items:
                self._itemSimMatrix.setdefault(i, dict())
                
                for j in items:
                    if i == j:
                        continue
                    self._itemSimMatrix[i].setdefault(j, 0)
                    if self._similarity == "cosine":
                        self._itemSimMatrix[i][j] += 1
                    elif self._similarity == "iuf":
                        self._itemSimMatrix[i][j] += 1. / math.log1p(len(items) * 1.)
        for i, related_items in self._itemSimMatrix.items():
            for j, cij in related_items.items():
                self._itemSimMatrix[i][j] = cij / math.sqrt(N[i]*N[j])
        # print(N)
        # print(self._itemSimMatrix)


        # with open('itemSimMatrix_6_12.pickle', 'wb') as f:
        #     pickle.dump(self._itemSimMatrix, f)
        # 是否要标准化物品相似度矩阵
        """
        標準化之後分數沒有比較高:3
        """
        # if self._isNorm:

        #     for i, relations in self._itemSimMatrix.items():
        #         #print(i, relations)
        #         if( relations != {} ):
        #             max_num = relations[max(relations, key=relations.get)]
        #         # 对字典进行归一化操作之后返回新的字典
        #             self._itemSimMatrix[i] = {k : v/max_num for k, v in relations.items()}

    def recommend(self, user, N, K):
        """
        :param user: 被推荐的用户user
        :param N: 推荐的商品个数
        :param K: 查找的最相似的用户个数
        :return: 按照user对推荐物品的感兴趣程度排序的N个商品
        """
        recommends = dict()
        # 先获取user的喜爱物品列表
        if self._trainData.get(user) is not None:
            items = self._trainData[user] 
        else:
            items = [2]

        if self._lastMonthData.get(user) is not None:
            last_month_items = self._lastMonthData[user]
        else:
            last_month_items = []

        #point = 1
        # for i in self._trainData:
        #     print(self._trainData[i])
        for item in items:
            # 对每个用户喜爱物品在物品相似矩阵中找到与其最相似的K个
            for i, sim in sorted(self._itemSimMatrix[item].items(), key=itemgetter(1), reverse=True)[:K]:
                if i in last_month_items:
                    continue  # 如果与user喜爱的物品重复了，则直接跳过
                recommends.setdefault(i, 0.)
                recommends[i] += sim #* point
            #point += 1.5
        # 根据被推荐物品的相似度逆序排列，然后推荐前N个物品给到用户
        #return dict(sorted(recommends.items(), key=itemgetter(1), reverse=True)[:N])
        return sorted(recommends.items(), key=itemgetter(1), reverse=True)[:N]

    def train(self):
        self.similarity()

if __name__ == "__main__":
    items = ["ind_ahor_fin_ult1", "ind_aval_fin_ult1", "ind_cco_fin_ult1", "ind_cder_fin_ult1", "ind_cno_fin_ult1", "ind_ctju_fin_ult1", "ind_ctma_fin_ult1", "ind_ctop_fin_ult1", "ind_ctpp_fin_ult1", "ind_deco_fin_ult1", "ind_deme_fin_ult1", "ind_dela_fin_ult1", "ind_ecue_fin_ult1", "ind_fond_fin_ult1", "ind_hip_fin_ult1", "ind_plan_fin_ult1", "ind_pres_fin_ult1", "ind_reca_fin_ult1", "ind_tjcr_fin_ult1", "ind_valo_fin_ult1", "ind_viv_fin_ult1", "ind_nomina_ult1", "ind_nom_pens_ult1", "ind_recibo_ult1"]
    train = LoadData("./train_small_6.csv")
    last_month = LoadData("./train_small_201605.csv")
    ItemCF = ItemCF(train, last_month, similarity='iuf', norm=False)
    ItemCF.train()

    fp = open("recommend_6.csv", "w")
    fp.write("ncodpers,added_products\n")
    with open ('../Data/test_hash_small.csv') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            if(i%1000 == 0):
                print(str(i)+" / "+str(len(lines)))
            ncodper = int(lines[i])
            ans = ItemCF.recommend(i, 7, 24)
            fp.write(str(ncodper)+",")
            for j,k in ans:
                fp.write(items[j]+" ")
            fp.write("\n")
            


 
    # for i in ItemCF._trainData:
    #     ans = ItemCF.recommend(i, 1000, 2000)
    #     #print(ans)
    #     ii = 1
    #     for j,k in ans:
    #         if(ii > 100):
    #             break
    #         if(j in candidate):
    #             fp.write(str(i)+','+str(j)+','+str(ii)+'\n')
    #             ii = ii+1