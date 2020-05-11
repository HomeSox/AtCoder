#!/usr/bin/env python3

A, B, C, K = map(int, input().split())

if K <= A:
    print(K)
else:
    nokori = K - A
    if nokori <= B:
        print(A)
    else:
        nokori2 = K - A - B
        print(A-nokori2)

