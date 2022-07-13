import collections as cl
import math

N, M, X, T, D = map(int, input().split())


l = [0 for _ in range(200)]
l[N] = T

for i in range(N - 1, -1, -1):
    if i < X:
        l[i] = l[i + 1] - D
    else:
        l[i] = l[i + 1]

for i in range(N + 1, 199):
    if i < X:
        l[i] = l[i - 1] + D
    else:
        l[i] = l[i - 1]


print(l[M])
