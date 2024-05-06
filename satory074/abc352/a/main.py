import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, X, Y, Z = map(int, input().split())


if X <= Z <= Y or X >= Z >= Y:
    print("Yes")
else:
    print("No")
