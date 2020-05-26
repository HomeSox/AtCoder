#!/usr/bin/env python3

S = input().split()
N = int(input())
T = [input() for _ in range(N)]

ANS = []

for s in S:
    f = True
    for t in T:
        if '*' in t:
            if len(t) != len(s): continue
            A = [False] * len(t)
            for i in range(len(t)):
                if t[i] == '*' or t[i] == s[i]:
                    A[i] = True
            
            if set(A) == 1 and set(A).pop() == True:
                ANS.append('*'*len(s))
            break
        else:
            if s == t:
                ANS.append('*'*len(s))
                f = False
                break
    if f: ANS.append(s)



ans = ANS[0]
for a in ANS[1:]:
    ans += ' ' + a
print(ans)
