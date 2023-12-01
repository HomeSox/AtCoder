import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

l = []
for a in a:
    if a >= L and a <= R:
        l.append(a)
        continue

    if a < L:
        l.append(L)
        continue

    if a > R:
        l.append(R)
        continue

print(*l)