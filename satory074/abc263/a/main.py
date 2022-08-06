import collections as cl
import math

A, B, C, D, E = map(int, input().split())
l = [A, B, C, D, E]

clc = cl.Counter(l)

if len(clc) == 2:
    if clc.most_common()[0][1] == 2 or clc.most_common()[1][1] == 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
