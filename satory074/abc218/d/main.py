N = int(input())

xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))

xy_set = set(xy)

ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        if x1 >= x2:
            continue

        if y1 >= y2:
            continue

        if (x1, y2) in xy_set and (x2, y1) in xy_set:
            ans += 1

print(ans)