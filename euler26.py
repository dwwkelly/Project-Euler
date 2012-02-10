#!/usr/bin/python

import eulerlib

if __name__ == '__main__':
        '''

        http://mathworld.wolfram.com/DecimalExpansion.html
        http://en.wikipedia.org/wiki/Repeating_decimal

        http://mathworld.wolfram.com/DiscreteLogarithm.html
        http://en.wikipedia.org/wiki/Discrete_logarithm

        '''
        dMax = 1000
        primes = eulerlib.sieveOfEratosthenes(dMax)
        primes.remove(2)
        primes.remove(5)
        primes.reverse()

        kMax = 1
        pMax = primes[0]

        for p in primes:
            k = 1
            while (pow(10, k) % p) != 1:
                k += 1
            if k > kMax:
                kMax = k
                pMax = p
        print 'Repeating length: ', kMax
        print 'd = ', pMax

