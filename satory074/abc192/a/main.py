import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

X = int(input())
print(100 - X % 100)
