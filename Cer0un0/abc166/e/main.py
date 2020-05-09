#!/usr/bin/env python3

import collections
N = int(input())
A = list(map(int, input().split()))

L = []
R = []
for i in range(N):
    L.append(i+A[i])
    R.append(i-A[i])

C_L = collections.Counter(L)
C_R = collections.Counter(R)
ans = 0
for l, t in C_L.items():
    if l in C_R:
        ans += t*C_R[l]
print(ans)
