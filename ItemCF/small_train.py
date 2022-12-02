import csv
import codecs
with open("../Data/train_ver2.csv","rb") as source:
    rdr = csv.reader(codecs.iterdecode(source, 'utf-8')  )
    with open("../Data/train_small.csv","w", newline='') as result:
        wtr = csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[24], r[25], r[26], r[27], r[28], r[29], r[30] , r[31], r[32], r[33], r[34], r[35], r[36], r[37], r[38], r[39], r[40], r[41], r[42], r[43], r[44], r[45], r[46], r[47]))
      