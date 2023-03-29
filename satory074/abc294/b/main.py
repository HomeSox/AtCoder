import collections as cl
import math

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for a in A:
    l = []
    for a_ in a:
        if a_ == 0:
            l.append('.')
        else:
            l.append(chr(ord('A') + a_ - 1))

    print(''.join(l))
