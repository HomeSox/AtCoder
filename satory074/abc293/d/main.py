import collections as cl
import math

N, M = map(int, input().split())

ropes = [[["R", -1], ["B", -1]] for _ in range(N + 1)]

for _ in range(M):
    A, B, C, D = input().split()
    A = int(A)
    C = int(C)

    r1 = ropes[A]
    r2 = ropes[C]

    if r1[0][0] == 'B':
        r1[0], r1[1] = r1[1], r1[0]

    if r2[0][0] == 'B':
        r2[0], r2[1] = r2[1], r2[0]

    if B == 'R':
        r2[1] = ["R", A]
    else:
        r2[1] = ["B", A]

    if D == 'R':
        r1[0] = ["R", C]
    else:
        r1[0] = ["B", C]

    ropes[A] = r1
    ropes[C] = r2

    for r in ropes:
        print(r)
    print()
