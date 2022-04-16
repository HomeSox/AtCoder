import collections as cl
import math

A, B, K = map(int, input().split())

ans = 0
sum_ = A
for i in range(10**9):
    if sum_ >= B:
        print(ans)
        break
    else:
        sum_ *= K
        ans += 1
