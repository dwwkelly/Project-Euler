#!/usr/bin/python

import eulerlib

n = 10000


if __name__ == '__main__':

   ans = []
   for ii in xrange(0, n):
      d_ii = sum(eulerlib.propDivisors(ii))
      if (sum(eulerlib.propDivisors(d_ii)) == ii )and (d_ii != ii):
         ans.append(d_ii)
	 print d_ii, '  ', ii
   print sum(ans)
       
