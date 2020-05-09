#!/usr/bin/env python3
S = input()

T = []
s = S[0]
for i in range(1, len(S)):
    if s[len(s)-1] == S[i]: s += S[i]
    else:
        T.append(s)
        s = S[i]
T.append(s)

ans = ''
for t in T:
    ans += t[0]+str(len(t))
print(ans)
