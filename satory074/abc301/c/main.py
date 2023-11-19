import collections as cl
import math

S = input()
T = input()

scnt = cl.Counter(S)
tcnt = cl.Counter(T)

for c in 'atcoder':
    ma = max(scnt[c], tcnt[c])

    if scnt['@'] < ma - scnt[c]:
        print('No')
        exit()

    if tcnt['@'] < ma - tcnt[c]:
        print('No')
        exit()

    scnt['@'] -= ma - scnt[c]
    scnt[c] = ma
    tcnt['@'] -= ma - tcnt[c]
    tcnt[c] = ma

if scnt == tcnt:
    print('Yes')
else:
    print('No')
