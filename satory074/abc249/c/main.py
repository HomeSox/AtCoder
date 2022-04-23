import collections as cl
import math

N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for n in range(2**N):
    s = ""
    for i in range(N):
        if (n >> i) & 1:
            s += S[i]

    clc = cl.Counter(s)
    ans_ = 0
    for k, v in clc.items():
        if v == K:
            ans_ += 1

    ans = max(ans, ans_)

print(ans)
