#!/usr/bin/env python3

N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

tele = [0]
s = 0
B = {0:0}
for i in range(N):
    if A[tele[-1]] in B and len(B) != 1:
        s = B[A[tele[-1]]]
        break
    B[A[tele[-1]]] = i+1
    tele.append(A[tele[-1]])

if K <= s:
    print(tele[K]+1)
else:
    K -= s
    amari = K%(len(tele[s:len(tele)]))
    tele = tele[s:len(tele)]*2
    print(tele[amari]+1)
