#!/usr/bin/python

import eulerlib


def getPlace(anInt):
    digits = list()
    n = eulerlib.nDigits(anInt)

    tmpInt = anInt

    for ii in xrange(n):
        aDigit = tmpInt % 10
        tmpInt = ( tmpInt - aDigit ) / ( 10 )
        digits.append( aDigit )

    digits.reverse()
    return digits


if __name__ == '__main__':

    ones = {1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            0: ''}

    tens = {1: '',
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety',
            0: ''}

    hundreds = {1: 'onehundred',
                2: 'twohundred',
                3: 'threehundred',
                4: 'fourhundred',
                5: 'fivehundred',
                6: 'sixhundred',
                7: 'sevenhundred',
                8: 'eighthundred',
                9: 'ninehundred',
                0: ''}

    thousands = {1: 'onethousand'}

    teens = {0: 'ten',
             1: 'eleven',
             2: 'twelve',
             3: 'thirteen',
             4: 'fourteen',
             5: 'fifteen',
             6: 'sixteen',
             7: 'seventeen',
             8: 'eighteen',
             9: 'nineteen'}

    duds = {0: '',
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: '',
            8: '',
            9: ''}

    dicts = [ones, tens, hundreds, thousands]

    number = 1000
    nChars = 0

    for ii in xrange( 1, number + 1 ):
        counter = 0

        digitList = getPlace(ii)
        if len(digitList) > 1:
            digitList.reverse()
            tmpDigit = digitList[1] * 10 + digitList[0]
            digitList.reverse()
            if tmpDigit > 9 and tmpDigit < 20:
                dicts[1] = duds
                dicts[0] = teens
            else:
                dicts[0] = ones
                dicts[1] = tens

        numberStr = ''

        digitList.reverse()
        for kk in digitList:
            numberStr = dicts[counter][kk] + numberStr
            counter = counter + 1

        if len(digitList) == 3 and ii % 100 != 0:
            numberStr = numberStr + 'and'

        nChars = nChars + len(numberStr)

    print nChars
