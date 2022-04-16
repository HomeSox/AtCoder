import collections as cl
import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N, M, K = map(int, input().split())


if N > K:
    print(0)
    exit()


ans = 1
MOD = 998244353
for i in range(N + 1, K + 1):
    ans += combinations_count(N, i) % MOD

print(ans)
