#!/usr/bin/env python3
N, M = map(int, input().split())
S = input()
T = input()

settou = False
setuo = False
if T[:N] == S: settou = True
if T[-N:] == S: setuo = True

if settou and setuo:
    print(0)
elif settou:
    print(1)
elif setuo:
    print(2)
else:
    print(3)
