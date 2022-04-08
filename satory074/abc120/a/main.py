import math
import collections as cl
from collections import deque

A, B, C = map(int, input().split())

print(min(B // A, C))
