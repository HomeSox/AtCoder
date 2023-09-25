#!/usr/bin/env python3

N, D = map(int, input().split())

S = []
for i in range(N):
    S.append(list(input()))
    
S_t = [list(x) for x in zip(*S)]

cnt = 0
o = []
for s in S_t:
    set_s = set(s)
    if len(set_s) == 1 and list(set_s)[0] == 'o':
        o.append('o')
    else:
        o.append('x')

cnt = 0
tmp = 0
for v in o:
    if v == 'o':
        tmp += 1
    else:
        if cnt < tmp: cnt = tmp
        tmp = 0

if cnt < tmp: cnt = tmp

print(cnt)