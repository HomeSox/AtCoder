import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split())

if b == 10:
    if a == 1:
        print('Yes')
        exit()

if abs(a - b) == 1:
    print('Yes')
else:
    print('No')
