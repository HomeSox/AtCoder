import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, X = map(int, input().split())
S = list(map(int, input().split()))

ans = 0
for s in S:
    if s <= X:
        ans += s

print(ans)
