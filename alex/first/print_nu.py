#_*_coding:utf-8_*_
print_num = input ('which loop do you want it to be printed out?')
count = 0
while count < 100000000:
  if count == print_num:
    print 'There you got the num:',count
    choice = raw_input('Do U want to continue the loop?y/n')
    if choice == 'n':
      break
    else:
      while print_num <= count:
        print_num = input ('which loop do you want it to be printed out?')
        print "the num have passed"
  else:
      print 'Loop:',count
  count +=1

else:
  print 'Loop:count',count
