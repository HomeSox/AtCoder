import collections as cl
import math

N, M = map(int, input().split())

n_useable_underbar = 16
S = []
for _ in range(N):
    S.append(input())
    n_useable_underbar -= len(S[-1])

if n_useable_underbar > 16:
    print(-1)
    exit()

T = []
for _ in range(M):
    T.append(input())
