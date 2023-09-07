import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

A.sort()

for i in range(min(A), max(A) + 1):
    if i not in A:
        print(i)
        break