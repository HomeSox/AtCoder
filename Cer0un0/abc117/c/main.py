#!/usr/bin/env python3

N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

D = {}

for i in range(M-1):
    D[(X[i],X[i+1])] = X[i+1] - X[i]

s_D = sorted(D.items(), key=lambda x:x[1])[::-1]
A = s_D[N-1:]
ans = 0
for a in A:
    ans += a[1]
print(ans)
