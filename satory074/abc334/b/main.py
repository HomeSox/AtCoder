import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

A, M, L, R = map(int, input().split())

L -= A
R -= A
# print(A, M, L, R)

print(R // M - (L - 1) // M)