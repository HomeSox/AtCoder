#!/usr/bin/env python3

x = int(input())

if x % 11 == 0:
    tmp = 0
elif x % 11 < 7:
    tmp = 1
else:
    tmp = 2
print(x//11 * 2 + tmp)
