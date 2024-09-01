h, m = map(int, input().split())

for _ in range(3600):
    A, B = f"{h:02d}"
    C, D = f"{m:02d}"
    # print(f"{A}{B}:{C}{D}")
    # print(f"{A}{C}:{B}{D}")

    if 0 <= int(f"{A}{C}") <= 23 and 0 <= int(f"{B}{D}") <= 59:
        print(int(f"{A}{B}"), int(f"{C}{D}"))
        break

    m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
