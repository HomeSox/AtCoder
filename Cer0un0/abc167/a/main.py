#!/usr/bin/env python3

S = input()
T = input()
if S == T[:len(T)-1] and len(S)+1==len(T):
    print('Yes')
else:
    print('No')
