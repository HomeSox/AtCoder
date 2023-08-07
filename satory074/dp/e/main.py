N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[float("inf") for _ in range(100001)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(100001):
        if j - wv[i - 1][1] >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - wv[i - 1][1]] + wv[i - 1][0])
        else:
            dp[i][j] = dp[i - 1][j]

ans = 100000
while dp[N][ans] > W:
    ans -= 1

print(ans)
