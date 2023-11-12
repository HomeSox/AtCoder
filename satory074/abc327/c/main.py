S = [list(input().split()) for _ in range(9)]

# 行
for row in S:
    if len(set(row)) != 9:
        print("No")
        exit()

# 列
for col in range(9):
    if len(set(S[row][col] for row in range(9))) != 9:
        print("No")
        exit()

# 部屋
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        block = []
        for k in range(3):
            for l in range(3):
                block.append(S[i + k][j + l])

        if len(set(block)) != 9:
            print("No")
            exit()

print("Yes")
