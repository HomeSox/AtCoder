#!/usr/bin/env python3
import bisect
N = int(input())
L = sorted(list(map(int, input().split())))
ans = 0
for i in range(len(L)):
    for j in range(i+1, len(L)):
        b_i = bisect.bisect_left(L, L[i]+L[j]) # a+bより小さい数
        ans += b_i - (j+1)
print(ans)
