#!/usr/bin/python


upperLimit = 100
A = range(2, upperLimit + 1)
B = range(2, upperLimit + 1)

combinations = set()

for ii in A:
    for kk in B:
        combinations.add(ii ** kk)


print len(combinations)
