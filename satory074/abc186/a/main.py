import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, W = map(int, input().split())

print(N // W)
