import collections as cl
import math

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

for i, a in enumerate(A):
    if K <= 0:
        break

    if a >= X:
        diff = min(A[i] // X, K)
        K -= diff
        A[i] -= X * diff

A = sorted(A)[::-1]
# print(A, K)
print(sum(A[min(len(A), K) :]))

