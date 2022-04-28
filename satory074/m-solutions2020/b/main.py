import math
import collections as cl
from collections import deque

A, B, C = map(int, input().split())
K = int(input())

for _ in range(K):
    if B >= C:
        C *= 2
        continue

    if A >= B:
        B *= 2

if A < B < C:
    print('Yes')
else:
    print('No')

