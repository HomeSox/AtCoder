#!/usr/bin/env python3

N, M = map(int, input().split())
A = list(map(int, input().split()))

G = [-1 for _ in range(N)]
ans = [-1 for _ in range(N)]
for a in A:
    G[a-1] = 0
    
cnt = 0
index = N-1
for g in G[::-1]:
    if g != 0:
        cnt += 1
        ans[index] = cnt
    else:
        ans[index] = 0
        cnt = 0
    index -= 1
    
for a in ans:
    print(a)