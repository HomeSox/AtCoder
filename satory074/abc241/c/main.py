import collections as cl
import math

N = int(input())
S = [input() for _ in range(N)]


def calc(x, y, dx, dy):
    c = 0
    for i in range(6):
        if not (0 <= min(x, y) and max(x, y) < N):
            return False

        if S[x][y] == "#":
            c += 1

        x += dx
        y += dy

    return c >= 4


dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]
for x in range(N):
    for y in range(N):
        for dx_, dy_ in zip(dx, dy):
            if calc(x, y, dx_, dy_):
                print("Yes")
                exit()

print("No")
