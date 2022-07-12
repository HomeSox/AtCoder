import math
import collections as cl
from collections import deque

N = int(input())
a = list(map(int, input().split()))

ans = 10 ** 6
for n in range(-100, 101):
    cost = 0
    for a_ in a:
        cost += (a_ - n) ** 2

    if ans > cost:
        ans = cost

print(ans)
