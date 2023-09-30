N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = [0 for _ in range(N + 1)]

# print(*ans)

cur = A.pop(-1)
for i in range(N):
    # print(cur, i, ans[i], A)
    # print(ans)

    ans[i] = cur - i
    if A:
        if i == cur:
            cur = A.pop(-1)

for a in ans[1:]:
    print(a)

