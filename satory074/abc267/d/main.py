import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[math.inf * -1] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(M + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + A[i - 1] * j, dp[i - 1][j])

print(dp[N][M])
