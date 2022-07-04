N, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[0], reverse=True)

ans = 0
for a, b in AB:
    if W >= b:
        W -= b
        ans += a * b
    else:
        ans += a * W
        break

print(ans)
