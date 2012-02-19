#!/usr/bin/python

coins = [1, 2, 5, 10, 20, 50, 100, 200]
maxCoins = 200
combs = [1] + [0] * maxCoins

for ii in coins:
    for kk in xrange(ii, maxCoins + 1):
        combs[kk] += combs[kk - ii]

print combs[-1]
