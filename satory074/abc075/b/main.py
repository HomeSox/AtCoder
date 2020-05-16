#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
h, w  = map(int, input().split())
#  = list(map(int, input().split()))
masu = [list(input()) for i in range(h)]
#
# c = collections.Counter()


dumy = ['.'] * w
masu.append(dumy)
masu.insert(0, dumy)


for i in range(h+2):
    masu[i] = ['.'] + masu[i] + ['.']

nbomb = [[0] * (w + 2) for _ in range(h+2)]

for i, line in enumerate(masu[1:-1]):
    for j, m in enumerate(line[1:-1]):
        if m == '#':
            i_ = i + 1
            j_ = j + 1
            nbomb[i_-1][j_-1] += 1
            nbomb[i_-1][j_-0] += 1
            nbomb[i_-1][j_+1] += 1
            nbomb[i_-0][j_-1] += 1
            nbomb[i_-0][j_+1] += 1
            nbomb[i_+1][j_-1] += 1
            nbomb[i_+1][j_-0] += 1
            nbomb[i_+1][j_+1] += 1

for ml, bl in zip(masu[1:-1], nbomb[1:-1]):
    ml = ml[1:-1]
    bl = bl[1:-1]

    for m_, b_ in zip(ml, bl):
        if m_ == '.':
            print(b_, end='')
        else:
            print('#', end='')
    print()
