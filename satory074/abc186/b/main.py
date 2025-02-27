H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

mi = 10**18
for a in A:
    mi = min(mi, min(a))

# print(mi)

ans = 0
for a in A:
    for n in a:
        ans += n - mi

print(ans)
