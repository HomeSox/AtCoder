import collections as cl
import math

N, M = map(int, input().split())
X = list(map(int, input().split()))

bonus = dict()
for _ in range(M):
    c, y = map(int, input().split())
    bonus[c] = y

dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(i + 1):
        v = dp[i][j]
        dp[i + 1][0] = max(dp[i + 1][0], v)

        if j + 1 in bonus:
            v += bonus[j + 1]

        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], v + X[i])

print(max(dp[-1]))
