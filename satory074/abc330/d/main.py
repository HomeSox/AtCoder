import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
S = [input() for _ in range(N)]

bi = [0] * N
bj = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            bi[i] += 1
            bj[j] += 1

res = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            res += (bi[i] - 1) * (bj[j] - 1)

print(res)
