import collections as cl
import math

N = int(input())
A = [int(input()) for _ in range(N)]

clc = list(cl.Counter(A))
clc.sort()
print(clc[-2])
