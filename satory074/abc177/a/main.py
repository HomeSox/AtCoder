import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

D, T, S = map(int, input().split())

if D / S <= T:
    print("Yes")
else:
    print("No")
