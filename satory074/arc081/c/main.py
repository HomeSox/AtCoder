#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
l  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
c = collections.Counter(l)

cmc = c.most_common()

if cmc[0][1] == 1 or len(cmc) == 1:
    print(0)
else:
    cmc = sorted(cmc)[::-1]
    cmc = [(k, v) for k, v in cmc if v >= 2]
    print(cmc[0][0] * (cmc[0][0] if cmc[0][1] >= 4 else cmc[1][0]))

