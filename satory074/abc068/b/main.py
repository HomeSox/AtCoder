import collections as cl
import math

N = int(input())

wareru = 0
ans = 1
for n in range(1, N + 1):
    w = 0
    n_ = n
    for _ in range(10**9):
        if n_ % 2 == 0:
            n_ = n_ // 2
            w += 1
        else:
            break

    if wareru < w:
        wareru = w
        ans = n

    # print(n, w, wareru, ans)

print(ans)
