H, W = map(int, input().split())
G = [input() for _ in range(H)]

visited = [[False for _ in range(W)] for _ in range(H)]


def is_valid(x, y, visited, g):
    if not (0 <= x < H):
        return False

    if not (0 <= y < W):
        return False

    if visited[x][y]:
        return False

    if g[x][y] != "#":
        return False

    return True


def dfs(x, y, visited, g):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if not is_valid(x, y, visited, g):
            continue

        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stack.append((nx, ny))


count = 0
for i in range(H):
    for j in range(W):
        if G[i][j] != "#":
            continue

        if visited[i][j]:
            continue

        dfs(i, j, visited, G)
        count += 1

print(count)
