n, y = map(int, input().split())

for n1 in range(n+1):
    for n2 in range(n+1):
        for n3 in range(n+1):
            if n1 + n2 + n3 != n:
                continue

            if n1 * 10000 + n2 * 5000 + n3 * 1000 == y:
                print(n1, n2, n3)
                exit()
else:
    print(-1, -1, -1)