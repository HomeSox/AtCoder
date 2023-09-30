P1 = [list(input()) for _ in range(4)]
P2 = [list(input()) for _ in range(4)]
P3 = [list(input()) for _ in range(4)]

def check(P1, P2, P3):
    marked_positions = set()

    for grid in [P1, P2, P3]:
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '#':
                    if (i, j) in marked_positions:
                        return False# 重複が見つかった場合

                    marked_positions.add((i, j))

    return True

def rotate(grid):
    return [list(row)[::-1] for row in zip(*grid)]

for i1 in range(4):
    P1 = rotate(P1)

    for i2 in range(4):
        P2 = rotate(P2)

        for i3 in range(4):
            P3 = rotate(P3)

            if check(P1, P2, P3):
                [print(''.join(row)) for row in P1]
                [print(''.join(row)) for row in P2]
                [print(''.join(row)) for row in P3]
                print('Yes')
                exit()

print('No')