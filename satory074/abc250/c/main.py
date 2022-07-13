import collections as cl
import math

N, Q = list(map(int, input().split()))
x = [int(input()) for _ in range(Q)]

ans = [i for i in range(N + 1)]
inv = [i for i in range(N + 1)]

for i, x_ in enumerate(x):
    posX = inv[x_]
    posY = posX + 1

    if posY == N + 1:
        posY = N - 1

    posZ = ans[posY]

    ans[posX], ans[posY] = ans[posY], ans[posX]
    inv[x_], inv[posZ] = inv[posZ], inv[x_]

print(*ans[1:])
