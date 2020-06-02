#!/usr/bin/env python3

A = []
for i in range(4):
    A.append(list(map(int, input().split())))

for i in range(4): # yoko
    for j in range(3):
        if A[i][j] == A[i][j+1]:
            print('CONTINUE')
            exit()


for i in range(3):
    for j in range(4):
        if A[i][j] == A[i+1][j]:
            print('CONTINUE')
            exit()

print('GAMEOVER')
