import collections as cl
import math

N = int(input())
P = list(map(int, input().split()))
rP = P[::-1]
left = [p for p in P]

can_use = [False for _ in range(N + 1)]
can_use[P[-1]] = True
mi = P[-1]
li = [P[-1]]
for i, p in enumerate(rP):
    left.pop(-1)

    if i == 0:
        continue

    can_use[p] = True
    li.append(p)
    if p < mi:
        mi = min(mi, p)
    else:
        target = li[-1]
        rep = -1
        for l in li:
            if l < target:
                rep = max(l, rep)

        right = []
        for l in li:
            if l == rep:
                continue

            right.append(l)
        right.sort(reverse=True)

        # print(i, left, rep, right, li)

        break

print(*left, rep, *right)


# print(P)
# print(rP)
# print(can_use)
