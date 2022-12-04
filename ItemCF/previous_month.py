import pickle

def LoadData(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        return PreProcessData(lines)

def PreProcessData(lines):
    """
    data = 
    {"Date1": { UserID1: [ItemID1, ItemID2,...],
                UserID2: [ItemID2, ItemID4,...], 
              }
     "Date2": { UserID1: [ItemID1, ItemID2,...],
              }
    }
    """
    data = dict()
    for i in range(1, len(lines)):
        line = lines[i][:-1].split(',')
        date = line[0]
        userId = int(line[1])
        itemId = int(line[2])
        if data.get(date) is not None:
            if data[date].get(userId) is not None:
                data[date][userId].append(itemId)
            else:
                data[date].setdefault(userId, [])
                data[date][userId].append(itemId)
        else:
            data.setdefault(date, {})
            if data[date].get(userId) is not None:
                data[date][userId].append(itemId)
            else:
                data[date].setdefault(userId, [])
                data[date][userId].append(itemId)
    return data

def PreviousMonth(data):
    dates = list(data.keys()) #2015-01-28 ~ 2016-05-28
    """
    previousData = 
    { "Date1": { ItemID1: counts,
                 ItemID2: counts,
                }
      "Date2": {
      }
    }
    """
    previousData = dict()
    for date in dates:
        previousData.setdefault(date,{})
        for i in range(24):
            previousData[date].setdefault(i,0)

    dates = dates[::-1] #2016-05-28 ~ 2015-01-28
    for i in range(len(dates)-1): #2016-05-28 ~ 2015-02-28
        date = dates[i]
        pre_date = dates[i+1]
        for user in data[date]:
            items = data[date][user]
            if data[pre_date].get(user) is not None:
                pre_items = data[pre_date][user]
                for item in items:
                    if item not in pre_items:
                        previousData[date][item] += 1
            else:
                for item in items:
                    previousData[date][item] += 1
    last_month = dates[-1]
    for user in data[last_month]:
        items = data[last_month][user]
        for item in items:
            previousData[last_month][item] += 1

    with open('previous_month.pickle', 'wb') as f:
        pickle.dump(previousData, f)
    

if __name__ == "__main__":
    # with open('previous_preprocess.pickle', 'wb') as f:
    #     pickle.dump(LoadData("./train_small_ncod_item.csv"), f)
    
    with open('previous_preprocess.pickle', 'rb') as f:
        data = pickle.load(f)
    PreviousMonth(data)

    