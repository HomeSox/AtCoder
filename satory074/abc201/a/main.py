import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

A = list(map(int, input().split()))
A.sort()

if A[2] - A[1] == A[1] - A[0]:
    print("Yes")
else:
    print("No")

