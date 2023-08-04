import math

N, K = map(int, input().split())
h = list(map(int, input().split()))

if N <= K:
    print(abs(h[N - 1] - h[0]))
    exit()

dp = [0 for _ in range(N + 1)]

for i in range(1, K + 1):
    dp[i] = abs(h[i] - h[0])

for i in range(K + 1, N):
    min_ = math.inf
    for k in range(1, K + 1):
        min_ = min(min_, dp[i - k] + abs(h[i] - h[i - k]))

    dp[i] = min_

# print(dp)
print(dp[N - 1])
