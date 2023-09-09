import collections as cl
import math

N = int(input())

ans = ""
for i in range(N + 1):
    l = []
    for j in range(1, 10):
        if i % (N / j) == 0:
            l.append(j)

    if l:
        ans += str(min(l))
    else:
        ans += "-"


print(ans)

