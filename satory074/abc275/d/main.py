import collections as cl
import math
from functools import lru_cache

N = int(input())


@lru_cache
def f(n):
    # print(n)
    if n == 0:
        return 1
    else:
        return f(n // 2) + f(n // 3)


print(f(N))
