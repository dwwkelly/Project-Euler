#!/usr/bin/python

from eulerlib import num2List

finalSum = 0

for ii in xrange(2, 1000000):
    cumulativeSum = 0
    l = num2List(ii)
    for kk in l:
        cumulativeSum = cumulativeSum + kk ** 5
    
    if cumulativeSum == ii:
        finalSum = finalSum + cumulativeSum

print finalSum
