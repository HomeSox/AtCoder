import math
import collections as cl
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N-K):
    if A[i+K] > A[i]:
        print('Yes')
    else:
        print('No')