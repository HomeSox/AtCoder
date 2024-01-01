import collections as cl
import math
from collections import deque

N = int(input())
MOD = 998244353

dp = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for d in range(2, N + 1):
    for i in range(1, 10):
        for j in range(max(1, i - 1), min(10, i + 2)):
            dp[d][j] += dp[d - 1][i]
            dp[d][j] %= MOD

print(sum(dp[N]) % MOD)
