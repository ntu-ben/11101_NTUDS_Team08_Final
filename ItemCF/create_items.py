with open ('./items.txt') as f:
    lines = f.readlines()
    i=0
    lines = lines[0].split(",")
    for line in lines:
        i+=1
        print('\"'+line+'\",',end=' ')

  