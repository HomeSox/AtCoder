#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, m  = map(int, input().split())
h  = list(map(int, input().split()))
ab  = [tuple(map(int, input().split())) for i in range(m)]
#
# c = collections.Counter()

ans = 0
tenbo = [0] * n
for (a, b) in ab:
    #print(tenbo)
    if h[a-1] > h[b-1]:
        if tenbo[a-1] != -1:
            tenbo[a-1] = 1
        tenbo[b-1] = -1
    if h[a-1] < h[b-1]:
        if tenbo[b-1] != -1:
            tenbo[b-1] = 1
        tenbo[a-1] = -1
    if h[a-1] == h[b-1]:
        tenbo[a-1] = -1
        tenbo[b-1] = -1

for tenbo_ in tenbo:
    if tenbo_ == 1 or tenbo_ == 0:
        ans += 1

print(ans)
