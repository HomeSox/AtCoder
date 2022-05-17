import math
import collections as cl
from collections import deque

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

mi = 10 ** 9
ans = 10 ** 9
for i, h in enumerate(H):
    kion = T - h * 0.006
    if abs(A - kion) < mi:
        mi = abs(A - kion)
        ans = i + 1

print(ans)
