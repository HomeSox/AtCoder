#!/usr/bin/env pypy3
import collections
import itertools as it
import math
import numpy as np
 
#  = input()
#  = int(input())
yoko = [list(map(int, input().split())) for _ in range(3)]
is_flag = [False] * 9
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

yoko = list(np.array(yoko).flatten())

n = int(input())
for _ in range(n):
    b = int(input())

    if b in yoko:
        is_flag[yoko.index(b)] = True

is_flag = list(np.array(is_flag).reshape(3, 3))

line = is_flag # yoko
line += list(np.array(is_flag).T) # tate
line += [[line[0][0], line[1][1], line[2][2]], [line[0][2], line[1][1], line[2][0]]]

for l in line:
    if sum(l) == 3:
        print('Yes')
        break
else:
    print('No')
#print(yoko)
#print(tate)
#print(naname)
