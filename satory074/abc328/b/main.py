import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    for d in range(1, D[i-1] + 1):
        s = str(i) + str(d)

        if len(set(list(s))) == 1:
            ans += 1

print(ans)


