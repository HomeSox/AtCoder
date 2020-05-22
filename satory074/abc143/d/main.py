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
# c = collections.Counter()

l = sorted(l)
#print(l)

ans = 0
for i1 in range(len(l)-2):
    a = l[i1]
    if a >= l[i1+1] + l[i1+2]:
        continue

    for i2 in range(i1+1, len(l)-1):
        b = l[i2]
        if b >= a + l[i2+1]:
            continue

        for i3 in range(len(l)-1, i2, -1):
            if l[i3] < a + b:
                #print(a, b, l[i3])
                ans += 1
            else:
                break

        #l_ = [l[i3] for i3 in range(i2+1, len(l[i2+1:]))]

print(ans)
