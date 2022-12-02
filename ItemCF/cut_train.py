with open ('./train_small_ncod_item.csv') as f:
    lines = f.readlines()
    fp = open("train_small_6_12.csv", "w")
    fp.write("fecha_dato,ncodpers,item_id\n")

    for i in range(1,len(lines)):
        inline = lines[i]
        line = lines[i][:-1].split(',')
        date = line[0]
      
        if(date == '2015-06-28' or date == '2015-12-28'):
            fp.write(inline)
                
    