import collections as cl
import math

N = int(input())
a = list(map(int, input().split()))

a_sort = [(a, i + 1) for i, a in enumerate(a)]
# a_sort.sort(key=lambda x: x[0])

li = [False]
for i in range(N):
    if a_sort[i][0] == a_sort[i][1]:
        li.append(True)
    else:
        li.append(False)

Q = [0] * (len(li) + 1)
for i, b in enumerate(li):
    Q[i + 1] = Q[i] + int(b)

# print(a_sort)
# print(li)
# print(Q)

ans = 0
for i, (a, idx) in enumerate(a_sort):
    # print(a_sort[a - 1][0], i, a, idx)
    if a == idx:
        ans += Q[-1] - Q[a + 1]
    else:
        if a_sort[a - 1][0] == idx:
            if a_sort[a - 1][1] > idx:
                ans += 1


print(ans)
