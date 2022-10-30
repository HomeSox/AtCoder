import collections as cl
import math

MOD = 998244353
A, B, C, D, E, F = map(int, input().split())

print(
    ((A % MOD) * (B % MOD) * (C % MOD) - (D % MOD) * (E % MOD) * (F % MOD) + MOD) % MOD
)
