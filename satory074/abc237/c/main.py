import collections as cl

S = input()

rS = S[::-1]

n_a = 0
for s in rS:
    if s == "a":
        n_a += 1
    else:
        break


for i in range(n_a + 1):
    if S == rS:
        print("Yes")
        break
    else:
        S = "a" + S
        rS = rS + "a"
else:
    print("No")
