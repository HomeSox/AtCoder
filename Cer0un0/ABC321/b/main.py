#!/usr/bin/env python3
import copy
N, X = map(int, input().split())
A = list(map(int, input().split()))
A2 = copy.copy(A)
for i in range(0, 101):
    A2.append(i)
    A2 = sorted(A2)
    if sum(A2[1:N-1]) >= X:
        print(i)
        exit()
    A2 = copy.copy(A)
print(-1)