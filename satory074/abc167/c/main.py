#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, m, x  = map(int, input().split())
li  = [list(map(int, input().split())) for _ in range(n)]
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = 10**9
for i in range(2**n): # 総当り
    s = f'{i:012b}'[12-n:]

    # TODO:金額break

    rikaido = [0] * m
    price = 0
    for i2, b in enumerate(s): # 選んだやつ
        if b == '1':
            price += li[i2][0]
            for i3 in range(m): # 理解度を足す
                rikaido[i3] += li[i2][i3+1]

    # 理解してるか
    for r_ in rikaido:
        if r_ < x:
            break
    else:
        if price < ans:
            ans = price

print(-1 if ans == 10**9 else ans)
