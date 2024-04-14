import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
A = list(map(int, input().split()))

print(sum(A) * -1)