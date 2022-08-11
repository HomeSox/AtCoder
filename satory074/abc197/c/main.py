import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 10
for i in range(1 << (N - 1)):
    xor_ = 0
    or_ = 0
    for j in range(N):
        or_ |= A[j]
        if i >> j & 1:
            xor_ ^= or_
            or_ = 0

    xor_ ^= or_
    ans = min(ans, xor_)

print(ans)
