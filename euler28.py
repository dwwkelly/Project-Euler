#!/usr/bin/python

#
#        43 44 45 46 47 48 49
#        42 21 22 23 24 25 26
#        41 20  7  8  9 10 27
#        40 19  6  1  2 11 28
#        39 18  5  4  3 12 29
#        38 17 16 15 14 13 30
#        37 36 35 34 33 32 31
#
# 1 + 3 + 7 + 13 + 21 + 31 + 43 + 57 + 73 + ... + 1001
#
# 1 + 5 + 9 + 17 + 25 + 37 + 49 + 65 + 76 + ... + 1001

if __name__ == "__main__":

    loopCount = 0
    last = 1
    upperLimit = 1001
    current = 1
    nums = []

    while loopCount < upperLimit:
        current = current + (loopCount * 2)
        nums.append(current)
        loopCount = loopCount + 1

    current = 1
    loopCount = 0

    while loopCount <= 500:
        current = current + 4 * loopCount
        nums.append(current)
        current = current + 4 * loopCount
        nums.append(current)
        loopCount = loopCount + 1

    print sum(nums) - 2  # 1 get counted three times so subtract two of them
