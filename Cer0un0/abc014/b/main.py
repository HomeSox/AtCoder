#!/usr/bin/env python3

N, X = map(int, input().split())
A = list(map(int, input().split()))
A.reverse()

b = bin(X)[2:]

if len(b) != N:
    b = '0'*(N-len(b)) + b

ans = 0
for i in range(len(b)):
    if b[i] == '1':
        ans += A[i]
print(ans)
