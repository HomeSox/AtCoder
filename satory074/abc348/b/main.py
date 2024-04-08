import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())

XY = []
for i in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))

for i in range(N):
    x1, y1 = XY[i]

    ma = -1
    ans = 0
    for j in range(N):
        if i == j:
            continue

        x2, y2 = XY[j]

        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if dist > ma:
            ma = dist
            ans = j + 1

    print(ans)

