import collections as cl
from collections import deque

N = int(input())

L = []
for _ in range(N):
    l = list(map(int, input().split()))
    L.append(tuple(l[1:]))

clc = cl.Counter(L)
print(len(clc))
