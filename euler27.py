#!/usr/bin/python

from eulerlib import sieveOfEratosthenes
from eulerlib import howManyPrimes

n = 1000
print "for n = 1000, n^2 = ", n ** 2

p = sieveOfEratosthenes(n)
print "for p = ", len(p), ", p^2 = ", len(p) ** 2


p.reverse()
p.append(1)
maxPrime = 0
aMax = 0
bMax = 0

for ii in p:
    for kk in p:
        howMany1 = howManyPrimes(ii, kk)
        howMany2 = howManyPrimes(-ii, kk)
        howMany3 = howManyPrimes(ii, -kk)
        howMany4 = howManyPrimes(-ii, -kk)
        howManyMax = max([howMany1, howMany2, howMany3, howMany4])
        if howManyMax > maxPrime:
            maxPrime = howManyMax
            aMax = ii
            bMax = kk

print maxPrime, ', ', aMax, ', ', bMax, ', ', aMax  bMax
