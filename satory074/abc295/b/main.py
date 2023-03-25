R, C = map(int, input().split())
B = [input() for _ in range(R)]


B_ = [list(row) for row in B]
for r in range(R):
    for c in range(C):
        if B[r][c] == "." or B[r][c] == "#":
            continue

        B_[r][c] = "."
        for nr in range(R):
            if not 0 <= nr < R:
                continue

            for nc in range(C):
                if not 0 <= nc < C:
                    continue

                if abs(r - nr) + abs(c - nc) > int(B[r][c]):
                    continue

                B_[nr][nc] = "."

[print("".join(row)) for row in B_]
