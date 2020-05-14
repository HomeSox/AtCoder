#!/usr/bin/env python3
N, Q = map(int, input().split())
S = input()
LR = []
for i in range(Q):
    l, r = map(int, input().split())
    LR.append([l,r])

A = [0]

cnt = 0
for i in range(1, len(S)):
    if S[i-1:i+1] == 'AC':
        cnt += 1
    A.append(cnt)

for l, r in LR:
    print(A[r-1] - A[l-1])
