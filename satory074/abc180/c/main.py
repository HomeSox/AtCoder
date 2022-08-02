import math
import collections as cl
from collections import deque

N = int(input())

def yakusuu(n):
    yakusuu = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yakusuu.append(i)
            if i != n // i:
                yakusuu.append(n // i)
    return yakusuu

[print(n) for n in sorted(yakusuu(N))]