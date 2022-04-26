import math
import collections as cl
from collections import deque
import re

S = list(input().split())

PATTERN = r'@[a-z]*'

ans = []
for s in S:
    mat = re.findall(PATTERN, s)

    if mat:
        for m in mat:
            s = m[1:]

            if s:
                ans.append(s)

ans = sorted(list(set(ans)))
for a in ans:
    print(a)
