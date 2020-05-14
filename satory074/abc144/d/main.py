#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a, b, x  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()


def f(a, b, x):
    """
    """
    if a * a * b / 2 <= x:
        return math.atan(2 * (a * a * b - x) / (a * a * a))
    else:
        return math.pi / 2 - math.atan(2 * x / (a * b * b))

#print(f(a, b, x) * 180 / math.pi)
print(math.degrees(f(a, b, x)))
