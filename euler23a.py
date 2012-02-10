#!/usr/bin/python

import euler21
import numpy as np
import time

lower=12
upper=28123

if __name__ == '__main__':

   startTime = time.time()
   abundantNumbers=list()

   for ii in xrange(1, upper+1):
   	if sum(euler21.propDivisors(ii)) > ii:
	   abundantNumbers.append(ii)

   sumAbundantNumbers = sum(set(n1+n2 for n1 in abundantNumbers for n2 in abundantNumbers if (n1+n2) < (upper+1)))

   sumAllNumbers = sum(range(1,upper+1))

   print time.time() - startTime
   print sumAllNumbers - sumAbundantNumbers
