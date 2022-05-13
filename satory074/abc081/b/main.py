import math
import collections as cl
from collections import deque

N = int(input())
A = list(map(int, input().split()))

ans = 0
for _ in range(10 ** 9):
    for a in A:
        if a % 2 == 1:
            break
    else:
        ans += 1

        A = [a // 2 for a in A]

        continue

    break

print(ans)
