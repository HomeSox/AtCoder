N = int(input())
H = list(map(int, input().split()))

for i, h in enumerate(H):
    if i == 0:
        continue

    if H[0] < h:
        print(i + 1)
        exit()

print(-1)