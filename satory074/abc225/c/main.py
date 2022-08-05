N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M-1):
        if B[i][j] + 1 != B[i][j+1]:
            exit(print("No"))

        if B[i][j] % 7 == 0:
            exit(print("No"))

for j in range(M):
    for i in range(N-1):
        if B[i][j] + 7 != B[i+1][j]:
            exit(print("No"))

print("Yes")
