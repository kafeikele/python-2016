#_*_coding:utf8_*_
f = file('../file/passwd.txt','r')
for line in f.readlines():
    line = line.strip('\n').split(':')
    print line
f.close()

f = file('../file/passwd.txt','r')
for line in f.readlines():
    line = line.strip('\n').split(':')[0:4]
    print line
f.close()

#strip去掉换行符，split分开，是对字符串进行修饰
#line = line.strip('\n').split(':')
 已经由字符串转换为列表
#还可以对列表进行修饰，取值[0]
# f.write(u'学习python'.encode('utf-8'))

#f.read()是以字符串的形式读取文件
#f.readline是以列表的形式读取文件
#f.seek(0)回到开头,
#f.tell()告诉你在这个文本的哪里
#f.tell()和f.seek结合使用做日志分析

#_*_coding:utf8_*_

f = file('../file/test.txt','w')
f.write(u'haohao学习python'.encode('utf-8'))
f.close()
