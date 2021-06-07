n = int(input())

current = (0, 0)

txy = [tuple(map(int, input().split())) for _ in range(n)]

for (t1, x1, y1), (t2, x2, y2) in zip(txy[:-1], txy[1:]):
    print(t1, t2)