#!/usr/bin/env python3

H, W = map(int, input().split())
S = [list('.'*(W+2))]

for i in range(H):
    S.append(list('.' + input() + '.'))

S.append(list('.'*(W+2)))

A = []


for i in range(1, H+1):
    AA = []
    for j in range(1, W+1):
        cnt = 0
        if S[i][j] == '#':
            AA.append('#')
            continue
        if S[i-1][j-1] == '#': cnt += 1
        if S[i-1][j] == '#': cnt += 1
        if S[i-1][j+1] == '#': cnt += 1
        if S[i][j-1] == '#': cnt += 1
        if S[i][j+1] == '#': cnt += 1
        if S[i+1][j-1] == '#': cnt += 1
        if S[i+1][j] == '#': cnt += 1
        if S[i+1][j+1] == '#': cnt += 1
        AA.append(cnt)
    A.append(AA)

for a in A:
    print(''.join(map(str, a)))
