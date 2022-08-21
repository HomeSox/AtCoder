import collections as cl
import math

X, Y, N = map(int, input().split())

y = (N // 3) * Y
x = (N - (N // 3) * 3) * X
print(min(x + y, N * X))
