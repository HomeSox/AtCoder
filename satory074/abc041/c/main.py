import math
import collections as cl
from collections import deque

N = int(input())
a = list(map(int, input().split()))

ia = [(a, i + 1) for i, a in enumerate(a)]
ria = sorted(ia, reverse=True)

[print(i) for a, i in ria]

