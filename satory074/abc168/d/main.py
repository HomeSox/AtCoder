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


node = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

chikai = [[-1, 10**9] for _ in range(n+1)]
chikai[1][0] = [-1, 0]

def set_shirube(n, v):
    for n_ in node[n]:
        print(n, n_, v, chikai[n][1], chikai[n_][1] == 10**9)
        if chikai[n_][1] == 10**9:
            chikai[n_] = [n, v]
            set_shirube(n_, v+1)
        else:
            if v 
            chikai[n].append([n_, v])

set_shirube(1, 1)
print(chikai)

for l in chikai[1:]:
    r, v = l
    if v == 0:
        print('Yes')
    else:
        print(r)
