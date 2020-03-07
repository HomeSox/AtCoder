#!/usr/bin/env python3
N, A, B = map(int, input().split())

if A==0 and B==0:
    print(0)
    exit()

s = A + B

a = N // s

ans = A*a
nokori = N-s*a

if nokori <= A:ans += nokori
else: ans += A

print(ans)
