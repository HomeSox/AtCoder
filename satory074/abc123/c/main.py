import math
import collections as cl

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
l = [A, B, C, D, E]

print(5 + (math.ceil(N / min(l))) - 1)
