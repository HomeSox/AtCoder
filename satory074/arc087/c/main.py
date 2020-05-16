#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
a  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
c = collections.Counter(a)

ans = 0

for c_ in c.items():
    if c_[0] > c_[1]:
        ans += c_[1]
    elif c_[0] < c_[1]:
        ans += c_[1] - c_[0]

print(ans)
