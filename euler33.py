#!/usr/bin/python

from eulerlib import num2List
from eulerlib import gcd
from fractions import Fraction

fractionList = []

for numerator in range( 10, 100 ):
   for denomenator in range( 10, 100 ):
      divisor = gcd( numerator, denomenator )

      nL = num2List( numerator )
      dL = num2List( denomenator )

      if  dL[1] is not 0 and numerator < denomenator:
         if dL[0] in nL:
            f1 = Fraction( numerator, denomenator )
            nL.remove(dL[0])
            dL.remove(dL[0])
            f2 = Fraction( nL[0], dL[0] )

            if f1 == f2:
               fractionList.append(f1)
         elif  dL[1] in nL:
            f1 = Fraction( numerator, denomenator )
            nL.remove(dL[1])
            dL.remove(dL[1])
            f2 = Fraction( nL[0], dL[0] )

            if f1 == f2:
               fractionList.append(f1)


product = fractionList[0] * fractionList[1] * fractionList[2] * fractionList[3]
reducedProduct = product / gcd(product.numerator, product.denominator)
print reducedProduct.denominator
