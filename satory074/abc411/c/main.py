N, Q = map(int, input().split())
A = list(map(int, input().split()))

black_cells = set()
ans = 0

for a in A:
    left_is_black = (a - 1) in black_cells
    right_is_black = (a + 1) in black_cells

    if a in black_cells:
        if left_is_black and right_is_black:
            ans += 1
        elif not left_is_black and not right_is_black:
            ans -= 1
        black_cells.remove(a)
    else:
        if left_is_black and right_is_black:
            ans -= 1
        elif not left_is_black and not right_is_black:
            ans += 1
        black_cells.add(a)

    print(ans)

