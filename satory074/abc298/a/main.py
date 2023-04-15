import collections as cl
import math

N = int(input())
S = input()

c = 0
for s in S:
    if s == 'x':
        print('No')
        exit()

    if s == 'o':
        c += 1

if c >= 1:
    print('Yes')
else:
    print('No')