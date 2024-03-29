n = int(input())
txy = [tuple(map(int, input().split())) for _ in range(n)]
txy.insert(0, (0, 0, 0))

ans = 'No'
for (t1, x1, y1), (t2, x2, y2) in zip(txy[:-1], txy[1:]):
    dt = abs(t2 - t1)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx + dy > dt:
        break

    if abs(dx + dy - dt) % 2 == 0:
        continue
    else:
        break
else:
    ans = 'Yes'

print(ans)