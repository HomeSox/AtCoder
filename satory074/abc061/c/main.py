N, K = map(int, input().split())

ab = [tuple(map(int, input().split())) for _ in range(N)]

ab.sort(key=lambda x: x[0])

idx = 0
for a, b in ab:
    idx += b

    if idx >= K:
        print(a)
        exit()
