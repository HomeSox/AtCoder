T = int(input())

for _ in range(T):
    N = int(input())
    sN = str(N)
    lN = len(sN)
    ans = 10 ** (len(sN) - 1) - 1

    for d in range(1, lN // 2 + 1):
        if lN % d:
            continue

        q = lN // d

        n = sN[:d]
        if int(n * q) <= N:
            ans = max(ans, int(n * q))

        n = str(int(n) - 1)
        if int(n * q) <= N:
            ans = max(ans, int(n * q))

    print(ans)
