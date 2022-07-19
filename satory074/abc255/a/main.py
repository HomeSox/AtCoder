import collections as cl
import math

R, C = map(int, input().split())
A1 = list(input().split())
A2 = list(input().split())
A = [A1, A2]

print(A[R - 1][C - 1])
