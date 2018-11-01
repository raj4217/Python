'''
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''

import datetime

# Complete the dayOfProgrammer function below.


def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            return (datetime.datetime(2000, 1, 1) + datetime.timedelta(255)).strftime("%d.%m.%Y").replace('2000', str(year))
        else:
            return (datetime.datetime(2001, 1, 1) + datetime.timedelta(255)).strftime("%d.%m.%Y").replace('2001', str(year))
    if year == 1918:
        return (datetime.datetime(year, 2, 14) + datetime.timedelta(255 - 31)).strftime("%d.%m.%Y")
    else:
        return (datetime.datetime(year, 1, 1) + datetime.timedelta(255)).strftime("%d.%m.%Y")
