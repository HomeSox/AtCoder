import collections as cl
import math

S = list(map(int, input().split()))

for s1, s2 in zip(S[:-1], S[1:]):
    if s1 > s2:
        print('No')
        break

    if not 100 <= s1 <= 675:
        print('No')
        break

    if s1 % 25 != 0:
        print('No')
        break
else:
    if not 100 <= S[-1] <= 675:
        print('No')
    elif S[-1] % 25 != 0:
        print('No')
    else:
        print('Yes')
