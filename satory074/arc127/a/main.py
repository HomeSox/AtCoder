N = int(input())

ans = 0
for k in range(1, 16):
    for d in range(k, 17):
        l = int("1" * k + "0" * (d - k))
        r = min(int("1" * k + "9" * (d - k)), N)

        ans += max(0, r - l + 1)

print(ans)
