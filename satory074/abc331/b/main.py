import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, S, M, L = map(int, input().split())

ans = 10 ** 18
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i * 6 + j * 8 + k * 12 >= N:
                ans = min(ans, S * i + M * j + L * k)

print(ans)
