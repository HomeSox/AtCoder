def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes


N = int(input())
primes = sieve_of_eratosthenes(3 * (10 ** 5))

ans = 0
for i in range(len(primes)):
    a = primes[i]

    for j in range(i + 1, len(primes)):
        b = primes[j]

        if (a ** 2) * (b ** 3) > N:
            break

        if (a ** 3) * (b ** 2) > N:
            break

        for k in range(j + 1, len(primes)):
            c = primes[k]

            if (a ** 2) * b * (c ** 2) > N:
                break
            else:
                ans += 1

print(ans)
