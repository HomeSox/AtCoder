import collections as cl
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = math.inf * -1

tmp = 0
for i in range(1, M + 1):
    tmp += i * A[i - 1]

ans = tmp

minus = sum(A[:M])
for i in range(N - M):
    tmp = tmp - minus + (A[M + i] * M)
    ans = max(ans, tmp)

    minus = minus - A[i] + A[M + i]

print(ans)
