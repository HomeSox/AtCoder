X, Y, Z = list(map(int, input().split()))
S = input()

dp = [[0, 0] for _ in range(len(S) + 1)]
dp[0][1] = Z

for i, s in enumerate(S):
    if s == "a":
        dp[i + 1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i + 1][1] = min(dp[i][1] + Y, dp[i][0] + Z + Y)
    else:
        dp[i + 1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i + 1][1] = min(dp[i][1] + X, dp[i][0] + Z + X)

print(min(dp[len(S)]))
