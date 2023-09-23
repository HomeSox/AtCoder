import collections as cl
import math

N = int(input())
S = str(N)

if len(S) == 1:
    print('Yes')
    exit()

for s1, s2 in zip(S[:-1], S[1:]):
    if s1 > s2:
        continue

    print('No')
    exit()

print('Yes')
