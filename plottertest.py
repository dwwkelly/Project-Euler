#!/usr/bin/python

import collections
import random
import timeit

import matplotlib.pyplot as pyplot

MICROSECONDS_PER_SECOND = 1E6
FUNS = []
def test_fun(fun):
    FUNS.append(fun)
    return fun

@test_fun
def with_map(nums):
    return int(''.join(map(str, nums)))

@test_fun
def with_interpolation(nums):
    return int(''.join('%d' % num for num in nums))

@test_fun
def with_genexp(nums):
    return int(''.join(str(num) for num in nums))

@test_fun
def with_sum(nums):
    return sum(digit * 10 ** (len(nums) - 1 - i)
        for i, digit in enumerate(nums))

@test_fun
def with_reduce(nums):
    return int(reduce(lambda x, y: x + str(y), nums, ''))

@test_fun
def with_builtins(nums):
    return int(filter(str.isdigit, repr(nums)))

@test_fun
def with_accumulator(nums):
    tot = 0
    for num in nums:
        tot *= 10
        tot += num
    return tot

def time_test(digit_count, test_count=10000):
    """
    :return: Map from func name to (normalized) microseconds per pass.
    """
    print 'Digit count:', digit_count
    nums = [random.randrange(1, 10) for i in xrange(digit_count)]
    stmt = 'to_int(%r)' % nums
    result_by_method = {}
    for fun in FUNS:
        setup = 'from %s import %s as to_int' % (__name__, fun.func_name)
        t = timeit.Timer(stmt, setup)
        per_pass = t.timeit(number=test_count) / test_count
        per_pass *= MICROSECONDS_PER_SECOND
        print '%20s: %.2f usec/pass' % (fun.func_name, per_pass)
        result_by_method[fun.func_name] = per_pass
    return result_by_method

if __name__ == '__main__':
    pass_times_by_method = collections.defaultdict(list)
    assert_results = [fun([1, 2, 3]) for fun in FUNS]
    assert all(result == 123 for result in assert_results)
    digit_counts = range(1, 100, 2)
    for digit_count in digit_counts:
        for method, result in time_test(digit_count).iteritems():
            pass_times_by_method[method].append(result)
    for method, pass_times in pass_times_by_method.iteritems():
        pyplot.plot(digit_counts, pass_times, label=method)
    pyplot.legend(loc='upper left')
    pyplot.xlabel('Number of Digits')
    pyplot.ylabel('Microseconds')
    pyplot.show()
