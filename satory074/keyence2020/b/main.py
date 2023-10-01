N = int(input())
robots = []
for _ in range(N):
    x, l = map(int, input().split())
    robots.append((x + l, x - l))

robots.sort()

cur = -float("inf")
ans = 0
for r in robots:
    if cur <= r[1]:
        ans += 1
        cur = r[0]

print(ans)
