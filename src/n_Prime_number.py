"""
prime_numbers.py
Created by Angelo Palmieri
"""


def is_prime_func(number):
    '''
        Takes in a Number and determines if it is a Prime Number
        Args: A Number
        Returns: True or False
    '''
    is_prime = True
    n = abs(int(number))    # make sure n is a positive integer
    if n < 2:               # 0 and 1 are not primes
        is_prime = False
    elif n == 2:            # 2 is the only even prime number
        is_prime = True
    elif n % 2 == 0:
        is_prime = False
    else:
        # range starts with 3 and only needs to go up the squareroot
        # of n for all odd numbers
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                is_prime = False
    return is_prime


def find_n_prime(n):
    '''
        Finds what the n Prime number is
        Args: None
        Returns: The n Prime Number
    '''
    current_number = 2
    count = 0
    while True:
        is_prime = is_prime_func(current_number)
        if is_prime:
            count += 1
        if count == n:
            return current_number
        else:
            current_number += 1


def main():
    print 'Prime Numbers'
    print '='*40
    print ''

    a = int(raw_input('Get the nth Prime Number: '))

    thous_prime = find_n_prime(a)

    if thous_prime:
            print ''
            print 'The %sth Prime Number is: %s' % (a, int(thous_prime))
    else:
            print 'Sorry, Error Occurred'


if __name__ == '__main__':
    main()
