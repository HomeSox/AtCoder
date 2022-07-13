import collections as cl
import numpy as np

H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]

A = list(np.array(A).T)

for a in A:
    print(*a)
