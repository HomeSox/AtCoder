import collections as cl
import math
from collections import deque

N, K = map(int, input().split())

ab = {}
sum_ = 0
for _ in range(N):
    a, b = map(int, input().split())
    ab[a] = b + ab.get(a, 0)

    sum_ += b

if sum_ <= K:
    print(1)
    exit()

ab = sorted(ab.items(), key=lambda x: x[0])

cur = 0
for a, b in ab:
    sum_ -= b

    if sum_ <= K:
        cur = a + 1
        break


print(cur)
