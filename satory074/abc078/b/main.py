import math
import collections as cl
from collections import deque

X, Y, Z = map(int, input().split())

print(math.floor((X - Z) / (Y + Z)))

