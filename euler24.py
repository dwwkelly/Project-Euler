#!/usr/bin/python

import eulerlib
import math

if __name__ == '__main__':

    n = 1000000
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nNums = len(nums)
    answer = list()

    while len(nums) > 1:
        f = eulerlib.factorial(nNums - 1)
        nNums -= 1
        tmp = int(math.ceil(float(n) / float(f)))
        answer.append(nums[tmp - 1])
        nums.remove(nums[tmp - 1])
        n -= f * (tmp - 1)

    answer.append(nums[0])

    print ''.join(map(str, answer))
