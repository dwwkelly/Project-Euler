#!/usr/env/python

import eulerlib

if __name__ == '__main__':
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = {7: 'monday', 1: 'tuesday', 2: 'wendesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday'}
    nYears = 100
    nMonths = 12
    nSundays = 0

    remainingDays = 0
    for ii in xrange(nYears):
        if eulerlib.isLeapYear(ii + 1901):
            months[2] = 29
        else:
            months[2] = 28

        for kk in xrange(nMonths):
            remainingDays = (remainingDays + months[kk + 1]) % 7
            if days[remainingDays + 1] == 'sunday':
                nSundays = nSundays + 1

    print nSundays
