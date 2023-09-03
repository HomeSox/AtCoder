import collections as cl
import math

n = int(input())
a = list(map(int, input().split()))

ans = 0
for a_ in a:
    if a_ in [1, 3, 7, 9]:
        continue

    if a_ in [2, 4, 8]:
        ans += 1
        continue

    if a_ in [5]:
        ans += 2
        continue

    if a_ in [6]:
        ans += 3
        continue

print(ans)