#_*_coding:utf8_*_
#字符串处理方法
name_list=['wdh', 'whh', 'wxh', 'a', 1, 2, 3, 4, 5, 6, 7, 'a', 1, 2, 3, 4, 5, 6, 7,2,35,56,345,1,2]
first_pos = 0
for i in range(name_list.count(2)):
    new_name_list=name_list[first_pos:]
    next_pos = new_name_list.index(2) + 1
    print 'Find:',first_pos + new_name_list.index(2)
    first_pos += next_pos





