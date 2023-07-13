import collections as cl
import math

NA, NB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

aab = set(A) & set(B)
aob = set(A) | set(B)

print(len(aab) / len(aob))