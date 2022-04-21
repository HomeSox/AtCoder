from collections import deque

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

que = deque(A)

dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0][que.popleft()] = 1

for i in range(1, N):
    a = que.popleft()
    for j in range(10):
        if dp[i - 1][j] != 0:
            dp[i][(j + a) % 10] = (dp[i][(j + a) % 10] + dp[i - 1][j]) % MOD
            dp[i][(j * a) % 10] = (dp[i][(j * a) % 10] + dp[i - 1][j]) % MOD

[print(dp[N - 1][k]) for k in range(10)]
