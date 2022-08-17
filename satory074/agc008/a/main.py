x, y = map(int, input().split())

ans = 10**10
for n in range(4):
    x1 = x
    y1 = y
    ans1 = 0
    # nの2進数
    b = bin(n)[2:]
    # 0埋め
    b = b.zfill(2)

    if b[0] == '1':
        x1 *= -1
        ans1 += 1


    if b[1] == '1':
        y1 *= -1
        ans1 += 1

    if x1 <= y1:
        ans = min(ans, y1 - x1 + ans1)

print(ans)


