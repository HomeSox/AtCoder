#!/usr/bin/env python3

S = input().split('+')

ans = 0
for i in range(len(S)):
    if '*' in S[i] and '0' in S[i]:
        pass
    elif '*' in S[i]:
        ans += 1
    elif S[i] != '0':
        ans += 1

print(ans)
