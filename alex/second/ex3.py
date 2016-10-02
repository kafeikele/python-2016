#_*_coding:utf8_*_
#字符串处理方法
name_list=['wdh', 'whh', 'wxh', 'a', 1, 2, 3, 4, 5, 6, 7, 'a', 1, 2, 3, 4, 5, 6, 7,2,35,56,345,1,2]


pos = 0
for i in range(name_list.count(2)):
    if pos == 0:
        pos = name_list.index(2)
    else:
        pos = name_list.index(2,pos+1)
    print pos