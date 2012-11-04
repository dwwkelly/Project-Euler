#!/usr/bin/python

from eulerlib import factorial
from eulerlib import num2List

answerL = []
facts = {}
for ii in range( 0, 10 ):
   facts[ii] = factorial( ii )

for ii in range( 3, 999999 ):
   s = 0
   iiL = num2List(ii)
   for kk in iiL:
      s += facts[kk]

   if s == ii:
      answerL.append( s )

print sum( answerL )
