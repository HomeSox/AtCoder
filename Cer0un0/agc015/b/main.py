#!/usr/bin/env python3

S = input()
B = [i for i in range(1, len(S)+1)]

cnt = 0
for i in range(len(S)):
    if S[i] == 'U':
        cnt += len(S[i+1:])
        cnt += len(S[:i])*2
    else:
        cnt += len(S[i+1:])*2
        cnt += len(S[:i])
print(cnt)
