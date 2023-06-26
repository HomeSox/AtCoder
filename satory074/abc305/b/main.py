import collections as cl
import math

p, q = map(str, input().split())

l = [0, 3, 4, 8, 9, 14, 23]

# 'A' = 65
pn = ord(p) - 65
qn = ord(q) - 65

# print(pn, qn)
print(abs(l[pn] - l[qn]))