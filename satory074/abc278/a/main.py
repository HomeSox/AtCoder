import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    A = A[1:] + [0]

print(*A)

