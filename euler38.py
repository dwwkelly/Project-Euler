#!/usr/bin/python

import eulerlib

largest = 0

for kk in range(10, 10000):
    tmp = str( kk ) + str( 2 * kk )
    if len( tmp ) is 9:
        tmp = int(tmp)
        if eulerlib.isPandigital( tmp ) and tmp > largest:
            print kk
            largest = tmp


for kk in range(10, 10000):
    tmp = str( kk ) + str( 2 * kk ) + str( 3 * kk )
    if len( tmp ) is 9:
        tmp = int(tmp)
        if eulerlib.isPandigital( tmp ) and tmp > largest:
            print kk
            largest = tmp

for kk in range(10, 10000):
    tmp = str( kk ) + str( 2 * kk ) + str( 3 * kk ) + str( 4 * kk )
    if len( tmp ) is 9:
        tmp = int(tmp)
        if eulerlib.isPandigital( tmp ) and tmp > largest:
            print kk
            largest = tmp
print largest
