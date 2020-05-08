A, B, X = map(int, input().split())


def is_buy(N):
    return X >= A * N + B * len(str(N))


def bi(l, r):
    m = (l + r) // 2

    # print(is_buy(m), l, m, r)
    if m == l or m == r:
        print(m if is_buy(m) else 0)
        exit()

    if is_buy(m):
        bi(m, r)
    else:
        bi(l, m)


if is_buy(10**9):
    print(10**9)
else:
    bi(0, 10**9)
