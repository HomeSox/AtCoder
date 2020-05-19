#!/usr/bin/env python3

S = list(input())
S.reverse()

for i in range(1, len(S)):
    s = S[i:]
    if len(s) % 2 == 1: continue
    x = len(s) // 2
    if s[:x] == s[x:]:
        print(len(s))
        exit()
