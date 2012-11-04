#!/usr/bin/python

from eulerlib import sieveOfEratosthenes
from eulerlib import rotateInt
from eulerlib import nDigits

primes = sieveOfEratosthenes(1000000)
circPrimes = []

for ii in primes:
   iiLength = nDigits( ii )

   for kk in range( iiLength ):
      rotated = rotateInt( ii, kk )
      if rotated not in primes:
         continue
      else:
         primes.remove( rotated )

      if kk == iiLength - 1:
         circPrimes.append( ii )

print len( circPrimes )
