import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

S = input()

if ord('A') <= ord(S[0]) <= ord('Z'):
    for s in S[1:]:
        if ord('a') <= ord(s) <= ord('z'):
            continue
        else:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')
