import collections as cl
import math

N = int(input())
A = [list(input()) for _ in range(N)]

B = [[s for s in l] for l in A]

B[0][0] = A[1][0]
for i in range(N - 1):
    B[0][i + 1] = A[0][i]

for i in range(1, N - 1):
    B[i][0] = A[i + 1][0]
    B[i][-1] = A[i - 1][-1]

B[-1][-1] = A[-2][-1]
for i in range(N - 1):
    B[-1][i] = A[-1][i + 1]

for b in B:
    print(''.join(b))