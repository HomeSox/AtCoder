import collections as cl
import math

N, x, y = map(int, input().split())
A = list(map(int, input().split()))
A1 = A[0::2]
A2 = A[1::2]


def f(l):
    clc = cl.Counter(l)
    print(clc)


print(f(A1))
