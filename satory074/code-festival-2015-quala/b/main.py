import math
import collections as cl
from collections import deque

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans = ans * 2 + a

    # print(a, ans)

print(ans)
