import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

S = input()

stack = []

for s in S:
    if s == 'C' and stack[-2:] == ['A', 'B']:
        stack.pop()
        stack.pop()
    else:
        stack.append(s)

print(''.join(stack))
