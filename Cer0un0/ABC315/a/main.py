#!/usr/bin/env python3

S = input()

r = ['a','i','u','e','o']
res = ''
for s in S:
    if s in r: continue
    res += s
    
print(res)