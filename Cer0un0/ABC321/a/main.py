#!/usr/bin/env python3

N = int(input())
s = str(N)
for i in range(0, len(s)-1):
    if int(s[i]) <= int(s[i+1]):
        print('No')
        exit()
print('Yes')