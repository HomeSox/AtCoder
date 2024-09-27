A, K = map(int, input().split())

ans = 0
cur = A
for i in range(10**9):
    if cur >= 2 * (10**12):
        print(ans)
        break
    else:
        cur = 1 + (K * cur)
