M = int(input())
D = list(map(int, input().split()))

mid = sum(D) // 2 + 1

for m in range(M):
    for d in range(D[m]):
        mid -= 1

        if mid == 0:
            print(m + 1, d + 1)
            exit()