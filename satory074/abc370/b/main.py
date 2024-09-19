N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(len(A[i])):
        A[i][j] -= 1

ans = 0
for i in range(N):
    if ans >= i:
        ans = A[ans][i]
    else:
        ans = A[i][ans]

print(ans + 1)
