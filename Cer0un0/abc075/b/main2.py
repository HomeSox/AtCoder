#!/usr/bin/env python3

H, W = map(int, input().split())
S = [list('.'*(W+2))]

for i in range(H):
    S.append(list('.' + input() + '.'))

S.append(list('.'*(W+2)))

A = []
print(S)
for i in range(1, W):
    AA = []
    for j in range(1, H):
        cnt = 0
        print(i, j, S[i])
        if S[i-1][j-1] == '#': cnt += 1
        if S[i-1][j] == '#': cnt += 1
        if S[i-1][j+1] == '#': cnt += 1
        if S[i][j-1] == '#': cnt += 1
        if S[i][j] == '#': cnt += 1
        if S[i][j+1] == '#': cnt += 1
        if S[i+1][j-1] == '#': cnt += 1
        if S[i+1][j] == '#': cnt += 1
        if S[i+1][j+1] == '#': cnt += 1
        AA.append(cnt)
    A.append(AA)

print(A)
