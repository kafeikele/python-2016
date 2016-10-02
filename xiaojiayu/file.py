f = file('passwd','r')
for line in f.readlines():
	line = line.strip('\n').split(':')
	print line
