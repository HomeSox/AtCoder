#!/usr/bin/env pypy3
import collections
import itertools as it
import math
#import numpy as np
 
s = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

sp = s[:len(s)//2]
sn = s[len(s)//2:]

#if len(sp) == len(sn):
#    sn = sn[1:]

ans = 0
#print(sp, sn[::-1])
for sp_, sn_ in zip(sp, sn[::-1]):
    #print(sp_, sn_)
    if sp_ != sn_:
        ans += 1

print(ans)
