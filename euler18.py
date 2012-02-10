#!/usr/bin/python
import numpy as np

txt = open('files/triangle67.txt')

lines = list()
for ii in txt.readlines():
    kk = ii.rstrip('\n')
    kk = kk.split(' ')
    line = list()
    for x in kk:
        line.append(int(x))
    lines.append(line)

lines.reverse()

nlines = len(lines)

topLine = lines[0]
for ii in xrange(nlines-1):
    bottomLine = lines[ii+1]

    maxLine = list()
    for kk in xrange(len(bottomLine)):
        m = max(topLine[kk], topLine[kk+1])
        maxLine.append(m)

    topLine = [sum(pair) for pair in zip(maxLine, bottomLine)]

print topLine
