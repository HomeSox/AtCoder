import collections as cl
import math

N = int(input())
A = [list(input()) for _ in range(N)]

# print(A)

for i in range(N):
    for j in range(N):
        s = A[i][j]

        if s == "-":
            continue

        if s == "W":
            t = "L"
        elif s == "L":
            t = "W"
        else:
            t = "D"

        if A[j][i] == t:
            continue
        else:
            print("incorrect")
            exit()

print("correct")
