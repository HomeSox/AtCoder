import collections as cl
import math

N = int(input())
S = input()

is_A = False
is_B = False
is_C = False
for i, s in enumerate(S):
    if s == "A":
        is_A = True
    elif s == "B":
        is_B = True
    elif s == "C":
        is_C = True
    else:
        None

    if is_A and is_B and is_C:
        print(i + 1)
        break
