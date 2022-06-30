import math
import collections as cl
from collections import deque

A, B, C = map(int, input().split())

sign_ac = -1 if A < 0 and C % 2 == 1 else 1
sign_bc = -1 if B < 0 and C % 2 == 1 else 1

if sign_ac == sign_bc:
    if abs(A) > abs(B):
        print('>')
    elif abs(A) < abs(B):
        print('<')
    else:
        print('=')
else:
    if sign_ac > sign_bc:
        print('>')
    else:
        print('<')
