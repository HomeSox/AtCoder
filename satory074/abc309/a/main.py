import collections as cl
import math

A, B = map(int, input().split())

if A % 3 == 1:
    if A + 1 == B:
        print('Yes')
    else:
        print('No')
elif A % 3 == 2:
    if A + 1 == B:
        print('Yes')
    elif A - 1 == B:
        print('Yes')
    else:
        print('No')
else:
    if A - 1 == B:
        print('Yes')
    else:
        print('No')