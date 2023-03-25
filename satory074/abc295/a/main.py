import collections as cl
import math

N = int(input())
W = list(input().split())

l = ['and', 'not', 'that', 'the', 'you']

for w in W:
    if w in l:
        print('Yes')
        break
else:
    print('No')