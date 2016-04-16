name = raw_input('What is your name? ')
print 'Nice'
print 'So %s, I will now guess your age!' % name
print 'But I need to ask some questions:'
n1 = input('What is the first number of your age? ')
print 'Ok %s, I will multiply that by 5 = %s' % (name,5*n1)
#     'Ok',name,'I will multiply that by 5 = %s' % (5*n1)

print 'Next, I will add 3 to the number = %s' % ((n1*5)+3)
print 'Next, I will double that number = %s' % ((((n1*5)+3))*2)
n2 = input('Now I will need the second number of your age: ')
print 'Thanks, I will add that number to our running total %s + %s = %s ' %((((n1*5)+3))*2, n2, n2+(((n1*5)+3)*2))
print 'And the last thing I will do is subtract 6 ( %s - 6 ) = %s ' % (n2+(((n1*5)+3)*2), (n2+(((n1*5)+3)*2)-6))
