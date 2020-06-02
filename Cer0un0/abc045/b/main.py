#!/usr/bin/env python3

from collections import deque
SA = input()
SB = input()
SC = input()

que = {'a': deque(SA), 'b':deque(SB), 'c': deque(SC)}

index = 'a'

while True:
    if len(que[index]) == 0:
        print(index.upper())
        exit()
    index = que[index].popleft()

