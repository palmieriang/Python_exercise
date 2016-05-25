"""
Nuggets.py
Created by Angelo Palmieri.
"""
def nuggets(number):
    """
    Finds a combination of nugget packs (6, 9, 20) to purchase
    a given number of nuggets.
    Args: total number of nuggets needed (limit).
    Returns: a string.
    """
    # check parameters
    try:
        limit = int(number) # check that is the integer value of the number
        assert type (limit) == int, 'input value is not an Integer' # assert just check something
        assert limit >= 0, 'input value is negative'

        # try every possibility
        for c in range(int(limit/20)+1):
            for b in range(int(limit/9)+1):
                for a in range(int(limit/6)+1):
                    n = 6*a + 9*b + 20*c
                    if n == limit:
                        return '6 packs = %s, 9 packs = %s, 20 packs = %s' % (str(a), str(b), str(c))
        return 'No solution for %s nuggets' %str(limit)
    except:
        return 'An error occurred, make sure you entered an Integer.'

def test():
    """ This is a test for the nuggets function """
    print ('Testing 55')
    answer = nuggets(55)
    print str(answer)

def main():
    print 'Nuggets Program'
    print '='*40
    print ''
    user_input = str(raw_input('Test or Run? '))
    if user_input.lower() == 'test':
        print ''
        test()
    elif user_input.lower() == 'run':
        while True:
            print ''
            print "How many nuggets do you need? (or type 'q' to quit)"
            user_input2 = raw_input('>> ')
            if user_input2.lower() == 'q':
                break
            answer = nuggets(user_input2)
            print str(answer)
    else:
        print 'An error occurred, make sure you wrote test or run'
        return main()

if __name__ == '__main__':
    main()
