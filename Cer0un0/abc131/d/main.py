#!/usr/bin/env python3

N = int(input())

AB = {} # 締め切り: かかる時間


for i in range(N):
    a, b = map(int, input().split())
    if b in AB: AB[b].append(a)
    else: AB[b] = [a]


time = 0
for s, t in sorted(AB.items(), key=lambda x:x[0]):
    for ti in t:
        time += ti
        if time > s:
            print('No')
            exit()
print('Yes')

