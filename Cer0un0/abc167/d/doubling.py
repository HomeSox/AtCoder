#!/usr/bin/env python3

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [a-1 for a in A]

b = bin(K)
D = {0:list(range(N))} # ダブリングマトリクス
D[1] = [A[D[0][i]] for i in range(N)]

for i in range(1, len(b)-2):
    D[2**i] = [D[2**(i-1)][D[2**(i-1)][j]] for j in range(N)]


n = 2**(len(b[2:])-1)
S = D[n][0] # 初期状態
keta = len(b[2:]) - 2
for j in range(len(b[3:])):
    k = 2**keta
    if b[j+3] == '1':
        S = D[k][S]
    keta -= 1

print(S+1)
