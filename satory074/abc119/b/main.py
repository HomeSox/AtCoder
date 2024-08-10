N = int(input())

ans = 0
for _ in range(N):
    x, u = input().split()

    if u == "JPY":
        ans += int(x)
        continue

    ans += 380000.0 * float(x)

print(ans)
