N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
sa = 0
total_r = 0
for l, r in LR:
    sa += l
    total_r += r

if sa > 0 or total_r < 0:
    print("No")
    exit()

ans = []
for l, r in LR:
    d = min(r - l, -sa)
    ans.append(l + d)
    sa += d

if sa < 0:
    print("No")
    exit()

print("Yes")
print(*ans)
