import math
import collections as cl
from collections import deque

N = int(input())
h = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    prev1 = dp[i-1] + abs(h[i] - h[i-1])
    prev2 = dp[i-2] + abs(h[i] - h[i-2])

    dp[i] = min(prev1, prev2)

print(dp[N-1])
