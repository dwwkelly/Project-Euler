#!/usr/bin/python

import eulerlib


lower = 12
upper = 28123

if __name__ == '__main__':

    abundantNumbers = list()

    for ii in xrange(1, upper + 1):
        if sum(eulerlib.propDivisors(ii) > ii):
            abundantNumbers.append(ii)

    abundantSums = list()
    for a in abundantNumbers:
        for b in abundantNumbers:
            if a + b < upper:
                abundantSums.append(a + b)

    abundantSums = sum(set(abundantSums))

    return
