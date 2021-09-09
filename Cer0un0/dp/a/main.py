#!/usr/bin/env python3

N = int(input())
H = list(map(int, input().split()))
dp = [float('inf')]*N
dp[0] = 0

for i in range(1, N):
    dp[i] = min(dp[i], dp[i-1] + abs(H[i]-H[i-1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i-2] + abs(H[i]-H[i-2]))

print(dp[N-1])
