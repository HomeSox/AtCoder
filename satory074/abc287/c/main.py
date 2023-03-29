import collections as cl
import math

N, M = map(int, input().split())

count = [0 for _ in range(N + 1)]
connect = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())

    count[u] += 1
    count[v] += 1
    connect[u].append(v)
    connect[v].append(u)

one = []
for i, c in enumerate(count[1:]):
    if c != 2:
        if c == 1 and len(one) < 2:
            one.append(i + 1)
        else:
            print("No")
            exit()

if len(one) == 2:
    is_visit = [False for _ in range(N + 1)]
    cur = one[0]
    prev = one[0]
    for i in range(N):
        is_visit[cur] = True

        if len(connect[cur]) == 2:
            c1, c2 = connect[cur]
            if prev == c1:
                prev = cur
                cur = c2
            if prev == c2:
                prev = cur
                cur = c1
        else:
            cur = connect[cur][0]

    # print(is_visit)
    for b in is_visit[1:]:
        if not b:
            print("No")
            exit()

    print("Yes")
else:
    print("No")

# print(count)
# print(connect)
# print(one)
