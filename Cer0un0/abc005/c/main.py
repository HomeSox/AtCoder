#!/usr/bin/env python3
from collections import deque

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N < M:
    print('no')
    exit()

queA = deque(A)
queB = deque(B)
cnt = 0
while queB:
    hito = queB.popleft()
    while queA:
        takoyaki = queA.popleft()
        if takoyaki <= hito <= takoyaki + T:
            cnt += 1
            break

if cnt == M: print('yes')
else: print('no')
