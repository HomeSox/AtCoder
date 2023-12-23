import collections as cl
import math

N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
i = 0
for j in range(len(A)):
    while i < len(A) and A[i] - A[j] < X:
        i += 1

    if i < len(A) and A[i] - A[j] == X:
        print("Yes")
        exit()

print("No")
