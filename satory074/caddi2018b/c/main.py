def prime_factors(n):
    factors = {}

    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 2

    if n > 2:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1

    return factors


N, P = map(int, input().split())
factors = prime_factors(P)

gcd = 1
for p, k in factors.items():
    gcd *= p ** (k // N)

ans = gcd


print(ans)
