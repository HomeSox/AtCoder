import math
import collections as cl
from collections import deque

N = int(input())
A = list(map(int, input().split()))

A.sort()

if A == list(range(1, N+1)):
    print('Yes')
else:
    print('No')
