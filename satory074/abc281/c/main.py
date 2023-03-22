import collections as cl
import math

N, T = map(int, input().split())
A = list(map(int, input().split()))


mod = T % sum(A)

for i, a in enumerate(A):
    if mod < a:
        print(i + 1, mod)
        exit()
    else:
        mod -= a
