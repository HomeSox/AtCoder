#!/usr/bin/env python3

N, M = map(int, input().split())

D = {} # 親；子
T = {}
for i in range(1, N+1):
    D[i] = []
    T[i] = 0

for i in range(1,M+1):
    A, B = map(int, input().split())
    D[A].append(B)
    D[B].append(A)

parent = [1]


while len(parent) > 0:
    child = []
    for p in parent:
        for c in D[p]:
            if T[c] != 0: continue
            T[c] = p
            child.append(c)
    parent = child

for i in range(2, N+1):
    if T[i] == 0:
        print('No')
        exit()

print('Yes')
for i in range(2, N+1):
    print(T[i])
    


