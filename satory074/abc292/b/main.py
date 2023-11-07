import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())

n_yellow = [0 for _ in range(N + 1)]

for i in range(Q):
    n, x = map(int, input().split())

    if n == 1:
        n_yellow[x] += 1
        continue

    if n == 2:
        n_yellow[x] += 2
        continue

    if n == 3:
        if n_yellow[x] >= 2:
            print("Yes")
        else:
            print("No")

        continue


