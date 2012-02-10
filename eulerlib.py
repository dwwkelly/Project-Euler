import math
import sys
from optparse import OptionParser

__author__ = 'Devin Kelly <dwwkelly@gmail.com>'

functions = []
MICROSECONDS_PER_SECOND = 1000000


def test_fun(fun):
    functions.append(fun)
    return fun


@test_fun
def nDigits(anInt):
    ''' Returns how many digits a number has

    >>> nDigits(100)
    3
    >>> nDigits(999)
    3
    >>> nDigits(1234567890)
    10
    '''
    exponent = 0
    while(float(anInt) / float(10 ** exponent) >= 1):
        exponent = exponent + 1

    return int(exponent)


@test_fun
def nDigitsStr(anInt):
    ''' Return how many digits a number has

    >>> nDigitsStr(100)
    3
    >>> nDigitsStr(999)
    3
    >>> nDigitsStr(0)
    1
    >>> nDigitsStr(1234567890)
    10
    '''
    return len(str(anInt))


@test_fun
def isLeapYear(year):
    ''' returns true for years that leapyears, false otherwise

    >>> isLeapYear(1600)
    True
    >>> isLeapYear(1601)
    False
    >>> isLeapYear(2000)
    True
    >>> isLeapYear(1700)
    False
    >>> isLeapYear(2011)
    False
    '''
    if ((year % 4) == 0 and (year % 100) != 0) or ((year % 400) == 0):
        return True
    else:
        return False


@test_fun
def factorial(anInt):
    ''' returns the factorial of an integer, i.e. n!
    >>> factorial(0)
    1
    >>> factorial(2)
    2
    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    '''
    if anInt == 0:
        return 1

    if anInt > 1:
        return anInt * factorial(anInt - 1)
    else:
        return anInt


@test_fun
def propDivisors(anInt):
    ''' returns the proper divisors of the given int.
        proper divisors are all the numbers that evenly divide the number

        >>> propDivisors(6)
        [1, 2, 3]

        >>> propDivisors(120)
        [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60]

        >>> propDivisors(220)
        [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]

        >>> propDivisors(284)
        [1, 2, 4, 71, 142]
        '''
    l = [1]
    for ii in xrange(2, (anInt / 2) + 1):
        if anInt % ii == 0:
            l.append(ii)
    return l


@test_fun
def npickk(n, k):
    ''' returns n pick k,

            n!
        ---------
         (n - k)!

        >>> npickk(4, 2)
        12

        >>> npickk(8, 5)
        6720
        '''
    return int(float(factorial(n)) / float(factorial(n - k)))


@test_fun
def nchoosek(n, k):
    ''' Returns n choose k

             n!
        ------------
         k! (n - k)!

        >>> nchoosek(8, 5)
        56

        >>> nchoosek(2, 2)
        1

        >>> nchoosek(10, 4)
        210
        '''
    from operator import mul
    numerator = reduce(mul, range(n - k + 1, n + 1))
    denominator = factorial(k)

    return int(numerator / denominator)


@test_fun
def fibonacci(n):
    '''
    returns the Nth term of the fibonacci sequence

    >>> fibonacci(1)
    1

    >>> fibonacci(8)
    21

    >>> fibonacci(13)
    233
    '''
    if n is 1 or n is 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@test_fun
def fibonacciCF(n):
    '''
    returns the Nth term of the fibonacci sequence

    >>> fibonacciCF(1)
    1

    >>> fibonacciCF(8)
    21

    >>> fibonacci(13)
    233

    >>> fibonacciCF(49)
    7778742049
    '''
    sqrtFive = math.sqrt(5.0)
    goldenRatio = (1.0 + sqrtFive) / 2.0

    partOne = goldenRatio ** float(n)
    partTwo = (-1.0 / goldenRatio) ** float(n)
    return int(round((partOne - partTwo) / sqrtFive))


@test_fun
def gcd(a, b):
    ''' Returns the greatest common denominator of the given number

    this uses Euclid's method

    >>> gcd(1071, 462)
    21
    >>> gcd(58, 8)
    2

    '''
    remainder = b
    while remainder is not 0:
        t = remainder
        remainder = a % remainder
        a = t

    return a


@test_fun
def primeGen(n):
    ''' Returns a list of primes up to the given number, n

    Uses the 'Sieve of Eratosthenes'
    source: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> primeGen(5)
    [2, 3, 5]

    >>> primeGen(45)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

    >>> primeGen(11)
    [2, 3, 5, 7, 11]
    '''
    p = 2
    allNums = set(range(p, n + 1))
    primes = set()
    composites = set()

    while 1:
        [composites.add(ii) for ii in range(p * 2, n + 1, p)]

        try:
            p = min(allNums - composites - primes)
        except:
            break
        primes.add(p)

    return sorted(list(primes))


@test_fun
def sieveOfEratosthenes(n):
    ''' Returns a list of primes up to the given number, n

    Uses the 'Sieve of Eratosthenes'
    source: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> sieveOfEratosthenes(5)
    [2, 3, 5]

    >>> sieveOfEratosthenes(45)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

    >>> sieveOfEratosthenes(11)
    [2, 3, 5, 7, 11]
    '''
    l = [False, False]
    [l.append(True) for ii in xrange(1, n)]

    for ii in xrange(2, n / 2 + 2):
        if l[ii] is True:
            for kk in xrange(2, n / ii + 1):
                l[kk * ii] = False

    return [ii for ii in xrange(1, len(l)) if l[ii] is True]


@test_fun
def isPrime(n):
    """
        >>> isPrime(6)
        False
        >>> isPrime(7)
        True
        >>> isPrime(15)
        False
        >>> isPrime(16)
        False
        >>> isPrime(17)
        True
        >>> isPrime(281)
        True
    """

    primes = sieveOfEratosthenes(n)

    if primes.count(n) is not 0:
        return True
    else:
        return False


@test_fun
def lcm(a, b):
    ''' returns the least common multiple of a and b using this algorithm

                       (a*b)
      lcm(a, b) =   ------------
                      gcd(a, b)

    >>> lcm(6, 4)
    12
    >>> lcm(21, 6)
    42

    '''
    return (a * b) / gcd(a, b)


@test_fun
def lcmHeuristic(a, b):
    ''' returns the least common multiple of a and b using a heurstic method

    >>> lcmHeuristic(4, 6)
    12
    >>> lcmHeuristic(4, 5)
    20
    '''
    commonMultiple = a * b + 1
    aSet = set(range(a, commonMultiple, a))
    bSet = set(range(b, commonMultiple, b))

    return min(aSet & bSet)


@test_fun
def carmichael(n, maxloop=200):
    ''' returns the smallest positive integer n such that
     m
    a  = 1 (mod n)

    http://en.wikipedia.org/wiki/Carmichael_function

    >>> carmichael(1)
    1
    >>> carmichael(2)
    1
    >>> carmichael(4)
    2
    >>> carmichael(5)
    4
    >>> carmichael(9)
    6
    >>> carmichael(13)
    12
    >>> carmichael(17)
    16
    >>> carmichael(18)
    6
    >>> carmichael(19)
    18
    >>> carmichael(20)
    4
    >>> carmichael(21)
    6
    >>> carmichael(23)
    22

    '''

    if n is 1 or n is 2:
        return 1

    coprimes = []
    [coprimes.append(ii) for ii in xrange(1, n + 1) if gcd(n, ii) == 1]

    for m in xrange(1, maxloop):
        for a in coprimes:
            if (a ** m) % n is not 1:
                break
        else:
            return m
    return n - 1  # FIXME this might be hack, but the tests pass


@test_fun
def totient(n):
    '''
    Returns the totient of the given number.

    The totient of a positive integer n is defined
    to be the number of positive integers less than
    or equal to n that are coprime to n

    http://en.wikipedia.org/wiki/Euler%27s_totient_function

    >>> totient(1)
    1
    >>> totient(2)
    1
    >>> totient(4)
    2
    >>> totient(5)
    4
    >>> totient(9)
    6
    >>> totient(13)
    12
    >>> totient(17)
    16
    >>> totient(18)
    6
    >>> totient(19)
    18
    >>> totient(20)
    8
    >>> totient(21)
    12
    >>> totient(23)
    22
    >>> totient(24)
    8
    '''

    coprimes = 0

    for ii in range(1, n + 1):
        if gcd(n, ii) == 1:
            coprimes += 1
    return coprimes


@test_fun
def multiplicativeOrder(a, n, maxloops=2000):
    '''

    http://en.wikipedia.org/wiki/Order_(number_theory)

    >>> multiplicativeOrder(4, 7)
    3
    >>> multiplicativeOrder(7, 108)
    18
    '''
    assert gcd(a, n) is 1

    primes = sieveOfEratosthenes(a * n)

    for k in primes:
        if (a ** k) % n  is 1:
            return k
    return None


@test_fun
def howManyPrimes(a, b):
    """
        >>> howManyPrimes(1, 41)
        40
        >>> howManyPrimes(-79, 1601)
        80
    """
    nPrimes = 0
    counter = 0

    while True:
        result = counter ** 2 + a * counter + b

        if isPrime(result):
            nPrimes = nPrimes + 1
            counter = counter + 1
        else:
            break

    return nPrimes


if __name__ == '__main__':
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-t", "--test",
        action="store_true", dest="test", default=False,
        help="Tests All Functions")
    parser.add_option("-l", "--list",
        action="store_true", dest="functionList", default=False,
        help="Prints a list of functions")
    parser.add_option("-f", "--function",
        dest="function", default='',
        help="Get info on the given function")

    (options, args) = parser.parse_args()

    if options.test is True:
        import doctest
        doctest.testmod()
        sys.exit()

    if options.functionList is True:
        for fun in functions:
            print fun.__name__
        sys.exit()

    function = options.function
    if function is not '':
        import timeit
        import matplotlib.pyplot as pyplot

        us = list()
        items = range(1, 1001, 10)
        for ii in items:
            t = timeit.Timer(function + '(' + str(ii) + ')',\
                    'from __main__ import ' + function)
            us.append(t.timeit(100) * 1000000)

        pyplot.plot(items, us)
        pyplot.legend(loc='upper left')
        pyplot.xlabel('Number of Digits')
        pyplot.ylabel('Microseconds')
        pyplot.show()
