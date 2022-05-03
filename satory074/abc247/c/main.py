import collections as cl
import math

N = int(input())


def f(n):
    if n == 1:
        return [1]

    n_1 = f(n - 1)
    return n_1 + [n] + n_1


print(*f(N))
