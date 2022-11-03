import collections as cl
import math

N, M = map(int, input().split())

ans = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    kx = list(map(int, input().split()))
    k = kx[0]
    x = kx[1:]

    for x1 in x:
        for x2 in x:
            ans[x1][x2] += 1

for a in ans[1:]:
    for a_ in a[1:]:
        if a_ < 1:
            print("No")
            exit()
print("Yes")
