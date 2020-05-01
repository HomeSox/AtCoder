#!/usr/bin/env pypy3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, k  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = 0

for i in range(1, n+1):
    for ntoss in range(10000000):
        #print(i, ntoss)
        if i * (2 **  ntoss) >= k:
            ans += (1 / n) * ((1 / 2) ** ntoss)
            break
    # n_omote = int(math.ceil(math.log(k, 2)))
print(ans)
