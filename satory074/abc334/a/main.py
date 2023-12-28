import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

B, G = map(int, input().split())

if B > G:
    print('Bat')
else:
    print('Glove')
