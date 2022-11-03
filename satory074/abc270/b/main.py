import collections as cl
import math

X, Y, Z = map(int, input().split())

is_wall = True if 0 > Y > X or 0 < Y < X else False

if 0 < Y < X:
    if 0 < Y < Z:
        print(-1)
        exit()

if 0 > Y > X:
    if 0 > Y > Z:
        print(-1)
        exit()

if 0 < Y < X:
    print(abs(Z) + abs(X - Z))
    exit()
elif 0 > Y > X:
    print(abs(Z) + abs(X - Z))
    exit()
else:
    print(abs(X))
