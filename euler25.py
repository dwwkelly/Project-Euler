#!/usr/bin/python

from eulerlib import fibonacciCF
import io

if __name__ == '__main__':

    f = io.open('fibo.txt', 'w')

    for ii in range(1, 501):
        result = fibonacciCF(ii)
        f.write(unicode(ii) + u' ' + unicode(len(str(result))) + '\n')

    f.close()
