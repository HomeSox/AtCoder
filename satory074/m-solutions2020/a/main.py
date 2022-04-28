import math
import collections as cl
from collections import deque

X = int(input())

ans = 10 - X // 200

if ans >= 9:
    print(8)
else:
    print(ans)
