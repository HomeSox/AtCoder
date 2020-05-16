#!/usr/bin/env python3
import collections
N = int(input())
A = list(map(int, input().split()))

C = collections.Counter(A)
ans = 0
for v, c in C.items():
    if v > c:
        ans += c
    else:
        ans += c-v
print(ans)
