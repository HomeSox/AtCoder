import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

K = int(input())

ans = ''
for i in range(K):
    ans += chr(ord('A') + i)

print(ans)
