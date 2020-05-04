#!/usr/bin/env python3

N = int(input())
MOD = 10**4+7

A = [0, 0, 1]

for i in range(3, 10**6+1):
    v = A[i-3]+A[i-2]+A[i-1]
    A.append(v%MOD)

print(A[N-1])

