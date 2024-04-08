import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())

ans = ''
for i in range(N):
    if (i + 1) % 3 == 0:
        ans += 'x'
    else:
        ans += 'o'

print(ans)

