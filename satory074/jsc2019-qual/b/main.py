import collections as cl
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7

ans = 0
for i in range(N):
    n = 0
    m = 0
    for j in range(i):
        if A[i] > A[j]:
            n += 1

    for j in range(i+1, N):
        if A[i] > A[j]:
            n += 1
            m += 1

    ans += ((m * K) + n * K * (K-1) // 2) % MOD

print(ans % MOD)