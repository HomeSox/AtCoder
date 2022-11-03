import collections as cl
import math

N, x, y = map(int, input().split())
A = list(map(int, input().split()))
A1 = A[2::2]
A2 = A[1::2]


def f(a, o, p):
    s = set([o])
    for n in a:
        l = set([])
        for n2 in s:
            l.add(n2 + n)
            l.add(n2 - n)

        s = l

    if p not in s:
        print("No")
        exit()


f(A1, A[0], x)
f(A2, 0, y)

print("Yes")
