from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
deg = [0 for _ in range(N)]

for _ in range(M):
    A, B, C, D = input().split()
    A, C = int(A) - 1, int(C) - 1

    G[A].append(C)
    G[C].append(A)

    deg[A] += 1
    deg[C] += 1

x, y = 0, 0
used = [False for _ in range(N)]
for i in range(N):
    if used[i]:
        continue

    que = deque([i])
    used[i] = True

    f = True
    while que:
        q = que.popleft()

        if deg[q] != 2:
            f = False

        for v in G[q]:
            if used[v]:
                continue

            que.append(v)
            used[v] = True

    if f:
        x += 1
    else:
        y += 1

print(x, y)