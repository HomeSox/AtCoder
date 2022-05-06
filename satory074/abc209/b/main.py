import math
import collections as cl
from collections import deque

N, X = map(int, input().split())
A = list(map(int, input().split()))

if X >= sum(A) - (len(A) // 2):
    print('Yes')
else:
    print('No')

