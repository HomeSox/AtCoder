from collections import deque

H, W = map(int, input().split())
G = [input() for _ in range(H)]

SNUKE = "snuke"
que = deque()
visited = [[False for _ in range(W)] for _ in range(H)]

que.append((0, 0, 0))
while que:
    i, j, step = que.popleft()
    if i < 0 or i >= H or j < 0 or j >= W or visited[i][j] or G[i][j] != SNUKE[step % len(SNUKE)]:
        continue
    
    visited[i][j] = True
    if i == H - 1 and j == W - 1:
        print("Yes")
        break
    
    que.append((i - 1, j, step + 1))
    que.append((i, j - 1, step + 1))
    que.append((i + 1, j, step + 1))
    que.append((i, j + 1, step + 1))
else:
    print("No")
