import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
    d = 1

    if m == M:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1

print(y, m, d)
