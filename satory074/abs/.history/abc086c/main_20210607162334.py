n = int(input())

current = (0, 0)

txy = [tuple(map(int, input().split())) for _ in range(n)]
txy.insert(0, (0, 0, 0))

ans = 'No'
for (t1, x1, y1), (t2, x2, y2) in zip(txy[:-1], txy[1:]):
    dt = t2 - t1
    dx = x2 - x1
    dy = y2 - y1

    if dx + dy < dt:
        break

    if (dx + dy) % 2 == 0 and dt % 2 == 0:
        continue
    elif (dx + dy) % 2 == 1 and dt % 2 == 1:
        continue
    else:
        break
else:
    ans = 'Yes'

print(ans)