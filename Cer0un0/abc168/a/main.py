#!/usr/bin/env python3

N = input()
S = N[-1]
if S == '0' or S=='1' or S=='6' or S=='8':
    print('pon')
elif S=='3':
    print('bon')
else:
    print('hon')
