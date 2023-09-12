import collections as cl
import math

A = int(input())

max_ = -1
for i in range(A):
    if i * (A - i) > max_:
        max_ = i * (A - i)

print(max_)
