#!/usr/bin/env python3
import collections
import itertools as it
import math

# import numpy as np

#  = input()
#  = int(input())
H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]

hashi = []
for a in A:
    lidx = None
    ridx = None
    for i, s in enumerate(a):
        if (lidx is not None) and (ridx is not None):
            if s == "#":
                exit(print("Impossible"))

        if lidx is None:
            if s == "#":
                lidx = i
                continue

        if (lidx is not None) and (ridx is None):
            if s == ".":
                ridx = i - 1
                continue
    else:
        if (lidx is not None) and (ridx is None):
            if a[-1] == "#":
                ridx = W - 1

        hashi.append((lidx, ridx))

# print(hashi)

for (l1, r1), (l2, r2) in zip(hashi[:-1], hashi[1:]):
    if r1 != l2:
        exit(print("Impossible"))
else:
    exit(print("Possible"))

