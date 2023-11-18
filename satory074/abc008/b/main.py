import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())

l = []
for _ in range(N):
    l.append(input())

l_ = cl.Counter(l)
print(cl.Counter(l_).most_common()[0][0])


