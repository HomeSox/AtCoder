import math
import collections as cl
from collections import deque

N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(N)]

for i in range(N-1):
    if A[i] <= A[i+1]:
        ans[i] ^= 1
        ans[i+1] ^= 1

ans_ = 1000
kabu = 0
is_buy = True
for i in range(N):
    # print(ans_)
    if ans[i]:
        if is_buy:
            kabu = ans_ // A[i]
            ans_ -= kabu * A[i]
        else:
            ans_ += kabu * A[i]
            kabu = 0

        is_buy ^= 1

print(ans_)