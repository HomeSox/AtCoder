H, W = map(int, input().split())
Si, Sj = map(int, input().split())
Si -= 1
Sj -= 1
C = [list(input()) for _ in range(H)]
X = input()

for x in X:
    if x == "L":
        if Sj == 0:
            continue

        if C[Si][Sj - 1] == ".":
            Sj -= 1

        continue

    if x == "R":
        if Sj == W - 1:
            continue

        if C[Si][Sj + 1] == ".":
            Sj += 1

        continue

    if x == "U":
        if Si == 0:
            continue

        if C[Si - 1][Sj] == ".":
            Si -= 1

        continue

    if x == "D":
        if Si == H - 1:
            continue

        if C[Si + 1][Sj] == ".":
            Si += 1

        continue

print(Si + 1, Sj + 1)
