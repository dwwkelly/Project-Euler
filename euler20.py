#!/usr/bin/python

import eulerlib

def split(anInt):
    l = list(str(anInt))
    return [int(x) for x in l]


if __name__ == '__main__':
    print sum(split(eulerlib.factorial(100)))
