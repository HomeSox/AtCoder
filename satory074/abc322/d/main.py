P1 = [list(input()) for _ in range(4)]
P2 = [list(input()) for _ in range(4)]
P3 = [list(input()) for _ in range(4)]
P = [P1, P2, P3]


def rotate(v):
    w = [list(row) for row in v]
    for i in range(4):
        for j in range(4):
            w[j][3 - i] = v[i][j]

    return w


def can_put(exist, P, di, dj):
    for i in range(4):
        for j in range(4):
            if P[i][j] == "#":
                ni, nj = i + di, j + dj

                if not (0 <= ni < 4 and 0 <= nj < 4):
                    return False

                if exist[ni][nj] == 1:
                    return False

                exist[ni][nj] = 1

    return True


def dfs(i, l, P):
    if i == 3:
        if all(cell == 1 for row in l for cell in row):
            print("Yes")
            exit()

        return

    for di in range(-3, 4):
        for dj in range(-3, 4):
            ex2 = [row[:] for row in l]

            if can_put(ex2, P[i], di, dj):
                dfs(i + 1, ex2, P)


for _ in range(4):
    for _ in range(4):
        l = [[0 for _ in range(4)] for _ in range(4)]
        dfs(0, l, P)
        P[2] = rotate(P[2])

    P[1] = rotate(P[1])

print("No")
exit()
