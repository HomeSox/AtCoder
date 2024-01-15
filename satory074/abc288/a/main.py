import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())

    print(A + B)

