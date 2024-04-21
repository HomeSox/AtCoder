import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

S = input()

if 1 <= int(S[3:]) < 350:
    if int(S[3:]) == 316:
        print('No')
    else:
        print('Yes')
else:
    print('No')

