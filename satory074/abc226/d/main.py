import collections as cl
from collections import deque
import math

N = int(input())

xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

pair = []
for x1, y1 in xy:
    for x2, y2 in xy:
        if x1 == x2 and y1 == y2:
            continue

        dx = x2 - x1
        dy = y2 - y1
        gcd_ = math.gcd(dx, dy)
        pair.append((dx // gcd_, dy // gcd_))

clc = cl.Counter(pair)
print(len(clc))
