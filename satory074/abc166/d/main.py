#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
x  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

for a in range(-500, 500):
    for b in range(-500, 500):
        if (a ** 5) - (b **5) == x:
            print(a, b)
            exit()
"""
for a in range(1, 10**9):
    b = abs((a**5 - x)**(1/5))
    #print(a, b, (b.is_integer()))

    if b.is_integer():
        b = int(b)
        if (a ** 5) - (-b ** 5) == x:
            print(a, -b)
        else:
            print(-a, b)

        break
"""
