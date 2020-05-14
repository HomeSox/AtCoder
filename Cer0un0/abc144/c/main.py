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

D = make_divisors(N)

ans = 10**12+1
for d in D:
    b = N//d
    if d + b < ans:
        ans = d + b
print(ans-2)
