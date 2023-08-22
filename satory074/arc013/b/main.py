C = int(input())

ans = [-1, -1, -1]
for _ in range(C):
    NML = list(map(int, input().split()))
    N, M, L = sorted(NML)

    ans[0] = max(ans[0], N)
    ans[1] = max(ans[1], M)
    ans[2] = max(ans[2], L)

print(ans[0] * ans[1] * ans[2])

