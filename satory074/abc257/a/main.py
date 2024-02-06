import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, X = map(int, input().split())

s = ''
for i in range(26):
    s += chr(ord('A') + i) * N

print(s[X - 1])

