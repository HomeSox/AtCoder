#!/usr/bin/env python3

N, M, X = map(int, input().split())

li = [f'{i:012b}' for i in range(2**N)]
C = []
A = []
for i in range(N):
    B = list(map(int, input().split()))
    C.append(B[0])
    A.append(B[1:])

d = []
for l in li:
    b = l[::-1][:N]
    rikai = [0]*M
    pri = [0]*N
    for i in range(len(b)):
        if b[i] == '1':
            for j in range(M):
                rikai[j] += A[i][j]
            pri[i] += C[i]
    d.append((sum(pri), rikai))

ans = 10**100
for s in d:
    f = True
    for r in s[1]:
        if r < X:
            f = False
            break
    if f:
        ans = min(ans, int(s[0]))
if ans == 10**100:print(-1)
else: print(ans)
