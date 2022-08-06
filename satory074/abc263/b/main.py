import collections as cl
import math

N = int(input())
P = list(map(int, input().split()))

oya = [-1 for _ in range(N + 1)]
for i, p in enumerate(P):
    oya[i + 2] = p

idx = N
ans = 0
while True:
    ans += 1

    if oya[idx] == 1:
        break

    idx = oya[idx]


print(ans)
