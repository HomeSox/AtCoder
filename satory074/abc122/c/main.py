#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = int(input())
n, q  = map(int, input().split())
s  = input()
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

nac = []
c = 0
for i, s_ in enumerate(s):
    if s[i] == 'C':
        if s[i-1] == 'A':
            c += 1

    nac.append(c)

#print(nac)

for _ in range(q):
    l, r = map(int, input().split())
    print(nac[r-1] - nac[l-1])
