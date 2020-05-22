#!/usr/bin/env python3

N = int(input())

n = 0

for i in range(N):
    if i**2 > N:
        n = i
        break

sa = 10**9
tairu = 10**9
for i in range(1,N+1):
    for j in range(1,N+1):
        if i*j <= N:
            s = abs(i-j)
            t = N - i*j
            if t >= 0 and sa+tairu > s+t:
                sa = s
                tairu = t
                #break
        else:
            break

print(sa+tairu)
