MOD = 998244353
N, M, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K + 1):
        for k in range(1, M + 1):
            if j - k >= 0:
                dp[i + 1][j] += dp[i][j - k]

            dp[i + 1][j] %= MOD

print(sum(dp[N]) % MOD)
