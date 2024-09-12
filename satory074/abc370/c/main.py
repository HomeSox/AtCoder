S = list(input())
T = list(input())

ans = []
while "".join(S) != "".join(T):
    change = ["z" for _ in range(len(S))]
    for i, (s, t) in enumerate(zip(S, T)):

        if s != t:
            S_ = [s for s in S]
            S_[i] = T[i]

            change = list(min("".join(S_), "".join(change)))

    ans.append(change)
    S = [s for s in change]

    # for a in ans:
    # print("".join(a))
    # print()
#
print(len(ans))
for a in ans:
    print("".join(a))
