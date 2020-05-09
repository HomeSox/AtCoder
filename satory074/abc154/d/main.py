#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, k  = map(int, input().split())
p  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

q = sum(p[:k])
max_ = (q, 0, k)
for i in range(k, n):
    q = q + p[i] - p[i-k]
    if max_[0] < q:
        max_ = (q, i-k+1, i+1)

ans = 0
for p_ in p[max_[1]:max_[2]]:
    ans += 1 + (p_ - 1) * 0.5

#print(max_)
print(ans)
