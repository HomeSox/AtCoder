import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

S = input()
a, b = map(int, input().split())
a -= 1
b -= 1

ans = ''
for i in range(len(S)):
    if i == a:
        ans += S[b]
        continue

    if i == b:
        ans += S[a]
        continue

    ans += S[i]

print(ans)
