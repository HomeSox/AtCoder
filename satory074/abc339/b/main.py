H, W, N = map(int, input().split())

G = [["." for _ in range(W)] for _ in range(H)]
x, y = 0, 0

l = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dxy_idx = 0
for i in range(N):
    # print(l[dxy_idx])

    if G[y][x] == ".":
        G[y][x] = "#"
        dxy_idx = (dxy_idx + 1) % 4
    else:
        G[y][x] = "."
        dxy_idx = (dxy_idx + 4 - 1) % 4

    dx, dy = l[dxy_idx]
    x = (x + dx + W) % W
    y = (y + dy + H) % H

for g in G:
    print("".join(g))
