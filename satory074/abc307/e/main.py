import collections as cl
import math

N, M = map(int, input().split())

MOD = 998244353


def power(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = res * x % MOD
        x = x * x % MOD
        y >>= 1
    return res


def inv(x):
    return power(x, MOD - 2)


def solve(N, M):
    fact = [1] * (M + 1)
    for i in range(1, M + 1):
        fact[i] = fact[i - 1] * i % MOD
    ans = 0
    for i in range(1, N + 1):
        temp = fact[M] * inv(fact[i]) % MOD
        temp = temp * inv(fact[M - i]) % MOD
        if (N - i) & 1:
            ans = (ans - temp + MOD) % MOD
        else:
            ans = (ans + temp) % MOD
    return (power(M, N) - ans + MOD) % MOD


print(solve(N, M))
