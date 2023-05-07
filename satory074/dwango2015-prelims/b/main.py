import collections as cl
import math

S = input()

while S.count('25') > 0:
    S = S.replace('25', 'A')

s = len(S)
C = []

now = 0
for i in range(s):
    if S[i] == 'A':
        now += 1
    else:
        C.append(now)
        now = 0
C.append(now)

ans = 0
for c in C:
    ans += c*(c+1)//2
print(ans)