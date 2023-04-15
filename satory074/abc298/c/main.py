import collections as cl
import math

N = int(input())
Q = int(input())

num2box = [[] for _ in range(2 * 10 ** 5 + 1)]
box2num = [[] for _ in range(2 * 10 ** 5 + 1)]

for _ in range(Q):
    ipt = list(map(int, input().split()))

    if ipt[0] == 1:
        i = ipt[1]
        j = ipt[2]

        num2box[i].append(j)
        box2num[j].append(i)

    if ipt[0] == 2:
        i = ipt[1]

        box2num[i] = sorted(box2num[i])
        print(*box2num[i])

    if ipt[0] == 3:
        i = ipt[1]

        num2box[i] = sorted(set(num2box[i]))
        print(*num2box[i])


