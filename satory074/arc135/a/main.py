from functools import lru_cache
MOD = 998244353

@lru_cache
def f(x):
    if x <= 4:
        return x
    else:
        return (f(x // 2) * f((x + 1) // 2)) % MOD

X = int(input())
print(f(X))