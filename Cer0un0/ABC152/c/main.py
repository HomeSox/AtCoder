#!/usr/bin/env python3

N = int(input())
P = list(map(int, input().split()))
M = [0] * N
M[0] = P[0]
m = P[0]
for i in range(1, N):
    m = min(P[i], m)
    M[i] = m


ans = 0
for i in range(N):
    if P[i] <= M[i]:ans+=1

print(ans)
