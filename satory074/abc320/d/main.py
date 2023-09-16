from collections import deque

N, M = map(int, input().split())

G = [{} for _ in range(N + 1)]
for _ in range(M):
    A, B, X, Y = map(int, input().split())

    G[A][B] = (X, Y)
    G[B][A] = (-X, -Y)

zahyo = [[None, None] for _ in range(N + 1)]
is_visited = [False for _ in range(N + 1)]

zahyo[1] = [0, 0]
is_visited[1] = True

queue = deque([1])
while queue:
    current = queue.popleft()
    for n, (dx, dy) in G[current].items():
        if is_visited[n]:
            continue

        is_visited[n] = True

        x, y = zahyo[current]
        zahyo[n] = [x + dx, y + dy]

        queue.append(n)

for x, y in zahyo[1:]:
    if x is None:
        print("undecidable")
    else:
        print(x, y)