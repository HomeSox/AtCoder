import collections as cl
import math

S = input()
T = input()

is_icchi = [False for _ in range(len(T))]
n_fuicchi = 0


def hantei(s1, s2):
    if s1 == "?":
        return True

    if s2 == "?":
        return True

    if s1 == s2:
        return True

    return False


ans = True
S_ = list(S[-(len(T)) :])
for i in range(len(T) + 1):

    if i == 0:
        for j, (s, t) in enumerate(zip(S_, T)):
            is_icchi[j] = hantei(s, t)

            if is_icchi[j] == False:
                ans = False
                n_fuicchi += 1
    else:
        b = hantei(S_[i - 1], T[i - 1])

        if b == True and is_icchi[i - 1] == False:
            n_fuicchi -= 1

        if b == False and is_icchi[i - 1] == True:
            n_fuicchi += 1

    if n_fuicchi == 0:
        print("Yes")
    else:
        print("No")

    # print("".join(S_), is_icchi, ans)

    if i != len(T):
        S_[i] = S[i]
