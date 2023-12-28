import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


S = list(input())
T = list(input())

S.sort()
T.sort()

S = ''.join(S)
T = ''.join(T)

l = ['AB', 'BC', 'CD', 'AE']

if S in l and T in l:
    print('Yes')
    exit()

if S not in l and T not in l:
    print('Yes')
    exit()

print('No')
