from itertools import product

H, W = map(int, input().split())
S = [input() for _ in range(H)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for i, j in product(range(H), range(W)):
    for dx, dy in direction:

        t = ""
        for k in range(5):
            x = i + dx * k
            y = j + dy * k

            if 0 <= x < H and 0 <= y < W:
                t += S[x][y]

        # print(t)

        if t == "snuke":
            for k in range(5):
                x = i + dx * k
                y = j + dy * k

                print(x + 1, y + 1)

            exit()

print("No")
