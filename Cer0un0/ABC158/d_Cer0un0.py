#!/usr/bin/env python3
S = input()
Q = int(input())

count = True
ans = S

ireru_mae = ''
ireru_usiro = ''
for i in range(Q):
    T = input().split()
    if len(T)==1:
        count = not(count)
        continue

    if count:
        if T[1] == '1': ireru_mae = T[2] + ireru_mae
        else: ireru_usiro += T[2]
    else:
        if T[1] == '1': ireru_usiro += T[2]
        else: ireru_mae = T[2] + ireru_mae

ans = ireru_mae + ans + ireru_usiro
if count:
    print(ans)
else:
    print(ans[::-1])
