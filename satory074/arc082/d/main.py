n = int(input())
p = list(input().split())

ans = 0
c = 0
for i, p_ in enumerate(p[:-1]):
    if p_ == i + 1:
        p[i], p[i+1] = i[i+1], i[i]
        ans += 1

print(ans)

