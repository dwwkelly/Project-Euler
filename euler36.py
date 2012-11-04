#!/usr/bin/python

from eulerlib import isPalindrome


twoBasePalindromes = []

for ii in range( int( 1e6 ) ):
    if isPalindrome( ii ):
        if isPalindrome( int(bin(ii)[2:])):
            twoBasePalindromes.append( ii )

print sum(twoBasePalindromes)
