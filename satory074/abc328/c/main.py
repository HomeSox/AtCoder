import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())
S = input()

q = [0 for _ in range(N + 1)]
for i in range(N):
    q[i+1] = q[i]
    is_tonari = False

    if i != 0:
        if S[i] == S[i-1]:
            is_tonari = True

    # if i != N - 1:
        # if S[i] == S[i + 1]:
            # is_tonari = True

    if is_tonari:
        q[i + 1] += 1

# print(q)

for _ in range(Q):
    l, r = list(map(int, input().split()))

    print((q[r] - q[l]))

