import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


N = int(input())

A, T = 0, 0
for _ in range(N):
    t, a = map(int, input().split())
    T += t
    A += a

if A == T:
    print("Draw")
else:
    if A > T:
        print("Aoki")
    else:
        print("Takahashi")
