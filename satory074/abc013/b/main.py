import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

a = int(input())
b = int(input())

print(min(abs(a - b) % 10, 10 - abs(a - b) % 10))