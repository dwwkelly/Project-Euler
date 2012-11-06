#!/usr/bin/python

import eulerlib


primes = eulerlib.sieveOfEratosthenes( int( 1e6 ) )

truncatablePrimes = []

for prime in primes:

    if eulerlib.isTruncatable( prime, primes ) and prime not in [2, 3, 5, 7]:
        truncatablePrimes.append( prime )

    if len( truncatablePrimes ) == 11:
        break

print sum( truncatablePrimes )
