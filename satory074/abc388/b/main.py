N, D = map(int, input().split())
TL = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, D + 1):
    li = [l + i for _, l in TL]

    ans = []
    for (t, _), l in zip(TL, li):
        ans.append(t * l)

    print(max(ans))
