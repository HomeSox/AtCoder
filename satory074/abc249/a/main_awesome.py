import collections as cl
import math

A, B, C, D, E, F, X = map(int, input().split())

tak = 0
aok = 0
for t in range(X):
    if t % (A + C) < A:
        tak += B

    if t % (D + F) < D:
        aok += E

if tak == aok:
    print("Draw")
elif tak > aok:
    print("Takahashi")
else:
    print("Aoki")
