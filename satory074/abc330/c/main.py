import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

D = int(input())

ans = float("inf")
best_x, best_y = 0, 0

max_x = int(math.ceil(math.sqrt(D)))

for x in range(max_x + 1):
    C = x ** 2 - D

    if C >= 0:
        y = 0
    else:
        y1 = int(math.floor(math.sqrt(-C)))
        y2 = int(math.ceil(math.sqrt(-C)))

        if abs(y1 ** 2 + C) < abs(y2 ** 2 + C):
            y = y1
        else:
            y = y2

    diff = abs(x ** 2 + y ** 2 - D)
    if diff < ans:
        ans = diff
        best_x, best_y = x, y

print(ans)

