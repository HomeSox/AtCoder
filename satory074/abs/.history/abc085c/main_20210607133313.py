n, y = map(int, input().split())

for n1 in range(n+1):
    for n2 in range(n+1):
        for n3 in range(n+1):
            if n1 + n2 + n3 > n:
                break

            if (n1 * 1000 + n2 * 5000 + n3 * 10000) == y:
                print(n1, n2, n3)
                exit()
else:
    print(-1, -1, -1)