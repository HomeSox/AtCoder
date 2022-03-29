import collections as cl
from collections import deque

N, M = map(int, input().split())

print(min((N * 2 + M) // 4, M // 2))
