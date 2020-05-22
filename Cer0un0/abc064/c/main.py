#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

D = {400:0, 800:0, 1200:0, 1600:0, 2000:0, 2400:0, 2800:0, 3200:0}

cnt = 0
for a in A:
    if a < 400:
        D[400]+=1
    elif a < 800:
        D[800]+=1
    elif a < 1200:
        D[1200]+=1
    elif a < 1600:
        D[1600]+=1
    elif a < 2000:
        D[2000]+=1
    elif a < 2400:
        D[2400]+=1
    elif a < 2800:
        D[2800]+=1
    elif a < 3200:
        D[3200]+=1
    elif a >= 3200:
        cnt += 1

mi = 0
ma = 0

for k, v in D.items():
    if v !=0:
        mi += 1

ma = mi + cnt
if mi == 0: mi = 1

print(str(mi) + ' ' + str(ma))
