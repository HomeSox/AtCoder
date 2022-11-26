import collections as cl
import math

S = input()
ans = 0
for s in S:
    if s == 'v':
        ans += 1

    if s == 'w':
        ans += 2

print(ans)
