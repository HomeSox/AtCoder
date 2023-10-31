N = int(input())
S = list(input())

S.sort()
ans = 0
for n in range(int((10 ** N) ** 0.5) + 1):
    s = list(str(n * n).zfill(N))
    s.sort()

    if s == S:
        ans += 1
        # print(n * n)

print(ans)