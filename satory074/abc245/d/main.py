import collections as cl
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = []
for i in range(M + 1):
    b = C[N + M - i]

    for j in range(1, i + 1):
        if N - j >= 0:
            b -= A[N - j] * B[-j]

    B.append(b // A[N])

B = B[::-1]

print(*B)