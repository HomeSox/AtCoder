N = int(input())
qr = [list(map(int, input().split())) for _ in range(N)]
# print(qr)

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())

    q, r = qr[t - 1]
    shuushuubi = r + (d // q) * q

    if d % q > r:
        shuushuubi += q

    print(shuushuubi)
    # print(t, d, q, r, d % q, d // q)
