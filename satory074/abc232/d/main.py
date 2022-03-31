import collections as cl
from collections import deque

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


f = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for h in range(H - 1, -1, -1):
    for w in range(W - 1, -1, -1):
        if C[h][w] == "#":
            continue

        f[h][w] = max(f[h + 1][w], f[h][w + 1]) + 1

print(f[0][0])
