#!/usr/bin/env python3

N = int(input())
S = input()
d = {'A':0, 'B':0, 'C':0}

cnt = 0
for s in S:
    d[s] += 1
    cnt += 1
    if d['A'] > 0 and d['B'] > 0 and d['C'] > 0:
        print(cnt)
        exit()