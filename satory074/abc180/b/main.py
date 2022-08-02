import math
import collections as cl
from collections import deque

N = int(input())
x = list(map(int, input().split()))

ans = 0
for x_ in x:
    ans += abs(x_)

print(ans)

ans = 0
for x_ in x:
    ans += abs(x_) ** 2

print(ans ** 0.5)

print(max([abs(x_) for x_ in x]))