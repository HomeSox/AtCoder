#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
ab  = [tuple(map(int, input().split())) for _ in range(n)]
ba = [(b, a) for (a, b) in ab]
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ba = sorted(ba)
#print(ba)

qa = 0
for (b, a) in ba:
    qa += a

    if qa > b:
        print('No')
        break
else:
    print('Yes')
