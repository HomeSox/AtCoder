import collections as cl
import math

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

diff_L = [L - a for a in A]
diff_R = [R - a for a in A]
r_diff_R = diff_R[::-1]
print(diff_L, diff_R)

qL = [diff_L[0]] * (N + 1)
qR = [r_diff_R[0]] * (N + 1)
for i in range(1, N):
    qL[i + 1] = qL[i] + diff_L[i]
    qR[i + 1] = qR[i] + r_diff_R[i]


qL = qL[1:]
qR = qR[1:]
r_qR = qR[::-1]

print(qL, r_qR)

minsum_L = [qL[0]] * (N + 1)
minsum_R = [qR[0]] * (N + 1)
for i in range(1, N):
    minsum_L[i + 1] = min(minsum_L[i], qL[i])
    minsum_R[i + 1] = min(minsum_R[i], qR[i])

minsum_L = minsum_L[1:]
minsum_R = minsum_R[1:]

print(minsum_L)
print(minsum_R)
