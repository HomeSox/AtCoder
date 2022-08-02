X, Y, A, B = map(int, input().split())

ans = 0
tsuyosa = X
for _ in range(10**9):
    if tsuyosa * A > tsuyosa + B:
        break

    if tsuyosa * A >= Y:
        break

    tsuyosa *= A
    ans += 1

print(ans + (Y - tsuyosa - 1) // B)