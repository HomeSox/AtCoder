import math
import collections as cl
from collections import deque

N, K, A = map(int, input().split())

ans = A
for _ in range(K - 1):
    # print(ans)
    if ans == N:
        ans = 1
    else:
        ans += 1

print(ans)
