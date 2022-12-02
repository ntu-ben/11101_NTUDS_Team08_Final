with open ('../Data/train_small.csv') as f:
    lines = f.readlines()
    fp = open("train_small_ncod_item.csv", "w")
    fp.write("fecha_dato,ncodpers,item_id\n")
    items = lines[0][:-1].split(",")
    for i in range(1,len(lines)):
        line = lines[i][:-1].split(',')
        date = line[0]
        ncodper = line[1]
        index = 0
        for j in line[2:]: # j in items  
            if(j=="NA"):
                continue  
            if(int(j) == 1):
                fp.write(date+","+ncodper+","+str(index)+"\n")
            index += 1
                
       
    # for i in range(1, len(lines)):
    #     iniline = lines[i]
    #     line = lines[i].split(',')[2].split(' ')[0].split('-')
    #     # if (  (line[0] == '2021' and (line[1] == '05' or line[1] == '04' or line[1] == '03' ) or line[1] == '02' or line[1] == '01' ))   :
    #     if (  line[0] == '2021'  or  line[0] == '2020' and 6<int(line[1][1])<9 )   :
    #         fp.write(iniline)
