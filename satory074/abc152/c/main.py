#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
p  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = 0
min_ = 10**9
for i in range(n):
    if p[i] < min_:
        ans += 1
        min_ = p[i]

print(ans)

