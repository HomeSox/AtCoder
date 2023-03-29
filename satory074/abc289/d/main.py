import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

is_mochi = [False for _ in range(X + 1)]
for b in B:
    is_mochi[b] = True

dp = [False] * (X + 1)
dp[0] = True

for i in range(1, X + 1):
    for a in A:
        if i >= a and dp[i - a] and not is_mochi[i]:
            dp[i] = True
            break

if dp[X]:
    print("Yes")
else:
    print("No")