import collections as cl
import math

N, D = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
cur = 0
for d in range(D):
    for n in range(N):
        if S[n][d] == "x":
            ans = max(ans, cur)

            cur = 0

            break
    else:
        cur += 1

print(max(ans, cur))