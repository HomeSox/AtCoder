import math
import collections as cl
from collections import deque

S = input()

l = len(set(S))
if l == 1:
    print(1)
elif l == 2:
    print(3)
elif l == 3:
    print(6)
