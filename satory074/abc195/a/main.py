import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

M, H = map(int, input().split())

if H % M == 0:
    print("Yes")
else:
    print("No")