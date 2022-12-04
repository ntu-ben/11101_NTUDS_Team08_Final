import pickle

path = '../Data/train_small.csv'

f = open(path,"r")
lines = f.readlines()

headers = lines[0][:-1].split(',')[2:]
previous_month = {}
for header in headers:
    previous_month.update({header:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})

# previous_month['ind_ahor_fin_ult1'][3] += 9
# previous_month['ind_cco_fin_ult1'][16]+=3

#print(previous_month)

# line = lines[1]
# print(line)
# line = lines[1][:-1].split(',')
# ncodper = line[1]
# items = line[2:]
# print(line)
# print(ncodper)
# print(items)
# print("=============")
# line2 = lines[1681277][:-1].split(',')
# ncodpe2r = line[1]
# items2 = line[2:]

# print(ncodpe2r == ncodper)

# for i in range(2):
#     line = [1,2,3,4]
#     for j in range(2):
#         line2 = [2,3,4,5]
#         line = line2
#         print(line)
#     print(line)

for i in range(12715857,13647310): #2016-05-28
    if(i%10 == 7):
        print(i)

    month_index = 16
    line = lines[i][:-1].split(',')
    ncodper = line[1]
    items = line[2:]

    flag = True
    for j in range(11787583,12715857): #2016-04-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(10862507,11787583): #2016-03-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(9941603,10862507): #2016-02-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(9025334,9941603): #2016-01-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(8113313,9025334): #2015-12-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(7207204,8113313): #2015-11-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(6314953,7207204): #2015-10-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(5449513,6314953): #2015-09-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(4606312,5449513): #2015-08-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(3776495,4606312): #2015-07-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(3144385,3776495): #2015-06-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(2512428,3144385): #2015-05-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(1882061,2512428): #2015-04-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(1252852,1882061): #2015-03-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    flag = True
    for j in range(625458,1252852): #2015-02-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break
    if(flag == True):
        continue

    for j in range(1,625458): #2015-01-28
        inline = lines[j][:-1].split(',')
        inncodper = inline[1]
        initems = inline[2:]
        if(ncodper == inncodper):
            flag = False
            for k in range(len(items)):
                if(items[k]=='1' and initems[k]=='0'):
                    previous_month[headers[k]][month_index] += 1
            month_index -= 1
            items = initems
            break

with open("previous_month.pickle", "wb") as file:
    pickle.dump(previous_month, file, pickle.HIGHEST_PROTOCOL)
