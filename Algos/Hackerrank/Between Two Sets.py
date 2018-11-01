'''
https://www.hackerrank.com/challenges/between-two-sets/problem
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
'''

from functools import reduce
from math import gcd


def getTotalX(a, b):
    if len(a) > 1:
        lcm = reduce(lambda x, y: (x * y) // gcd(x, y), a)
    else:
        lcm = a[0]
    l = lcm
    count = 0
    while lcm <= min(b):
        if not all(i % lcm == 0 for i in b) or not lcm % l == 0:
            lcm += 1
            continue
        count += 1
        lcm += 1
    return count


print(getTotalX([2, 3, 6], [42, 84]))
