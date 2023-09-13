#!/usr/bin/env python3

M = int(input())
D = list(map(int, input().split()))
sum_d = sum(D)
mid = sum_d // 2 + 1
v = 0
mid_i = 0
ans = []
for i in range(M):
    v += D[i]
    if v >= mid:
        mid_i = i + 1
        break

print(*[mid_i, mid-(v-D[mid_i-1])])