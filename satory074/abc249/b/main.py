import collections as cl
import math

S = input()
clc = cl.Counter(S)

# print(S.lower(), S.upper(), clc.most_common())
if clc.most_common()[0][1] != 1:
    print("No")
    exit()

if S == S.upper():
    print("No")
    exit()

if S == S.lower():
    print("No")
    exit()

print("Yes")
