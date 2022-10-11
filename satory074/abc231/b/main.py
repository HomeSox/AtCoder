import math
import collections as cl
from collections import deque

N = int(input())
S = [input() for _ in range(N)]

ans = ''
ma = -1
for s in S:
    if ma < S.count(s):
        ma = S.count(s)
        ans = s

print(ans)
