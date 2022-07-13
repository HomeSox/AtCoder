import collections as cl
import math

S = input()
T = input()

s_idx = 0
t_idx = 0

while True:
    if s_idx == len(S) or t_idx == len(T):
        if s_idx == len(S) and t_idx == len(T):
            print("Yes")
        else:
            rest = list(set(T[t_idx:]))

            if rest:
                if len(rest) == 1 and rest[0] == S[s_idx - 1]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")

        break
    # print(s_idx, t_idx, S[s_idx], T[t_idx])

    if S[s_idx] == T[t_idx]:
        s_idx += 1
        t_idx += 1
    else:
        if s_idx == 0 or s_idx == 1:
            print("No")
            break

        if S[s_idx - 1] == T[t_idx] and S[s_idx - 2] == T[t_idx]:
            t_idx += 1
        else:
            print("No")
            break
