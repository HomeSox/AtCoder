import collections as cl
import math

N, H, X = map(int, input().split())
P = list(map(int, input().split()))

min_ = max(P)
ans = 1
for i, p in enumerate(P):
    if (H + p) >= X:
        if p <= min_:
            min_ = p
            ans = i + 1

print(ans)
