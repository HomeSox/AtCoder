G = [input().strip() for _ in range(8)]

rows = sum(1 for row in G if '#' not in row)

cols = 0
for col in range(8):
    if all(G[row][col] == '.' for row in range(8)):
        cols += 1

print(rows * cols)

