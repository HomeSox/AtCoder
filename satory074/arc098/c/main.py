import collections as cl
from collections import deque

N = int(input())
S = input()

clc = cl.Counter(S)

lwest = 0
least = 0
rwest = clc["W"]
reast = clc["E"]

ans = 10**9
for s in S:
    if s == "W":
        ans_ = clc["W"] - 1

    ans_ = lwest + reast - (1 if s == "E" else 0)
    if ans_ < ans:
        ans = ans_

    if s == "W":
        lwest += 1
        rwest -= 1
    else:
        least += 1
        reast -= 1

    # print(lwest, least, rwest, reast)

print(ans)
