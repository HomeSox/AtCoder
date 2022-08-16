import math
import collections as cl
from collections import deque

S = input()

d = {}
for s in S:
    if s not in d:
        d[s] = 1

l = [chr(i) for i in range(97, 97 + 26)]

for l_ in l:
    if l_ not in d:
        print(f"{S}{l_}")
        exit()

l = []
for i in range(len(S) - 1, -1, -1):
    if S[i] not in l:
        l.append(S[i])
        l.sort()

    for s in l:
        ans_ = f"{S[:(i-1)]}{(s)}"
        # print(ans_, l)
        if ans_ > S:
            if S[0] == l[-1]:
                print(-1)
            else:
                print(ans_)

            exit()
