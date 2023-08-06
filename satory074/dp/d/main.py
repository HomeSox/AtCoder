import collections as cl
import math
from collections import deque

N, W = map(int, input().split())

wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        if j - wv[i - 1][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wv[i - 1][0]] + wv[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][W])
