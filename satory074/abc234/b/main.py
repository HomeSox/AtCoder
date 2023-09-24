N = int(input())
xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))

ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        if ans < ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5:
            ans = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(ans)
