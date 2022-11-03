from collections import deque

N, M = map(int, input().split())

ldist = []
for x in range(-N, N):
    for y in range(-N, N):
        if x**2 + y**2 == M:
            ldist.append((x, y))

ans = [[-1 for _ in range(N)] for _ in range(N)]
ans[0][0] = 0

q = deque([])
q.appendleft((0, 0))

while q:
    x, y = q.pop()

    for x_, y_ in ldist:
        x_ += x
        y_ += y

        if not 0 <= x_ < N:
            continue

        if not 0 <= y_ < N:
            continue

        if ans[x_][y_] != -1:
            continue

        ans[x_][y_] = ans[x][y] + 1
        q.appendleft((x_, y_))

[print(*l) for l in ans]
