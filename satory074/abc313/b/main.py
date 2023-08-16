N, M = map(int, input().split())
deg = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[b] += 1

# print(deg)

ans = -1
for i in range(N):
    if deg[i] == 0:
        if ans != -1:
            print(-1)
            exit()
        else:
            ans = i + 1

print(ans)