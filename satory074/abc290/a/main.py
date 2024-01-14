import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for b in B:
    ans += A[b-1]

print(ans)