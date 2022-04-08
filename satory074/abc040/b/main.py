import math
import collections as cl
from collections import deque

n = int(input())

ans = 10 ** 12
for tate in range(1, n + 1):
    for yoko in range(1, min(n // tate, tate) + 1):
        rest_ty = abs(tate - yoko)
        rest_tile = n - (tate * yoko)

        if ans > rest_ty + rest_tile:
            ans = rest_ty + rest_tile

print(ans)
