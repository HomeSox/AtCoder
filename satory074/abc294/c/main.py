import collections as cl
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

aidx = 0
bidx = 0
la = []
lb = []

while aidx < N and bidx < M:
    if A[aidx] < B[bidx]:
        la.append(aidx + bidx + 1)
        aidx += 1
    else:
        lb.append(bidx + aidx + 1)
        bidx += 1

while aidx < N:
    la.append(aidx + bidx + 1)
    aidx += 1

while bidx < M:
    lb.append(bidx + aidx + 1)
    bidx += 1

print(*la)
print(*lb)