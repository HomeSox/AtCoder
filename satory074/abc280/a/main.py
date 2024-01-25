import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())

ans = 0
for _ in range(H):
    S = input()
    ans += S.count("#")

print(ans)
