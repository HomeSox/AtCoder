import collections as cl
import math

N, A, B = map(int, input().split())

for i in range(N):
    s = ""
    for j in range(N):
        if (i + j) % 2 == 0:
            s += "." * B
        else:
            s += "#" * B

    for _ in range(A):
        print(s)
