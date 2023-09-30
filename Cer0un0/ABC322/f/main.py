#!/usr/bin/env python3

N, Q = map(int, input().split())
S = list(input())

for i in range(Q):
    c, l, r = map(int, input().split())
    if c == 1:
        for j in range(l-1, r):
            if S[j] == '0': S[j] = '1'
            else: S[j] = '0'
    else:
        cnt = 0
        ans = 0
        for j in range(l-1, r):
            if S[j] == '1':
                cnt += 1
            else:
                if ans < cnt : ans = cnt
                cnt = 0
        if ans < cnt : ans = cnt    
        print(ans)