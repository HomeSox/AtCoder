import math
import collections as cl
from collections import deque

N = int(input())
A = []
B = []
diff = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    diff -= a

X = [2 * a + b for a, b in zip(A, B)]
rX = sorted(X, reverse=True)

ans = 0
for x in rX:
    if diff > 0:
        break

    diff += x
    ans += 1

print(ans)
