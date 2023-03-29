import collections as cl
import math

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0
for s in S:
    for t in T:
        if t == s[-3:]:
            ans += 1
            break

print(ans)
