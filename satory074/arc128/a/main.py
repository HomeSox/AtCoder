import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(N)]

for i in range(N - 1):
    if A[i] > A[i + 1]:
        ans[i] ^= 1
        ans[i + 1] ^= 1

print(*ans)
