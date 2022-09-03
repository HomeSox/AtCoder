import collections as cl
import math

S = input()

if S[0] == "1":
    print("No")
    exit()

li = []

li.append((S[6] == "1"))
li.append((S[3] == "1"))
li.append((S[1] == "1") or (S[7] == "1"))
li.append((S[0] == "1") or (S[4] == "1"))
li.append((S[8] == "1") or (S[2] == "1"))
li.append((S[5] == "1"))
li.append((S[9] == "1"))
# print(li)

for i, l in enumerate(li[:-2]):
    if li[i] == True and li[i + 1] == False:
        for j in range(i + 2, len(li)):
            if li[j] == True:
                print("Yes")
                exit()
else:
    print("No")
