import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
w = list(input().split())

dict = {'b': 1, 'c': 1, 'd': 2, 'w': 2, 't': 3, 'j': 3, 'f': 4, 'q': 4, 'l': 5, 'v': 5, 's': 6, 'x': 6, 'p': 7, 'm': 7, 'h': 8, 'k': 8, 'n': 9, 'g': 9, 'z': 0, 'r': 0}

ans = []
for w_ in w:
    s = ''
    for w__ in w_:
        if w__.lower() in dict:
            s += str(dict[w__.lower()])

    if s != '':
        ans.append(s)

print(*ans)
