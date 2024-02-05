import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

K = int(input())

print(f'{21 + (K // 60):02d}:{K - (K // 60) * 60:02d}')
