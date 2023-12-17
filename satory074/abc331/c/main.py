import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
A = list(map(int, input().split()))

clc = cl.Counter(A)
# print(clc)

l_nnum = [0 for _ in range(10 ** 6 + 1)]
for k, v in clc.items():
    l_nnum[k] = k * v

# 累積和
Q = [0 for _ in range(10 ** 6 + 1)]
for i in range(1, 10 ** 6 + 1):
    Q[i] = Q[i - 1] + l_nnum[i]

ans = []
for a in A:
    ans.append(Q[-1] - Q[a])

print(*ans)

