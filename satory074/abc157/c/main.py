#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, m  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

sc = [tuple(map(int, input().split())) for _ in range(m)]

#print(sc)

start = 0 if n == 1 else 10 ** (n-1)
for i in range(start, 10**(n)):
    ans = str(i)

    for s, c in sc:
        #print(s,c,ans)
        if ans[s-1] != str(c):
            break
    else:
        print(ans)
        break
else:
    print(-1)
