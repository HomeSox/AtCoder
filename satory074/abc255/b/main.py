import collections as cl
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

X = []
Y = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

ans = 0
for i in range(N):
    d = 10**18
    for a in A:
        d_ = ((X[i] - X[a - 1]) ** 2 + (Y[i] - Y[a - 1]) ** 2) ** 0.5

        d = min(d, d_)

    ans = max(ans, d)

print(ans)
