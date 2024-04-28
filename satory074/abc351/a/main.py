import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sum(A) - sum(B) + 1)

