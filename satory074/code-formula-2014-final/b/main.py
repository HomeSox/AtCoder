import math
import collections as cl
from collections import deque

n = int(input())

print(n // 2 + (0 if n % 2 == 0 else 3))