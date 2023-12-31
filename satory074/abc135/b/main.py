N = int(input())
p = list(map(int, input().split()))

cnt = 0
for p1, p2 in zip(p, sorted(p)):
    if p1 != p2:
        cnt += 1

if cnt == 0 or cnt == 2:
    print('YES')
else:
    print('NO')
