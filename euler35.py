#!/usr/bin/python

from eulerlib import sieveOfEratosthenes
from eulerlib import rotateInt
from eulerlib import nDigits

primes = sieveOfEratosthenes(1000000)
#primes = sieveOfEratosthenes(100)
ncircPrimes = 0

digits = [[], [], [], [], [], []]

for ii in primes:
    n = nDigits( ii )
    digits[n - 1].append( ii )

for n in range(len(digits)):  # Loop over each bucket
    print n
    for m in digits[n]:  # Loop over the integers in each bucket
        isCircPrime = True
        for l in range(n + 1):  # Loop over the rotations of each number
            if rotateInt(m, l) not in digits[n]:
                break
        else:
            ncircPrimes = ncircPrimes + 1

print ncircPrimes
