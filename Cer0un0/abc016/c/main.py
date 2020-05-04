#!/usr/bin/env python3

N, M = map(int, input().split())

d = {}
for i in range(1, N+1):
    d[i] = [i]

for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)


ans = {}
for i in range(1, N+1):
    tomodati = d[i]
    cnt = []
    for t in tomodati:
        tomodati2 = d[t]
        for t2 in tomodati2:
            if t2 not in tomodati and t2 not in cnt:
                cnt.append(t2)

    ans[i] = len(cnt)

for z, c in ans.items():
    print(c)
