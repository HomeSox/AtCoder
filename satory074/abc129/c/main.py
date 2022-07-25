MOD = 10 ** 9 + 7

N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
a = a + [N+1]
a = set(a)

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    if i + 1 not in a:
        dp[i+1] += dp[i]
        dp[i+1] %= MOD

    if i + 2 not in a:
        dp[i+2] += dp[i]
        dp[i+2] %= MOD

print(dp[N])