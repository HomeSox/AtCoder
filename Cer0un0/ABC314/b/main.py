#!/usr/bin/env python3

N = int(input())

A = []

for i in range(N):
    C = int(input())
    A.append(list(map(int, input().split())))

X = int(input())

d = {}
for i in range(1, 38):
    d.update({i: []})
    
for i in range(len(A)):
    if X in A[i]:
        d[len(A[i])].append(i+1)
        
for k, v in d.items():
    if len(v) == 0: continue
    else:
        print(len(v))
        print(*v)
        exit()
print(0)
print()