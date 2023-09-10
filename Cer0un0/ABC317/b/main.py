#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

for a in range(min(A), max(A)+1):
    if a not in A:
        print(a)
        exit()