import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

V, T, S, D = map(int, input().split())

if V * T <= D <= V * S:
    print("No")
else:
    print("Yes")