import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

m, n, N = map(int, input().split())

ans = 0
while N >= m:
    ans += m
    N -= m
    N += n

ans += N

print(ans)

