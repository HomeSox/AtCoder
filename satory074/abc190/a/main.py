import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

A, B, C = map(int, input().split())

if (A + C) - B > 0:
    print('Takahashi')
else:
    print('Aoki')
