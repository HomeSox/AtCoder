import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

S = input()

for i, s in enumerate(S):
    if ord('A') <= ord(s) <= ord('Z'):
        print(i + 1)
        break

