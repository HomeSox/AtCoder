#!/usr/bin/env python3

a, b = map(int, input().split())

s_a = str(a)
s_b = str(b)
a1 = []
b1 = []
a1.append(int('9'+s_a[1:]))
a1.append(int(s_a[0]+'9'+s_a[-1]))
a1.append(int(s_a[:2]+'9'))
b1.append(int('1'+s_b[1:]))
b1.append(int(s_b[0]+'0'+s_b[2]))
b1.append(int(s_b[:2]+'0'))

ma = -10**9
for i in range(3):
    ma = max(a - b1[i], ma)

for i in range(3):
    ma = max(a1[i] - b, ma)

print(ma)
