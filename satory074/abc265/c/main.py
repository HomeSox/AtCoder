import collections as cl
import math

H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

n_visit = [[0] * (W + 2) for _ in range(H + 2)]

crnt = (0, 0)
while True:
    i, j = crnt

    if n_visit[i][j] >= 1:
        print(-1)
        exit()

    n_visit[i][j] += 1

    if G[i][j] == "U" and i != 0:
        crnt = (i - 1, j)
        continue

    if G[i][j] == "D" and i != H - 1:
        crnt = (i + 1, j)
        continue

    if G[i][j] == "L" and j != 0:
        crnt = (i, j - 1)
        continue

    if G[i][j] == "R" and j != W - 1:
        crnt = (i, j + 1)
        continue

    break

x, y = crnt
x += 1
y += 1
print(x, y)
