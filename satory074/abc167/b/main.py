#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a, b, c, k  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = 0
if a <= k:
    ans += a
    k -= a
else:
    print(k)
    exit()

if b <= k:
    k -= b
else:
    print(ans)
    exit()

if c <= k:
    ans -= c
else:
    print(ans - k)
    exit()

print(ans)
