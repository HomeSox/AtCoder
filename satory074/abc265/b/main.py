import collections as cl
import math

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [0] * (N + 2)
for _ in range(M):
    X, Y = map(int, input().split())
    XY[X] = Y

time = T
for i, a in enumerate(A):
    time -= a
    # print(time, a)

    if time <= 0:
        print("No")
        break

    time += XY[i + 2]
else:
    print("Yes")
