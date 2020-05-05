#!/usr/bin/env python3

N, D, K = map(int, input().split())

LR = []
UNBOBO = {}
for i in range(D):
    l, r = map(int, input().split())
    LR.append([l, r])

for i in range(K):
    s, t = map(int, input().split())
    UNBOBO[i] = [s, t]

UHHOHHO = {}
for i in range(D):
    for u, t in UNBOBO.items():
        if u in UHHOHHO: continue
        f = LR[i][0] <= t[0] <= LR[i][1]
        if LR[i][0] <= t[1] <= LR[i][1] and f:
            UHHOHHO[u] = i+1
            UNBOBO[u][0] = t[1]
        elif f:
            if t[0] < t[1]:
                UNBOBO[u][0] = LR[i][1]
            else:
                UNBOBO[u][0] = LR[i][0]



for k, day in sorted(UHHOHHO.items(), key=lambda x:x[0]) :
    print(day)
