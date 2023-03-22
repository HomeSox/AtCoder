import collections as cl
import math

S = input()

# if len(S) != 8:
# print("No")
# exit()

if not (ord("A") <= ord(S[0]) <= ord("Z")):
    print("No")
    exit()

if not (ord("A") <= ord(S[-1]) <= ord("Z")):
    print("No")
    exit()

for s in S[1:-1]:
    if not (ord("0") <= ord(s) <= ord("9")):
        print("No")
        exit()

if len(S) != 8:
    print("No")
    exit()

if 100000 <= int(S[1:-1]) <= 999999:
    if len(S[1:-1]) == 6:
        print("Yes")
    else:
        print("No")
else:
    print("No")
