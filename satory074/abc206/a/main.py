import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())

TEIKA = 206
hanbai = int(N * 1.08)

if TEIKA == hanbai:
    print('so-so')
    exit()

if TEIKA < hanbai:
    print(':(')
else:
    print('Yay!')
