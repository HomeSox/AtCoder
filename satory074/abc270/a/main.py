import collections as cl
import math

A, B = map(int, input().split())

ansA = []
ansB = []

if A >= 4:
    ansA.append(True)
    A -= 4
else:
    ansA.append(False)

if A >= 2:
    ansA.append(True)
    A -= 2
else:
    ansA.append(False)

if A >= 1:
    ansA.append(True)
    A -= 1
else:
    ansA.append(False)

if B >= 4:
    ansB.append(True)
    B -= 4
else:
    ansB.append(False)

if B >= 2:
    ansB.append(True)
    B -= 2
else:
    ansB.append(False)

if B >= 1:
    ansB.append(True)
    B -= 1
else:
    ansB.append(False)

# print(ansA)
# print(ansB)

ans = 0
if ansA[0] or ansB[0]:
    ans += 4

if ansA[1] or ansB[1]:
    ans += 2

if ansA[2] or ansB[2]:
    ans += 1

print(ans)
