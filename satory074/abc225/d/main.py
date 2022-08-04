import math
import collections as cl
from collections import deque

N, Q = map(int, input().split())

chain_idx_front = [-1] * (N + 1)
chain_idx_back = [-1] * (N + 1)
for _ in range(Q):
    arg = list(map(int, input().split()))
    c = arg[0]

    if c == 3:
        x = arg[1]
    else:
        x, y = arg[1], arg[2]

    if c == 1:
        chain_idx_front[y] = x
        chain_idx_back[x] = y
    elif c == 2:
        chain_idx_front[y] = -1
        chain_idx_back[x] = -1
    elif c == 3:
        ans = []

        idx = x
        while chain_idx_front[idx] != -1:
            idx = chain_idx_front[idx]

        ans.append(idx)

        while chain_idx_back[idx] != -1:
            idx = chain_idx_back[idx]
            ans.append(idx)

        print(len(ans), *ans)
