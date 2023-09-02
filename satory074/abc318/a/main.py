import collections as cl
import math

N, M, P = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    if i == M:
        ans += 1
        continue

    if (i - M) % P == 0:
        ans += 1

print(ans)