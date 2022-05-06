import math
import collections as cl
from collections import deque

A, B = list(map(int, input().split()))

if  A > B:
    print(0)
else:
    print(B - A + 1)

