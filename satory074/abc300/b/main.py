import collections as cl
import math

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

b = [b_ for b_ in B]
for i in range(H):
    b = [b[-1]] + b[:-1]

    b_ = [b__ for b__ in b]
    for j in range(W):
        b_ = [row[-1:] + row[:-1] for row in b_]

        if A == b_:
            print("Yes")
            exit()

print("No")
