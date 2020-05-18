#!/usr/bin/env python3
import collections
N = int(input())
A = list(map(int, input().split()))

T = collections.Counter(A)
hen1 = 0 # 小さい
hen2 = 0 # 大きい
for h, c in sorted(T.items(), key=lambda x:x[0]):
    if c >= 4:
        hen1 = h
        hen2 = h
    elif c >= 2:
        if hen1 >= hen2:
            hen2 = h
        else:
            hen1 = h
print(hen1*hen2)


