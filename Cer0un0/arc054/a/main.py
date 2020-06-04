#!/usr/bin/env python3

L, X, Y, S, D = map(int, input().split())

tokei = 10 ** 9
hantokei = 10 ** 9

if S < D:
    tokei = (D - S) / (Y + X)
    if X < Y:
        hantokei = (S + L - D) / (Y - X)
else:
    tokei = (L - S + D) / (Y + X)
    if X < Y:
        hantokei = (S - D) / (Y - X)


print(min(tokei, hantokei))
