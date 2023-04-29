import collections as cl
import math

import numpy as np

qlist = np.cumsum(list(range(10 ** 6 + 1)))
N = int(input())


ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    n = B - A
    ans += (n + 1) * A + qlist[n]

print(ans)
