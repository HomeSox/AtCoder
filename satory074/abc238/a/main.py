import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n = int(input())

if 2 ** n > n ** 2:
    print('Yes')
else:
    print('No')
