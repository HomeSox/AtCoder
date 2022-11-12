import collections as cl
import math

N = int(input())
slist = []
for _ in range(N):
    S = input()
    slist.append(S)

    if S[0] not in ["H", "D", "C", "S"]:
        print("No")
        exit()

    if S[1] not in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
        print("No")
        exit()

if len(slist) == len(set(slist)):
    print("Yes")
else:
    print("No")
