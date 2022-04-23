import collections as cl
import math

A, B, C, D, E, F, X = map(int, input().split())

tak = 0
aok = 0
tak_is_jog = True
aok_is_jog = True
tak_time = 0
aok_time = 0
for _ in range(X):
    tak_time += 1
    if tak_is_jog:
        tak += 1

        if tak_time == A:
            tak_is_jog = False
            tak_time = 0
    else:
        if tak_time == C:
            tak_is_jog = True
            tak_time = 0

    aok_time += 1
    if aok_is_jog:
        aok += 1

        if aok_time == D:
            aok_is_jog = False
            aok_time = 0
    else:
        if aok_time == F:
            aok_is_jog = True
            aok_time = 0

tak = tak * B
aok = aok * E

if tak == aok:
    print("Draw")
elif tak > aok:
    print("Takahashi")
else:
    print("Aoki")
