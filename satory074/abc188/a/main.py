import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

X, Y = map(int, input().split())

if abs(X - Y) < 3:
    print("Yes")
else:
    print("No")
