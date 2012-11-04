#!/usr/bin/python

import string
import numpy as np

alphaDict = dict(zip(string.ascii_uppercase, range(1, 27)))

if __name__ == '__main__':

    f = open('files/names.txt')

    names = f.read()
    f.close()

    names = names.split(',')

    names = [x.strip('"').rstrip('"') for x in names]

    names.sort()

    nNames = len(names)
    multipliers = range(1, nNames + 1)

    nameNumber = list()
    for name in names:
       nameNumber.append(sum([alphaDict[x] for x in list(name)]))

    print sum(np.array(nameNumber) * np.array(multipliers))
