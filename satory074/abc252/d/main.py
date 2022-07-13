import collections as cl
import math
from functools import lru_cache

N = int(input())
A = list(map(int, input().split()))

A.sort()
clc = cl.Counter(A)

keys = list(clc.keys())
values = list(clc.values())
# print(Q)
# print(keys)
# print(clc.values())


@lru_cache
def f():
    ans = 0
    sum_ = sum(values)
    for i in range(len(keys)):
        sum_ -= values[i]

        sum__ = sum(values[i + 1 :])
        for j in range(i + 1, len(keys) - 1):
            sum__ -= values[j]
            ans += sum__ * clc[keys[i]] * clc[keys[j]]
            # print(keys[i], keys[j], sum(values[j + 1 :]), ans)

    print(ans)


f()
