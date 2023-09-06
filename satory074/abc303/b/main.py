import collections as cl
import math

N, M = map(int, input().split())

l = {}
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            continue

        l[a * 100 + b] = False

for _ in range(M):
    a = list(map(int, input().split()))

    for a1, a2 in zip(a[:-1], a[1:]):
        l[a1 * 100 + a2] = True
        l[a2 * 100 + a1] = True

ans = 0
for l_ in l.values():
    if not l_:
        ans += 1

print(ans // 2)
