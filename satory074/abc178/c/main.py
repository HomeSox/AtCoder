import math
import collections as cl
from collections import deque

N = int(input())

MOD = 10 ** 9 + 7
print((10 ** N - 9 ** N - 9 ** N + 8 ** N) % MOD)
