print 'Hello, what is your name?'
name = str(raw_input(''))
print 'Nice'
print 'So %s, I will now guess your age!' % name
print 'But I need to ask some questions:'
print 'What is the first number of your age?'
first_number = int(raw_input(''))
n1 = first_number*5
print 'Ok %s, I will multiply that by 5 = %s' % (str(name), str(n1))
n2 = n1 + 3
print 'Next, I will add 3 to the number = %s' % n2
n3 = n2 * 2
print 'Next, I will double that number = ', n3
print 'Now I will need the second number of your age: '
second_number = int(raw_input(''))
n4 = n3 + second_number
print 'Thanks, I will add that number to our running total %s + %s = %s ' % (str(n3), str(second_number), str(n4))
age = n4 - 6
print 'And the last thing I will do is subtract 6: ( %s - 6 ) = %s' % (n4, str(age))
print 'So %s, your age is %s' % (str(name), str(age))