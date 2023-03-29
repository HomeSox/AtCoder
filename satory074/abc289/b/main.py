import collections as cl
import math

N, M = map(int, input().split())
a = list(map(int, input().split()))

l = []
a_ = -1
ans = []
for i in range(1, N+1):
    l.append(i)

    if i not in a:
        ans += l[::-1]
        l = []

print(*ans)
