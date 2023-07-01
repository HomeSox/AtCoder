import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
G = [input() for _ in range(H)]

snuke = 'snuke'

visited = set()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def next_char(c):
    return snuke[(snuke.index(c) + 1) % len(snuke)]

def is_valid(x, y):
    return 0 <= x < H and 0 <= y < W and (x, y) not in visited

def dfs(x, y, c):
    if (x, y) == (H-1, W-1):
        return True

    visited.add((x, y))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if is_valid(nx, ny) and G[nx][ny] == next_char(c):
            if dfs(nx, ny, G[nx][ny]):
                return True

    return False

if dfs(0, 0, 's'):
    print("Yes")
else:
    print("No")
