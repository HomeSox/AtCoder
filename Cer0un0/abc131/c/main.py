#!/usr/bin/env python3

import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

A, B, C, D = map(int, input().split())

N = B - A + 1

g = lcm(C,D)
C_ = B//C - (A-1)//C
D_ = B//D - (A-1)//D
CD_ = B//g - (A-1)//g
ans = N - C_ - D_ + CD_
print(ans)
