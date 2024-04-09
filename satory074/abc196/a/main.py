import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split())
c, d = map(int, input().split())

print(max(b - c, b - d, a - c, a - d))
