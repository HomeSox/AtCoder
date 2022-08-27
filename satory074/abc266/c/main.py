import collections as cl
import math

import numpy as np
from numpy import linalg as LA

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
ABCD = [A, B, C, D]

for i in range(4):
    a = np.array(ABCD[i - 1])
    b = np.array(ABCD[i])
    c = np.array(ABCD[(i + 1) % 4])

    vec_a = a - b
    vec_c = c - b

    x = np.cross(vec_a, vec_c)

    if x >= 0:
        print("No")
        break
else:
    print("Yes")
