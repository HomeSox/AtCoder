import collections as cl
import math

N = int(input())
T = list(map(int, input().split()))

ans = 0
for t in T:
    ans = (ans // (2**t) + 1) * (2**t)

    if ans % (2 ** (t + 1)) == 0:
        ans += 2**t

print(ans)
