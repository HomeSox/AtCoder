import math
import collections as cl
from collections import deque

A, B, C, X = map(int, input().split())

if X <= A:
    print(1)
elif A < X <= B:
    print(C / (B - A))
else:
    print(0)