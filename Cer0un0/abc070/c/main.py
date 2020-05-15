#!/usr/bin/env python3

import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

N = int(input())
T = [int(input()) for _ in range(N)]

g = T[0]
for i in range(1,N):
    g = lcm(g, T[i])
print(g)
