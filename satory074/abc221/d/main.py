import collections as cl
import math

N = int(input())

AB = [tuple(map(int, input().split())) for _ in range(N)]


x = sorted([(a, 1) for a, b in AB] + [(a + b, -1) for a, b in AB])

c = 0
ans = [0 for _ in range(N + 1)]
for i in range(len(x) - 1):
    c += x[i][1]
    ans[c] += x[i + 1][0] - x[i][0]

print(*ans[1:])
