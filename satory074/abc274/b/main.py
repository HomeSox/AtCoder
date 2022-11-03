import collections as cl
import math

import numpy as np

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
C = np.array(C).T

ans = []
for c in C:
    ans.append(list(c).count("#"))

print(*ans)
