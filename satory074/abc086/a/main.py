import math
import collections as cl
from collections import deque

a, b = map(int, input().split())

if (a * b) % 2 == 0:
    print('Even')
else:
    print('Odd')
