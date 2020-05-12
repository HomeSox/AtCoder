#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, m  = map(int, input().split())
x  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

x.sort()
q = [x1 - x2 for x1, x2 in zip(x[1:], x[:-1])]
q = sorted(q)[::-1]

print(sum(q[n-1:]))

