import math
import collections as cl
from collections import deque

N, T = map(int, input().split())

l = []
total = 0
for i in range(N):
    a, b = map(int, input().split())

    l.append([i, a, b, a - b])
    total += a


# print(l)
l = sorted(l, key=lambda x: x[3], reverse=True)

if total <= T:
    print(0)
    exit()

ans = 0
for l_ in l:
    total -= l_[3]

    ans += 1

    if total <= T:
        break
else:
    print(-1)
    exit()

print(ans)
