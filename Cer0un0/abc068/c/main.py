#!/usr/bin/env python3

N, M = map(int, input().split())
B = {}
for i in range(1, N+1):
    B[i] = []

for i in range(M):
    a, b = map(int, input().split())
    if b == N or a == 1:
        B[a].append(b)
for sima in B[1]:
    if N in B[sima]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
