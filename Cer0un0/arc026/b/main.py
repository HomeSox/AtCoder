#!/usr/bin/env python3


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N = int(input())
yakusu = make_divisors(N)
s = sum(yakusu) - N
if s == N: print('Perfect')
elif s < N: print('Deficient')
else: print('Abundant')
