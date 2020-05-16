#!/usr/bin/env python3

S = input()
K = int(input())

A = []
cnt = 1
C = []
for i in range(1,len(S)):
    print(i)
    if S[i-1] == S[i]:
        cnt += 1
    else:
        C.append([S[i-1], cnt])
        cnt = 1
C.append([S[i], cnt])

ans = 0
S2 = []
for c in C:
    ans += c[1]-1
    if c[1] == 1:
        S2.append(False)
    else:
        for _ in range(c[1]):
            S2.append(True)

print(ans)
print(C)
print(S2)

if S[0] == S[-1]:
    if S2[-1] == False:
        ans += 1
