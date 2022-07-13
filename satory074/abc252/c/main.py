import collections as cl
import math

N = int(input())
S = [input() for _ in range(N)]

ans = 10**9
for n in range(10):
    t = 0
    l = [s.index(str(n)) for s in S]

    clc = cl.Counter(l)

    # for k, v in clc.items():
    # print(k, v)

    cnt = N
    ans_ = 0
    while cnt:
        for i in range(10):
            if clc[i]:
                ans_ = (N - cnt) * 10 + i
                clc[i] -= 1

        cnt -= 1

    if ans_ < ans:
        ans = ans_

print(ans)
