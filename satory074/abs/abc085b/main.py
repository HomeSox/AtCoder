n = int(input())
d = [int(input()) for _ in range(n)]

d.sort(reverse=True)

if len(d) == 1:
    print(1)
    exit()

ans = 1
for d1, d2 in zip(d[:-1], d[1:]):
    if d1 > d2:
        ans += 1

print(ans)