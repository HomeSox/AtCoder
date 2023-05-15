import collections as cl
import math

A, B = map(int, input().split())

# 公約数を求める
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 素因数分解
def prime_factorization(n):
    arr = []
    while n % 2 == 0:
        arr.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            arr.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        arr.append(n)
    return arr

primes = set(prime_factorization(gcd(A, B)))
print(len(primes) + 1)
