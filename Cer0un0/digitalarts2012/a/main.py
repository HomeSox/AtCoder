#!/usr/bin/env python3

S = input().split()
N = int(input())
T = [input() for _ in range(N)]

ANS = []

for s in S:
    f = True
    for t in T:
        if len(t) != len(s): continue
        A = [False] * len(s)
        for i in range(len(s)):
            if t[i] == '*' or t[i] == s[i]:
                A[i] = True
            
        if len(set(A)) == 1 and set(A).pop() == True:
            ANS.append('*'*len(s))
            f = False
            break

    if f: ANS.append(s)



ans = ANS[0]
if len(ANS) > 1:
    for a in ANS[1:]:
        ans += ' ' + a
print(ans)
