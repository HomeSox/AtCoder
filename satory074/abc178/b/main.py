import math
import collections as cl
from collections import deque

a, b, c, d = map(int, input().split())

print(max([a*c, a*d, b*c, b*d]))
