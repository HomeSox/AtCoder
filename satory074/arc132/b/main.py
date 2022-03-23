import collections as cl
from collections import deque

n = int(input())
p = list(map(int, input().split()))

idx_1 = p.index(1)  # 1の位置
idx_1_right = (idx_1 + 1) % n  # 1の右隣のindex

if p[idx_1_right] == 2:  # asc
    print(min(idx_1, n - idx_1 + 2))
else:
    print(min(idx_1_right + 1, n - idx_1_right + 1))
