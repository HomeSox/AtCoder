import collections as cl
import math


N = int(input())
sx, sy, tx, ty = map(int, input().split())

circles = [list(map(int, input().split())) for _ in range(N)]

mat = [[False for _ in range(N)] for _ in range(N)]

for i1, circle1 in enumerate(circles):
    x1, y1, r1 = circle1
    for i2, circle2 in enumerate(circles):
        x2, y2, r2 = circle2

        print(x2 - r1, x1 - r1, x2 + r1, x1 + r1)
        print(y2 - r1, y1 - r1, y2 + r1, y1 + r1)
        print()

        if ((x2 - r1) <= (x1 - r1) <= (x2 + r1) <= (x1 + r1)) or (
            (y2 - r2) <= (y1 - r1) <= (y2 + r2) <= (y1 + r1)
        ):
            mat[i1][i2] = True
            mat[i2][i1] = True

print(mat)
