#_*_coding:utf8_*_
x = range(1,10)
y = range(1,10)

for i in x:
    for j in y:
        if i <= j:
            print "%d * %d = %d" %(i,j,i*j),

    print

